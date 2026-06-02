from pydantic import BaseModel, Field
from typing import List


class StudyMaterialRequest(BaseModel):
    title: str = Field(default="Untitled Notes")
    content: str = Field(min_length=20)


class StudyPlanRequest(BaseModel):
    exam_name: str = Field(default="Upcoming Exam")
    days_until_exam: int = Field(ge=1, le=30)
    weak_topics: List[str] = Field(default_factory=list)


class StudyGuideResponse(BaseModel):
    title: str
    summary: str
    key_points: List[str]
    focus_topics: List[str]


class QuizQuestion(BaseModel):
    question: str
    answer: str
    type: str = "short_answer"


class QuizResponse(BaseModel):
    title: str
    questions: List[QuizQuestion]


class Flashcard(BaseModel):
    front: str
    back: str


class FlashcardResponse(BaseModel):
    title: str
    flashcards: List[Flashcard]


class StudyPlanResponse(BaseModel):
    exam_name: str
    days_until_exam: int
    plan: List[str]
