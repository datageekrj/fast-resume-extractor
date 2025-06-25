from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SkillExtractorTFIDF:
    """
    Extract skills from resume text using TF-IDF with character n-grams.
    """

    def __init__(self, skills_list, ngram_range=(3, 5)):
        """
        Initialize the extractor.

        :param skills_list: List of skill phrases (strings)
        :param ngram_range: Tuple indicating n-gram range (default: (3, 5))
        """
        self.skills_list = [s.lower().strip() for s in skills_list]
        self.vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=ngram_range)
        self.skills_matrix = self.vectorizer.fit_transform(self.skills_list)

    # def extract(self, resume_text, threshold=0.6):
    #     """
    #     Extract matched skills from resume text.

    #     :param resume_text: Raw resume text (string)
    #     :param threshold: Cosine similarity threshold (0–1)
    #     :return: List of matched skill strings
    #     """
    #     resume_text = resume_text.lower().strip()
    #     resume_vector = self.vectorizer.transform([resume_text])
    #     similarity_scores = cosine_similarity(resume_vector, self.skills_matrix).flatten()

    #     matched = [
    #         self.skills_list[i]
    #         for i, score in enumerate(similarity_scores)
    #         if score >= threshold
    #     ]
    #     return matched
    def extract(self, resume_text, top_k=30, min_threshold=0.1):
        """
        Extract top K matched skills from resume text using similarity.

        :param resume_text: Raw resume text (string)
        :param top_k: Max number of top skills to return
        :param min_threshold: Minimum cosine similarity to include
        :return: List of (skill, score) tuples
        """
        resume_text = resume_text.lower().strip()
        resume_vector = self.vectorizer.transform([resume_text])
        similarity_scores = cosine_similarity(resume_vector, self.skills_matrix).flatten()

        # Create list of (skill, score) and filter
        scored_skills = [
            (self.skills_list[i], score)
            for i, score in enumerate(similarity_scores)
            if score >= min_threshold
        ]

        # Sort by score descending
        scored_skills.sort(key=lambda x: x[1], reverse=True)

        return scored_skills[:top_k]