from collections import defaultdict
from enum import Enum
from itertools import groupby
from typing import Type, cast, List, Optional, Dict

from collections_extended import RangeMap
from log_with_context import add_logging_context, Logger
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.processor import ProcessorParameters, ProcessorBase
from pymultirole_plugins.v1.schema import Document, Annotation

logger = Logger("pymultirole")


class WrappedTerm(object):
    def __init__(self, term):
        self.term = term
        self.status = term.properties.get('status', "") if term.properties else ""

    def __eq__(self, other):
        return self.term.identifier == other.term.identifier and self.status == other.status

    def __hash__(self):
        return hash((self.term.identifier, self.status))


class ReconciliationType(str, Enum):
    linker = "linker"


class ReconciliationParameters(ProcessorParameters):
    type: ReconciliationType = Field(
        ReconciliationType.linker,
        description="""Type of consolidation, use<br />
    <li>**linker** to retain only known entities (extracted by a model)<br />"""
    )
    kill_label: Optional[str] = Field(None, description="Label name of the kill list", extra="label,advanced")
    white_label: Optional[str] = Field(
        None, description="Label name of the white list", extra="label,advanced"
    )
    person_label: Optional[str] = Field(
        None, description="Label name of the person to apply the lastname resolution", extra="label,advanced"
    )
    remove_suspicious: bool = Field(
        True,
        description="Remove suspicious annotations extracted by the model (numbers, percentages, phrases without uppercase words)",
        extra="advanced"
    )
    resolve_lastnames: bool = Field(
        False,
        description="Try to resolve isolated family names if they have been seen before in the document",
        extra="advanced"
    )


class ReconciliationProcessor(ProcessorBase):
    """Reconciliation processor ."""

    def process(
            self, documents: List[Document], parameters: ProcessorParameters
    ) -> List[Document]:  # noqa: C901
        params: ReconciliationParameters = cast(ReconciliationParameters, parameters)
        for document in documents:
            with add_logging_context(docid=document.identifier):
                if document.annotations:
                    annotations = [a for a in document.annotations if a.labelName != 'sentence']
                    mark_whitelisted(annotations, params.white_label)
                    ann_groups = group_annotations(annotations, keyfunc=by_lexicon)
                    # Consolidate & links against KB and Wikidata
                    if params.type == ReconciliationType.linker:
                        conso_anns = consolidate_linker(document.text,
                                                        ann_groups,
                                                        params
                                                        )
                    document.annotations = conso_anns
        return documents

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return ReconciliationParameters


def mark_whitelisted(annotations, white_label):
    for a in annotations:
        if (
                a.labelName == white_label
        ):  # Consider whitelisted terms as entities coming from the model
            a.terms = None


def consolidate_linker(
        text,
        ann_groups,
        params: ReconciliationParameters
):
    conso_anns = []
    kb_names = [
        item
        for item in ann_groups.keys()
        if item not in ["", params.kill_label, params.white_label]
    ]
    for model_r in ann_groups[""].ranges():
        model_ann = model_r.value

        if params.remove_suspicious and is_suspicious(model_ann):
            logger.warning("Kill suspicious annotation")
            logger.warning(f"=> {model_ann}")
            continue
        kill_r = annotation_in_group(model_ann, ann_groups, [params.kill_label])
        perfect, kill_match = one_match(model_ann, kill_r)
        if perfect and kill_match:
            logger.warning("Kill annotation")
            logger.warning(f"=> {model_ann}")
            continue

        kb_r = annotation_in_group(model_ann, ann_groups, kb_names)
        perfect, kb_match = one_match(model_ann, kb_r)
        if kb_match:
            if perfect:
                if model_ann.labelName == kb_match.labelName or model_ann.labelName == params.white_label:
                    model_ann.labelName = kb_match.labelName
                    model_ann.label = kb_match.label
                    model_ann.terms = model_ann.terms or []
                    model_ann.terms.extend(kb_match.terms)
                else:
                    logger.warning("Found wrong label annotation in KB")
                    logger.warning(f"=> {model_ann}")
                    logger.warning("and")
                    logger.warning(f" -{kb_match}")
            else:
                logger.warning("Found larger annotation in KB")
                logger.warning(f"=> {model_ann}")
                logger.warning("and")
                logger.warning(f" -{kb_match}")
        elif kb_r and len(kb_r) > 1:
            logger.warning("Found overlapping annotations in KB")
            logger.warning(f"=> {model_ann}")
            logger.warning("and")
            for r in kb_r.values():
                logger.warning(f" -{r}")

        # wiki_r = annotation_in_group(model_ann, ann_groups, [params.wikidata_label])
        # perfect, wiki_match = one_match(model_ann, wiki_r)
        # if wiki_match:
        #     if validate_wiki_type(wiki_match, gname):
        #         if perfect:
        #             model_ann.terms = model_ann.terms or []
        #             wiki_match.terms[0].properties.pop("fingerprint", None)
        #             model_ann.terms.extend(wiki_match.terms)
        #         else:
        #             logger.warning("Found larger annotation in Wikidata")
        #             logger.warning(f"=> {model_ann}")
        #             logger.warning("and")
        #             logger.warning(f" -{wiki_match}")
        # elif wiki_r and len(wiki_r) > 1:
        #     logger.warning("Found overlapping annotations in Wikidata")
        #     logger.warning(f"=> {model_ann}")
        #     logger.warning("and")
        #     for r in wiki_r.values():
        #         logger.warning(f" -{r}")
        conso_anns.append(model_ann)
    sorted_annotations = sorted(conso_anns,
                                key=natural_order,
                                reverse=True,
                                )
    seen_names = defaultdict(set)
    if params.resolve_lastnames:
        for ann in sorted_annotations:
            if ann.labelName == 'person':
                lastnames = person_lastnames(ann, text)
                if lastnames is not None:
                    for i in range(len(lastnames)):
                        composed_name = ' '.join(lastnames[i:])
                        if has_knowledge(ann) and len(lastnames) > 1:
                            for t in ann.terms:
                                seen_names[composed_name].add(WrappedTerm(t))
                        else:
                            if composed_name in seen_names:
                                ann.terms = [wt.term for wt in seen_names[composed_name]]
                                break

    return sorted_annotations


def group_annotations(annotations, keyfunc):
    groups = defaultdict(RangeMap)
    sorted_annotations = sorted(annotations, key=keyfunc)
    for k, g in groupby(sorted_annotations, keyfunc):
        sorted_group = sorted(g, key=left_longest_match, reverse=True)
        for a in sorted_group:
            addit = True
            if a.start in groups[k] and a.end - 1 in groups[k]:
                b = groups[k][a.start]
                if a.start - b.start == 0 and a.end - b.end == 0:
                    terms = set(WrappedTerm(t) for t in b.terms) if b.terms else set()
                    if a.terms:
                        terms.update(set(WrappedTerm(t) for t in a.terms))
                    b.terms = [t.term for t in terms]
                    addit = False
            if addit:
                groups[k][a.start:a.end] = a
    return groups


def left_longest_match(a: Annotation):
    return a.end - a.start, -a.start


def natural_order(a: Annotation):
    return -a.start, a.end - a.start


def has_knowledge(a: Annotation):
    return a.terms is not None and a.terms


def is_whitelist(a: Annotation):
    if has_knowledge(a):
        for term in a.terms:
            props = term.properties or {}
            status = props.get("status", "")
            if "w" in status.lower():
                return True
    return False


def person_lastnames(a: Annotation, text):
    if 'person' in a.labelName:
        atext = a.text or text[a.start:a.end]
        words = atext.split()
        return words
    return None


def by_lexicon(a: Annotation):
    if a.terms:
        lex = a.terms[0].lexicon.split("_")
        return lex[0]
    else:
        return ""


def by_lexicon_or_label(a: Annotation):
    if a.terms:
        lex = a.terms[0].lexicon.split("_")
        return lex[0]
    else:
        return a.labelName


def by_label(a: Annotation):
    return a.labelName


def one_match(a: Annotation, matches: RangeMap):
    match = None
    perfect = False
    if matches and len(matches) >= 1:
        for match in matches.values():
            perfect = a.start == match.start and a.end == match.end
            if perfect:
                break
    return perfect, match


def is_suspicious(a: Annotation):
    suspicious = False
    if a.text:
        words = a.text.split()
        has_upper = any([w[0].isupper() for w in words])
        suspicious = not has_upper
    return suspicious


# noqa: W503
def annotation_in_group(
        a: Annotation, ann_groups: Dict[str, RangeMap], gnames: List[str] = None
):
    gname = by_lexicon_or_label(a)
    if gname in gnames:
        gnames = [gname]
    for gname in gnames:
        if (
                gname in ann_groups
                and a.start in ann_groups[gname]
                or a.end in ann_groups[gname]
        ):
            ga = ann_groups[gname][a.start: a.end]
            return ga
    return None
