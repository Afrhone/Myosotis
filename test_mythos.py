from myosotis import synthesize_mythos


def test_synthesize_mythos_combines_story_bi_and_controls():
    blueprint = synthesize_mythos(
        "myths for mitosis and osmosis",
        {"engagement": 1.4, "risk": -0.3},
        branch_count=2,
    )

    assert "remember-me-not myth" in blueprint.mythos
    assert len(blueprint.mitosis) == 2
    assert "Engagement" in blueprint.bi_summary
    assert 0.35 <= blueprint.model_controls["temperature"] <= 0.8
    assert "Mitosis branches" in blueprint.prompt_prelude()


def test_synthesize_mythos_keeps_at_least_one_branch():
    blueprint = synthesize_mythos("", branch_count=0)

    assert blueprint.theme == "A Gentle Intelligence Garden"
    assert len(blueprint.mitosis) == 1
    assert blueprint.osmosis == ("Absorb first-session curiosity into narrative pacing",)
