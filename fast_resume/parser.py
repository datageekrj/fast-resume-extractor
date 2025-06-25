import os

def extract_text(filepath):
    """
    Extract raw text from a resume file (.pdf, .docx, .txt).

    :param filepath: Path to the resume file
    :return: Extracted text as string
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    ext = os.path.splitext(filepath)[-1].lower()

    if ext == ".pdf":
        return _extract_pdf(filepath)
    elif ext == ".docx":
        return _extract_docx(filepath)
    elif ext == ".txt":
        return _extract_txt(filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def _extract_pdf(filepath):
    from pdfminer.high_level import extract_text as pdf_extract
    return pdf_extract(filepath)


def _extract_docx(filepath):
    from docx import Document
    doc = Document(filepath)
    return "\n".join(p.text for p in doc.paragraphs)


def _extract_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()