# StudyMind Backend

This backend uses FastAPI and currently provides local demo generation for study guides, quizzes, flashcards, and study plans.

Run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

The `/docs` page shows the API automatically.
