# 📚 AI-Powered Book Summarizer & Personal Advisor

An AI-powered platform that transforms your bookshelf into a personal knowledge assistant. Built using **FastAPI**, **PostgreSQL**, and **LLM APIs**, this project allows users to store books, generate AI-based summaries, and receive context-aware advice based on the wisdom of their personal book collection.

---

## 🔥 Key Features (MVP: Aug 13–20)

### ✅ 1. Add Books to Personal Shelf
- Users can input book names and authors.
- The system fetches AI-generated summaries using LLM APIs (e.g., OpenRouter, Together, Groq, or OpenAI).
- Summaries are stored and linked to the user's personal bookshelf.

### ✅ 2. View Your Book Shelf
- Authenticated users can view their saved books and AI-generated summaries.
- Books are organized and persisted in a PostgreSQL database.

### ✅ 3. Authentication
- Secure login/signup flow with JWT tokens.
- User-specific bookshelf and data isolation.

### ✅ 4. Clean Backend Architecture
- Modular FastAPI app with routes, schemas, models, services.
- Alembic for database migrations.
- Dockerized for easy deployment.

---

## 🧠 Coming Soon: Book-Based Personal Advisor (Post-Aug 20)

### 💡 Situation-Based Wisdom Engine
- Ask real-life questions (e.g., "How do I stay focused under pressure?")
- The system fetches advice from multiple books in your shelf and summarizes them via LLMs.
- Provides multiple perspectives (like an intelligent advisor).

### 📚 Smart Book Recommendations
- Recommends new books based on your current shelf and advice gaps.
- Suggests readings for personal growth across areas like mindset, decision-making, leadership, etc.

### 🧠 Vector-Based Knowledge Retrieval (Optional)
- Stores summaries in a vector database (e.g., ChromaDB).
- Uses embeddings to semantically match advice to questions.

---

## 🛠️ Tech Stack

| Layer          | Technology                            |
|----------------|----------------------------------------|
| Backend API    | FastAPI + Pydantic                     |
| Auth           | JWT (Access + Refresh Tokens)          |
| Database       | PostgreSQL + SQLAlchemy + Alembic      |
| AI Integration | LLM APIs (OpenRouter / Together / Groq)|
| DevOps         | Docker + Docker Compose                |
| Deployment     | Render / Railway / Fly.io (WIP)        |

---

## 📁 Folder Structure (Planned)

