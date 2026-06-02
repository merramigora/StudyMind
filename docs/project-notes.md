# Project Notes

StudyMind is meant to feel like something I would actually use as a student.

The main problem I wanted to solve:
- Students have too many PDFs, lecture slides, notes, and assignments.
- It is hard to know what to study first.
- Reading notes is not enough; students need active recall and practice.

The first version keeps the AI part simple so the app can run locally without paid API keys.
Later, the AI service can be connected to OpenAI or another model.

Important future technical upgrade:
- Extract text from PDFs
- Split text into chunks
- Create embeddings
- Store them in a vector database
- Use retrieval before generating answers

That would turn StudyMind into a real RAG-based learning assistant.
