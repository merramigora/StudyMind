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

Additional ideas
- Allow students to upload multiple documents for one course.
- Add a progress dashboard showing quiz performance over time.
- Support exporting flashcards to Anki format.
- Add a confidence score for generated quiz answers.
- Add support for instructor slide decks and lecture transcripts.

That would turn StudyMind into a real RAG-based learning assistant.
