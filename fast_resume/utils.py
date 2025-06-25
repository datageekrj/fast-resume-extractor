import re

def clean_text(text):
    """
    Lowercase and remove special characters/punctuation.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text