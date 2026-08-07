# StudyMind

StudyMind is an AI-powered study assistant designed to help college students organize lecture notes, PDFs, and class materials into study guides, quizzes, flashcards, and personalized exam preparation plans.

I built this project because, as both a student and a programming tutor, I know how overwhelming it can be to manage information spread across lecture slides, PDFs, handwritten notes, and assignments. My goal was to create a study tool that feels practical for real students rather than just another generic AI chatbot.

---

## Features

- Upload or paste study material
- Generate structured study guides
- Create quiz questions from notes
- Generate flashcards for active recall
- Build personalized exam preparation plans
- Track study progress and weak topics
- Clean and responsive user interface

---

## Why I Built It

Many students already use AI while studying, but most existing tools are designed for general conversations rather than focused learning.

StudyMind is designed specifically for academic workflows by helping students organize information, identify what to review, and prepare for exams in one place.

Building this project also allowed me to strengthen my full-stack development skills while designing an architecture that can later support real AI models, document processing, and retrieval-augmented generation (RAG).

---

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

---

## Current Features

The current version includes a complete demonstration workflow featuring:

- Dashboard
- Study material input
- Study guide generation
- Quiz generation
- Flashcard generation
- Exam preparation planning
- REST API endpoints
- Modular project structure

The application currently uses local rule-based generation so it can run without requiring an external AI API or API key. The architecture is intentionally designed to support future integration with OpenAI or other large language models.

---

## Architecture

```text
React Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
Rule-Based Study Generation
        │
        ▼
Future LLM + RAG Integration
```

StudyMind separates the frontend, backend, and study generation logic to keep the application modular and make future AI integration straightforward.

---

## Planned AI Features

- LLM-powered study guide generation
- AI-generated quizzes
- AI-generated flashcards
- Document question answering
- Retrieval-Augmented Generation (RAG)
- Vector search for uploaded documents

---

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

---

## Running the Project

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the local Vite development server in your browser.

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

---

## API Endpoints

```text
GET  /health
POST /api/study-guide
POST /api/quiz
POST /api/flashcards
POST /api/study-plan
```

---

## Future Improvements

- Support PDF upload and text extraction
- Integrate OpenAI or another LLM provider
- Implement Retrieval-Augmented Generation (RAG)
- Add PostgreSQL database support
- Add user authentication
- Save study history
- Track study streaks
- Deploy the frontend and backend

---

## What I Learned

Building StudyMind strengthened my experience with React, FastAPI, REST APIs, and full-stack application design.

I learned how to separate frontend and backend responsibilities, design modular API endpoints, and build an application architecture that can later support advanced AI features such as document processing and retrieval-augmented generation.

---

## Author

**Merra Migora**

Computer Science Student — University of Washington Tacoma
