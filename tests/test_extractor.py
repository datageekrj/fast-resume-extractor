from fast_resume.extractor import SkillExtractorTFIDF

def test_skill_extraction_basic():
    skills = ["python", "machine learning", "data analysis"]
    resume = "Experienced in Python and machine learnng techniques."

    extractor = SkillExtractorTFIDF(skills)
    matched = extractor.extract(resume, threshold=0.5)

    assert "python" in matched
    assert "machine learning" in matched
    assert "data analysis" not in matched
