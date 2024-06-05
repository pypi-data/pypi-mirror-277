from enum import Enum
from typing import List


class Scorers(str, Enum):
    toxicity = "toxicity"
    factuality = "factuality"
    correctness = "factuality"
    groundedness = "groundedness"
    context_adherence = "groundedness"
    context_adherence_plus = "groundedness"
    pii = "pii"
    latency = "latency"
    context_relevance = "context_relevance"
    sexist = "sexist"
    tone = "tone"
    prompt_perplexity = "prompt_perplexity"
    chunk_attribution_utilization_gpt = "chunk_attribution_utilization_gpt"
    chunk_attribution_utilization_plus = "chunk_attribution_utilization_gpt"
    completeness_gpt = "completeness_gpt"
    completeness_plus = "completeness_gpt"
    prompt_injection = "prompt_injection"
    adherence_basic = "adherence_nli"
    context_adherence_basic = "adherence_nli"
    completeness_basic = "completeness_nli"
    chunk_attribution_utilization_basic = "chunk_attribution_utilization_nli"
    adherence_luna = "adherence_nli"
    context_adherence_luna = "adherence_nli"
    completeness_luna = "completeness_nli"
    chunk_attribution_utilization_luna = "chunk_attribution_utilization_nli"

    @staticmethod
    def basic_deprecated_scorer_names() -> List["Scorers"]:
        return [
            Scorers.adherence_basic,
            Scorers.completeness_basic,
            Scorers.context_adherence_basic,
            Scorers.chunk_attribution_utilization_basic,
        ]
