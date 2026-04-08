from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(jd_text, resume_text):
    vectorizer = CountVectorizer().fit_transform([jd_text, resume_text])
    vectors = vectorizer.toarray()

    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(score * 100, 2)