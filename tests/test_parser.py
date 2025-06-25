from fast_resume.parser import extract_text
import os

def test_extract_txt():
    text_path = os.path.join(os.path.dirname(__file__), "sample_files", "test_resume.txt")
    text = extract_text(text_path)
    assert "python" in text.lower()