"""Mythos synthesis for Myosotis UI/UX, BI, and machine intelligence.

The module translates a product prompt plus optional business-intelligence
signals into a compact blueprint that can guide generation, interface copy, and
analytics.  Its three motifs are intentionally named for the project request:

* mythos: narrative intent for myths and user-facing story frames.
* mitosis: branching variants for experiments, cohorts, or generated scenes.
* osmosis: absorption of observed signals into safer model controls.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import tanh
from typing import Mapping


@dataclass(frozen=True)
class MythosSignal:
    """Business-intelligence signal normalized for experience synthesis."""

    name: str
    value: float
    weight: float = 1.0

    def normalized(self) -> float:
        """Return the weighted signal compressed into the inclusive [0, 1] range."""

        compressed = (tanh(self.value * self.weight) + 1.0) / 2.0
        return max(0.0, min(1.0, compressed))


@dataclass(frozen=True)
class MythosBlueprint:
    """A UI/UX, BI, and model-control blueprint for a Myosotis experience."""

    theme: str
    mythos: str
    mitosis: tuple[str, ...]
    osmosis: tuple[str, ...]
    ui_microcopy: tuple[str, ...]
    model_controls: Mapping[str, float]
    bi_summary: Mapping[str, float] = field(default_factory=dict)

    def prompt_prelude(self) -> str:
        """Build a generation prelude suitable for Lila-E8 prompts."""

        branches = ", ".join(self.mitosis)
        absorbed = ", ".join(self.osmosis)
        return (
            f"Mythos: {self.mythos}\n"
            f"Mitosis branches: {branches}\n"
            f"Osmosis signals: {absorbed}\n"
            f"Theme: {self.theme}"
        )


def _slug_to_title(text: str) -> str:
    words = [word for word in text.replace("_", " ").replace("-", " ").split() if word]
    return " ".join(word.capitalize() for word in words) or "Myosotis"


def synthesize_mythos(
    prompt: str,
    signals: Mapping[str, float] | None = None,
    *,
    branch_count: int = 3,
) -> MythosBlueprint:
    """Create an actionable mythos blueprint from a prompt and BI metrics.

    Args:
        prompt: Product, story, or user-intent prompt.
        signals: Optional BI values such as engagement, retention, risk, or
            conversion. Positive values strengthen creative branching; negative
            values dampen temperature and increase guidance.
        branch_count: Number of mitosis variants to propose. Values below one
            are promoted to one so the UI always has a visible next step.
    """

    clean_prompt = " ".join(prompt.split()).strip() or "a gentle intelligence garden"
    branch_count = max(1, branch_count)
    raw_signals = signals or {}
    normalized = {
        _slug_to_title(name): MythosSignal(name, float(value)).normalized()
        for name, value in raw_signals.items()
    }

    vitality = sum(normalized.values()) / len(normalized) if normalized else 0.5
    temperature = round(0.35 + 0.45 * vitality, 3)
    resonance_strength = round(0.05 + 0.10 * vitality, 3)
    repetition_penalty = round(1.25 - 0.15 * vitality, 3)

    theme = _slug_to_title(clean_prompt[:48])
    mythos = (
        f"A remember-me-not myth for {clean_prompt}, where insight becomes "
        "careful action and every metric earns a humane explanation."
    )
    mitosis = tuple(
        f"Branch {index + 1}: test a {'bold' if vitality > 0.62 else 'gentle'} variant of {theme}"
        for index in range(branch_count)
    )
    osmosis = tuple(
        f"Absorb {name} at {score:.2f} into narrative pacing"
        for name, score in normalized.items()
    ) or ("Absorb first-session curiosity into narrative pacing",)

    ui_microcopy = (
        "Mythos: turn the user's question into a living story.",
        "Mitosis: split the best idea into measurable variants.",
        "Osmosis: let BI signals tune the model without hiding the reason.",
    )

    return MythosBlueprint(
        theme=theme,
        mythos=mythos,
        mitosis=mitosis,
        osmosis=osmosis,
        ui_microcopy=ui_microcopy,
        model_controls={
            "temperature": temperature,
            "resonance_strength": resonance_strength,
            "repetition_penalty": repetition_penalty,
        },
        bi_summary=normalized,
    )
