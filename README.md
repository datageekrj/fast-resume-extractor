
# 🚀 FAST Resume Skill Extractor

**FAST** stands for:
> **F**ast, **A**ccurate, **S**imple, **T**uned

A blazing-fast, accurate, and fully local resume/CV skill extractor powered by character-level TF-IDF matching. No APIs, no rate limits — ideal for batch processing thousands of resumes.

---

## 🌟 Features

- ✅ Extracts **single and multi-word skills**
- ✅ Handles **spelling variations and typos** using char n-grams
- ✅ Fully local — no API calls or internet required
- ✅ Works with `.pdf`, `.docx`, and `.txt` resumes
- ✅ Easy-to-use CLI and Python API
- ✅ Scalable to thousands of resumes (batch mode)

---

## 🛠 Installation

```bash
git clone https://github.com/YOUR_USERNAME/fast-resume-extractor.git
cd fast-resume-extractor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
````

---

## 📦 Project Structure

```
fast_resume/       # Main package (parser, extractor, skill loader)
data/              # skills.json file
cli/               # Command-line interface
examples/          # Example scripts (e.g., batch processing)
tests/             # Unit tests
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 🚀 CLI Usage

```bash
python cli/main.py extract path/to/resume.pdf --skills data/skills.json --verbose
```

### Optional Flags:

* `--topk 30` → Return top 30 matched skills
* `--min 0.1` → Minimum similarity threshold
* `--ngram 3 5` → N-gram character range
* `--text "raw resume string"` → Extract from text instead of file

---

## 🗂️ Batch Processing (Directory of Resumes)

```bash
python examples/batch_extract.py resumes/ --skills data/skills.json --topk 20 --min 0.1
```

---

## 🧠 How It Works

* Loads resume text
* Loads a curated `skills.json` list
* Uses character n-gram TF-IDF to compare resume vs skills
* Returns top matches sorted by cosine similarity

---

## 📄 Sample `skills.json`

```json
[
  "python", "machine learning", "data analysis",
  "communication", "sql", "excel"
]
```

---

## 🧠 Future Ideas

* [ ] Group skills by category
* [ ] Save output as CSV/JSON
* [ ] Add fuzzy logic + aliases (e.g., "ml" → "machine learning")
* [ ] Web UI

---

## 🧑‍💻 Author

**\[Your Name]**
\[Your GitHub Profile]
Feel free to contribute, fork, or suggest improvements!

---

## 📜 License

MIT License

````

---

## ✅ PART 2: Push to GitHub (Step-by-Step)

---

### 🧱 Step 1: Initialize Git

```bash
cd FAST_SKILL_EXTRACTOR
git init
git add .
git commit -m "Initial commit: FAST resume skill extractor"
````