from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import (
    StudyMaterialRequest,
    StudyPlanRequest,
    StudyGuideResponse,
    QuizResponse,
    FlashcardResponse,
    StudyPlanResponse,
)
from app.services.study_generator import (
    make_summary,
    make_key_points,
    extract_keywords,
    make_quiz_questions,
    make_flashcards,
    make_study_plan,
)

app = FastAPI(
    title="StudyMind API",
    description="Backend API for the StudyMind AI study assistant.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "StudyMind API is running"}


@app.post("/api/study-guide", response_model=StudyGuideResponse)
def create_study_guide(request: StudyMaterialRequest):
    return {
        "title": request.title,
        "summary": make_summary(request.content),
        "key_points": make_key_points(request.content),
        "focus_topics": extract_keywords(request.content, limit=6),
    }


@app.post("/api/quiz", response_model=QuizResponse)
def create_quiz(request: StudyMaterialRequest):
    return {
        "title": f"Quiz for {request.title}",
        "questions": make_quiz_questions(request.content),
    }


@app.post("/api/flashcards", response_model=FlashcardResponse)
def create_flashcards(request: StudyMaterialRequest):
    return {
        "title": f"Flashcards for {request.title}",
        "flashcards": make_flashcards(request.content),
    }


@app.post("/api/study-plan", response_model=StudyPlanResponse)
def create_study_plan(request: StudyPlanRequest):
    return {
        "exam_name": request.exam_name,
        "days_until_exam": request.days_until_exam,
        "plan": make_study_plan(
            request.exam_name,
            request.days_until_exam,
            request.weak_topics,
        ),
    }
