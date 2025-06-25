import json
import os


def load_skills(filepath):
    """
    Load and normalize skills from a JSON or TXT file.

    :param filepath: Path to skills file
    :return: List of cleaned skill strings
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Skill file not found: {filepath}")

    _, ext = os.path.splitext(filepath)
    skills = []

    if ext == '.json':
        with open(filepath, 'r', encoding='utf-8') as f:
            skills = json.load(f)
    elif ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            skills = [line.strip() for line in f if line.strip()]
    else:
        raise ValueError("Unsupported skill file type. Use .json or .txt")

    # Normalize
    return [normalize_skill(s) for s in skills]


def normalize_skill(skill):
    """
    Normalize a skill phrase (lowercase, strip, remove dashes).

    :param skill: Raw skill string
    :return: Normalized skill
    """
    return skill.lower().strip().replace('-', ' ')
