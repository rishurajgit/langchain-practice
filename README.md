# 🚀 LangChain Practice 

A modular FastAPI project built to practice and demonstrate core LangChain concepts through multiple real-world APIs.

This project follows a clean architecture where each task is organized into its own module while sharing a common configuration and LLM setup.

---

# 📚 Concepts Covered

- FastAPI
- LangChain Expression Language (LCEL)
- PromptTemplate
- RunnableBranch
- RunnableLambda
- RunnableParallel
- RunnablePassthrough
- Structured Output
- Pydantic Models
- Google Gemini Integration
- Environment Configuration
- Modular API Design

---


---

# ⚙️ Features

## ✅ Health Check API

Simple API to verify the application is running.

**Endpoint**

```
GET /health
```

---

## ✅ Task 1 — Smart Text Toolkit

Transforms text using RunnableBranch.

Supported actions:

- Summarize
- Translate
- Tone Shift

**Endpoint**

```
POST /transform
```

### Concepts

- PromptTemplate
- RunnableBranch
- StrOutputParser

---

## ✅ Task 2 — Resume Parser

Extracts structured information from resume text.

Returns

- Name
- Skills
- Years of Experience
- Last Role

**Endpoint**

```
POST /parse-resume
```

### Concepts

- Structured Output
- Pydantic Models
- PromptTemplate

---

## ✅ Task 3 — Query Router

Classifies user questions into

- Coding
- Math
- General

Routes them to domain-specific prompts.

**Endpoint**

```
POST /ask
```

### Concepts

- RunnableLambda
- RunnableBranch
- LCEL

---

## ✅ Task 4 — Parallel Content Generator

Generates multiple social media contents simultaneously.

Returns

- Tweet
- LinkedIn Caption
- Hashtags

**Endpoint**

```
POST /generate-post
```

### Concepts

- RunnableParallel
- RunnablePassthrough

---

## ✅ Task 5 — Self Correcting Answer API

Creates an answer, reviews it, and improves it if required.


```

**Endpoint**

```
POST /answer
```

### Concepts

- Multi-step Chains
- Prompt Chaining
- Self-Correcting Workflow

---

# 🏗 Architecture

Every module follows the same architecture.

```
Request
   │
   ▼
Router
   │
   ▼
Workflow
   │
   ▼
Prompt
   │
   ▼
Gemini
   │
   ▼
Response
```

This separation keeps the project clean, reusable, and easy to maintain.

---

# 🛠 Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project

```bash
cd langchain-practice
```

Create virtual environment

```bash
uv venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
uv sync
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash
```

---

# ▶️ Run the Application

```bash
uv run uvicorn main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🧠 LangChain Components Used

- PromptTemplate
- RunnableBranch
- RunnableLambda
- RunnableParallel
- RunnablePassthrough
- StrOutputParser
- Structured Output
- LCEL Pipelines

---

# 🧪 APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /health | Health Check |
| POST | /transform | Smart Text Toolkit |
| POST | /parse-resume | Resume Parser |
| POST | /ask | Query Router |
| POST | /generate-post | Parallel Content Generator |
| POST | /answer | Self Correcting Answer |

---

# 📖 Learning Outcomes

This project demonstrates practical implementation of:

- Modular FastAPI Architecture
- LangChain LCEL
- Prompt Engineering
- Structured Output
- Branching Workflows
- Parallel Execution
- Self-Correcting LLM Pipelines
- Reusable Prompt Management
- Environment-based Configuration
- Clean Project Organization

---

# 👨‍💻 Author

**Rishu Raj**

Built as a LangChain Practice Assessment to gain hands-on experience with modern LLM application development using FastAPI and LangChain.