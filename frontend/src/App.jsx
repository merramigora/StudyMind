import { useMemo, useState } from 'react'
import { BookOpen, Brain, CheckCircle2, ClipboardList, Layers, Sparkles } from 'lucide-react'
import { sampleNotes } from './data/sampleNotes'

const API_BASE = 'http://127.0.0.1:8000'

function App() {
  const [title, setTitle] = useState('AVL Trees Review')
  const [content, setContent] = useState(sampleNotes)
  const [examName, setExamName] = useState('Algorithms Exam')
  const [days, setDays] = useState(5)
  const [weakTopics, setWeakTopics] = useState('AVL rotations, tree height, balance factor')
  const [result, setResult] = useState(null)
  const [activeTool, setActiveTool] = useState('study-guide')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const stats = useMemo(() => {
    const words = content.trim().split(/\s+/).filter(Boolean).length
    const minutes = Math.max(1, Math.ceil(words / 180))
    return { words, minutes }
  }, [content])

  async function postJson(path, body) {
    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch(`${API_BASE}${path}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      })

      if (!response.ok) {
        throw new Error('The backend did not return a successful response.')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError('I could not reach the backend. Make sure FastAPI is running on http://127.0.0.1:8000.')
    } finally {
      setLoading(false)
    }
  }

  function handleGenerate(tool) {
    setActiveTool(tool)

    if (tool === 'study-guide') {
      postJson('/api/study-guide', { title, content })
    }

    if (tool === 'quiz') {
      postJson('/api/quiz', { title, content })
    }

    if (tool === 'flashcards') {
      postJson('/api/flashcards', { title, content })
    }

    if (tool === 'study-plan') {
      const topics = weakTopics
        .split(',')
        .map((topic) => topic.trim())
        .filter(Boolean)

      postJson('/api/study-plan', {
        exam_name: examName,
        days_until_exam: Number(days),
        weak_topics: topics,
      })
    }
  }

  return (
    <main className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">AI study assistant</p>
          <h1>StudyMind</h1>
          <p className="heroText">
            Turn class notes into study guides, quizzes, flashcards, and exam plans.
            I wanted this to feel like a tool a busy student would actually use.
          </p>
          <div className="heroActions">
            <button onClick={() => handleGenerate('study-guide')}>
              <Sparkles size={18} /> Generate study guide
            </button>
            <button className="secondary" onClick={() => setContent(sampleNotes)}>
              Use sample notes
            </button>
          </div>
        </div>

        <div className="heroCard">
          <div className="metric">
            <span>{stats.words}</span>
            <p>words added</p>
          </div>
          <div className="metric">
            <span>{stats.minutes}</span>
            <p>min read</p>
          </div>
          <div className="metric">
            <span>4</span>
            <p>study tools</p>
          </div>
        </div>
      </section>

      <section className="grid">
        <div className="panel inputPanel">
          <div className="panelHeader">
            <BookOpen />
            <div>
              <h2>Study material</h2>
              <p>Paste notes, a lecture summary, or text from a PDF.</p>
            </div>
          </div>

          <label>
            Title
            <input value={title} onChange={(event) => setTitle(event.target.value)} />
          </label>

          <label>
            Notes
            <textarea value={content} onChange={(event) => setContent(event.target.value)} />
          </label>

          <div className="toolGrid">
            <button onClick={() => handleGenerate('study-guide')}>
              <Brain size={18} /> Study Guide
            </button>
            <button onClick={() => handleGenerate('quiz')}>
              <ClipboardList size={18} /> Quiz
            </button>
            <button onClick={() => handleGenerate('flashcards')}>
              <Layers size={18} /> Flashcards
            </button>
            <button onClick={() => handleGenerate('study-plan')}>
              <CheckCircle2 size={18} /> Study Plan
            </button>
          </div>

          <div className="miniForm">
            <label>
              Exam
              <input value={examName} onChange={(event) => setExamName(event.target.value)} />
            </label>
            <label>
              Days left
              <input
                type="number"
                min="1"
                max="30"
                value={days}
                onChange={(event) => setDays(event.target.value)}
              />
            </label>
          </div>

          <label>
            Weak topics
            <input value={weakTopics} onChange={(event) => setWeakTopics(event.target.value)} />
          </label>
        </div>

        <div className="panel resultPanel">
          <div className="panelHeader">
            <Sparkles />
            <div>
              <h2>Generated output</h2>
              <p>Results from the StudyMind backend.</p>
            </div>
          </div>

          {loading && <div className="empty">Generating...</div>}
          {error && <div className="error">{error}</div>}
          {!loading && !error && !result && (
            <div className="empty">
              Choose one of the tools to generate a study output.
            </div>
          )}

          {result && activeTool === 'study-guide' && (
            <div className="output">
              <h3>{result.title}</h3>
              <p>{result.summary}</p>
              <h4>Key points</h4>
              <ul>{result.key_points.map((item, index) => <li key={index}>{item}</li>)}</ul>
              <h4>Focus topics</h4>
              <div className="chips">
                {result.focus_topics.map((topic) => <span key={topic}>{topic}</span>)}
              </div>
            </div>
          )}

          {result && activeTool === 'quiz' && (
            <div className="output">
              <h3>{result.title}</h3>
              {result.questions.map((question, index) => (
                <article className="question" key={index}>
                  <strong>{index + 1}. {question.question}</strong>
                  <p>{question.answer}</p>
                </article>
              ))}
            </div>
          )}

          {result && activeTool === 'flashcards' && (
            <div className="flashcards">
              {result.flashcards.map((card, index) => (
                <article className="flashcard" key={index}>
                  <h4>{card.front}</h4>
                  <p>{card.back}</p>
                </article>
              ))}
            </div>
          )}

          {result && activeTool === 'study-plan' && (
            <div className="output">
              <h3>{result.exam_name}</h3>
              <p>{result.days_until_exam} day plan</p>
              <ol>{result.plan.map((day, index) => <li key={index}>{day}</li>)}</ol>
            </div>
          )}
        </div>
      </section>
    </main>
  )
}

export default App
