import re
from typing import List


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> List[str]:
    text = clean_text(text)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in sentences if len(s.strip()) > 20]

# Extracts frequently used terms from study material.
# This is intentionally simple for the first version so the
# project can run locally without external AI services.
# Later this can be replaced with embeddings or NLP models.
def extract_keywords(text: str, limit: int = 6) -> List[str]:
    stop_words = {
        "the", "and", "for", "with", "this", "that", "from", "are", "was",
        "were", "have", "has", "you", "your", "into", "about", "when",
        "then", "than", "they", "their", "there", "because", "which",
        "using", "used", "can", "will", "also", "not", "but"
    }

    words = re.findall(r"[A-Za-z][A-Za-z\-]{3,}", text.lower())
    counts = {}

    for word in words:
        if word not in stop_words:
            counts[word] = counts.get(word, 0) + 1

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [word.title() for word, _ in ranked[:limit]]


def make_summary(text: str) -> str:
    sentences = split_sentences(text)
    if not sentences:
        return "These notes cover several related topics. Focus on the main definitions, examples, and any steps that repeat."
    return " ".join(sentences[:3])


def make_key_points(text: str) -> List[str]:
    sentences = split_sentences(text)
    if len(sentences) >= 5:
        return sentences[:5]

    keywords = extract_keywords(text)
    return [f"Review the main idea behind {keyword}." for keyword in keywords[:5]]

# Generates review questions from important concepts found
# in the notes. The goal is to encourage active recall
# rather than simply rereading material.
def make_quiz_questions(text: str) -> List[dict]:
    keywords = extract_keywords(text, limit=5)
    if not keywords:
        keywords = ["the main concept", "the key process", "the important example"]

    questions = []
    for keyword in keywords:
        questions.append({
            "question": f"Explain {keyword} in your own words.",
            "answer": f"A strong answer should define {keyword}, explain why it matters, and connect it to an example from the notes.",
            "type": "short_answer"
        })

    questions.append({
        "question": "What is one topic from these notes that would be easy to confuse on an exam?",
        "answer": "Look for concepts that have similar definitions, formulas, or steps. Compare them side by side.",
        "type": "reflection"
    })

    return questions


def make_flashcards(text: str) -> List[dict]:
    keywords = extract_keywords(text, limit=6)
    if not keywords:
        keywords = ["Main concept", "Important definition", "Exam example"]

    return [
        {
            "front": f"What should I remember about {keyword}?",
            "back": f"Review the definition, purpose, and one example of {keyword}."
        }
        for keyword in keywords
    ]


def make_study_plan(exam_name: str, days: int, weak_topics: List[str]) -> List[str]:
    topics = weak_topics if weak_topics else ["main concepts", "practice problems", "old notes", "quiz review"]

    plan = []
    for day in range(1, days + 1):
        topic = topics[(day - 1) % len(topics)]
        if day == days:
            plan.append(f"Day {day}: Final review for {exam_name}. Redo missed questions and keep the review lighter.")
        elif day % 3 == 0:
            plan.append(f"Day {day}: Practice active recall on {topic}. Try answering without looking at notes first.")
        else:
            plan.append(f"Day {day}: Review {topic}, make quick notes, and create 3-5 practice questions.")

    return plan
