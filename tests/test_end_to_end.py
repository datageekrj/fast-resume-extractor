from fast_resume.extractor import SkillExtractorTFIDF
from fast_resume.parser import extract_text
from fast_resume.skills import load_skills
import os

def test_full_pipeline():
    resume_path = os.path.join(os.path.dirname(__file__), "sample_files", "test_resume.txt")
    skills_path = os.path.join("data", "skills.json")

    resume_text = extract_text(resume_path)
    skills = load_skills(skills_path)

    extractor = SkillExtractorTFIDF(skills)
    matched = extractor.extract(resume_text)

    assert isinstance(matched, list)
    assert any(skill in matched for skill in ["python", "data analysis"])