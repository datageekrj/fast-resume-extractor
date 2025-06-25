import os
import argparse
from fast_resume.parser import extract_text
from fast_resume.extractor import SkillExtractorTFIDF
from fast_resume.skills import load_skills
from fast_resume.config import DEFAULT_SKILL_FILE

def process_directory(folder_path, skills_path, top_k=30, min_threshold=0.1):
    skills = load_skills(skills_path)
    extractor = SkillExtractorTFIDF(skills)

    results = {}

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(('.pdf', '.docx', '.txt')):
            continue

        file_path = os.path.join(folder_path, filename)
        try:
            resume_text = extract_text(file_path)
            matches = extractor.extract(resume_text, top_k=top_k, min_threshold=min_threshold)
            results[filename] = matches
        except Exception as e:
            print(f"[!] Failed to process {filename}: {e}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Resume Skill Extractor")
    parser.add_argument("folder", type=str, help="Path to folder with resume files")
    parser.add_argument("--skills", type=str, default=DEFAULT_SKILL_FILE, help="Path to skills JSON")
    parser.add_argument("--topk", type=int, default=30, help="Top K skills to return per resume")
    parser.add_argument("--min", type=float, default=0.1, help="Minimum similarity threshold")

    args = parser.parse_args()

    result = process_directory(args.folder, args.skills, args.topk, args.min)

    for fname, matched in result.items():
        print(f"\n{fname}")
        print("-" * len(fname))
        for skill, score in matched:
            print(f"{skill:30} {score:.3f}")