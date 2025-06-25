import argparse
from fast_resume.parser import extract_text
from fast_resume.skills import load_skills
from fast_resume.extractor import SkillExtractorTFIDF
from fast_resume.config import DEFAULT_SKILL_FILE, DEFAULT_SIMILARITY_THRESHOLD, DEFAULT_NGRAM_RANGE

def main():
    parser = argparse.ArgumentParser(description="FAST Resume Skill Extractor")
    subparsers = parser.add_subparsers(dest="command")

    extract_parser = subparsers.add_parser("extract", help="Extract skills from resume")
    extract_parser.add_argument("resume", type=str, help="Path to resume file (or use --text instead)")
    extract_parser.add_argument("--skills", type=str, default=DEFAULT_SKILL_FILE, help="Path to skills JSON file")
    extract_parser.add_argument("--ngram", nargs=2, type=int, default=DEFAULT_NGRAM_RANGE, help="Character ngram range (e.g. 3 5)")
    extract_parser.add_argument("--topk", type=int, default=30, help="Max number of top skills to return")
    extract_parser.add_argument("--min", type=float, default=0.1, help="Minimum similarity threshold (0–1)")
    extract_parser.add_argument("--verbose", action="store_true", help="Print skill scores")
    extract_parser.add_argument("--text", type=str, help="Pass resume content directly instead of a file")

    args = parser.parse_args()

    if args.command == "extract":
        # Load text
        if args.text:
            resume_text = args.text
        else:
            resume_text = extract_text(args.resume)

        # Load and normalize skills
        skills = load_skills(args.skills)

        # Extract
        extractor = SkillExtractorTFIDF(skills, ngram_range=tuple(args.ngram))
        results = extractor.extract(resume_text, top_k=args.topk, min_threshold=args.min)

        if args.verbose:
            print("Top Matched Skills:")
            for skill, score in results:
                print(f"- {skill}: {score:.3f}")
        else:
            print(", ".join([skill for skill, _ in results]))

if __name__ == "__main__":
    main()