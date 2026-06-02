# StudyMind

StudyMind is an AI-powered study assistant for college students. It helps turn lecture notes, PDFs, and class material into study guides, quizzes, flashcards, and exam prep plans.

I built this project because I have been a student and a programming tutor, and I know how easy it is to feel overwhelmed when everything is spread across slides, PDFs, notes, and assignments. I wanted to make something that feels useful for real studying, not just another basic chatbot.

## What the app does

- Upload or paste study material
- Generate a simple study guide
- Create quiz questions from notes
- Build flashcards for review
- Make a short exam plan based on how many days are left
- Show study progress and weak topics
- Keep the design clean and easy to use

## Why I built it

A lot of students already use AI, but most tools feel too general. StudyMind is focused on studying. The idea is to help students understand what to review, practice active recall, and organize exam prep in one place.

This project also gave me a chance to practice full-stack development and AI application design using a frontend, backend API, and a structure that can later support real document search and retrieval.

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn

### Planned AI Features
- LLM-generated summaries
- Quiz generation
- Flashcard generation
- Document Q&A
- RAG/vector search for uploaded notes

## Current Features

This version includes a working demo flow:

- Dashboard
- Study material input
- Study guide generator
- Quiz generator
- Flashcard generator
- Exam plan generator
- Backend API endpoints
- Clean project structure

The backend currently uses local rule-based generation so the project can run without requiring an API key. The project is designed so an OpenAI API or another LLM provider can be added later.

## Project Structure

```text
StudyMind/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── README.md
│
├── database/
│   └── schema.sql
│
├── docs/
│   └── project-notes.md
│
└── README.md
```

## How to Run the Frontend

```bash
cd frontend
npm install
npm run dev
```

Then open the local Vite link in your browser.

## How to Run the Backend

Open another terminal:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

## API Endpoints

```text
GET  /health
POST /api/study-guide
POST /api/quiz
POST /api/flashcards
POST /api/study-plan
```

## Future Improvements

- Add real PDF upload and text extraction
- Add embeddings and vector search
- Add user accounts
- Save quiz history
- Track study streaks
- Add PostgreSQL integration
- Deploy frontend and backend

## Resume Bullet

Built StudyMind, an AI-powered study assistant using React and FastAPI that turns study material into study guides, quizzes, flashcards, and exam prep plans, with a backend structure designed for future LLM and RAG integration.

## Author

Merra Migora
