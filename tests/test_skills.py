from fast_resume.skills import normalize_skill

def test_normalize_skill():
    assert normalize_skill("Machine-Learning") == "machine learning"
    assert normalize_skill("  Python  ") == "python"