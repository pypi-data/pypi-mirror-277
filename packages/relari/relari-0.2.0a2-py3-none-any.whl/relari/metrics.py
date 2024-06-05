from enum import Enum
from typing import List, Union, Dict, TypedDict, Any

class ToolCall(TypedDict):
    name: str
    kwargs: Dict[str, Any]


class Metric(Enum):
    SingleLabelClassification = (
        "SingleLabelClassification",
        {"predicted_class": Union[str, int, List[float]]},
        {"ground_truth_class": Union[str, int]},
    )
    CodeStringMatch = (
        "CodeStringMatch",
        {"answer": str},
        {"ground_truth_answers": List[str]},
    )
    PythonASTSimilarity = (
        "PythonASTSimilarity",
        {"answer": str},
        {"ground_truth_answers": Union[List[str], str]},
    )
    DeterministicFaithfulness = (
        "DeterministicFaithfulness",
        {"answer": str},
        {"retrieved_context": Union[List[str], str]},
    )
    DeterministicAnswerCorrectness = (
        "DeterministicAnswerCorrectness",
        {"answer": str},
        {"ground_truth_answers": Union[List[str], str]},
    )
    FleschKincaidReadability = ("FleschKincaidReadability", {"answer": str}, dict())
    PrecisionRecallF1 = (
        "PrecisionRecallF1",
        {"retrieved_context": List[str]},
        {"ground_truth_context": List[str]},
    )
    RankedRetrievalMetrics = (
        "RankedRetrievalMetrics",
        {"retrieved_context": List[str]},
        {"ground_truth_context": List[str]},
    )
    ToolSelectionAccuracy = (
        "ToolSelectionAccuracy",
        {"tools": List[ToolCall]},
        {"ground_truths": List[ToolCall]},
    )
    LLMBasedFaithfulness = (
        "LLMBasedFaithfulness",
        {"answer": str, "question": str},
        dict(),
    )
    LLMBasedAnswerCorrectness = (
        "LLMBasedAnswerCorrectness",
        {"question": str, "answer": str},
        {"ground_truth_answers": Union[List[str], str]},
    )
    LLMBasedAnswerRelevance = (
        "LLMBasedAnswerRelevance",
        {"question": str, "answer": str},
        dict(),
    )
    LLMBasedStyleConsistency = (
        "LLMBasedStyleConsistency",
        {"answer": str},
        {"ground_truth_answers": Union[List[str], str]},
    )
    LLMBasedContextPrecision = (
        "LLMBasedContextPrecision",
        {"question": str, "retrieved_context": List[str]},
        dict(),
    )
    LLMBasedContextCoverage = (
        "LLMBasedContextCoverage",
        {"question": str, "retrieved_context": List[str]},
        {"ground_truth_answers": Union[List[str], str]},
    )

    def __init__(self, value, mandatory, optional):
        self._value_ = value
        self.mandatory = mandatory
        self.optional = optional


class SingleLabelClassification:
    def __init__(self, name, description):
        self.name = name
        self.description = description
