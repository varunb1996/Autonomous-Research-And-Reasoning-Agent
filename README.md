# 🧠 Cognitive Autonomous Multi-Agent Intelligence System

An advanced Agentic AI platform capable of:

- autonomous reasoning
- multi-agent collaboration
- web research
- memory retrieval
- reflection and critique
- self-improving response generation
- persistent vector memory
- autonomous retry loops

This system goes significantly beyond a traditional chatbot or basic RAG pipeline.

---

# 🚀 Features

## ✅ Multi-Agent Architecture

The system includes:

- Supervisor Agent
- Planner Agent
- Research Agent
- Reasoning Agent
- Critic Agent
- Reflection Agent
- Response Agent

---

## ✅ Autonomous Reasoning Workflow

The agents collaboratively:

- plan tasks
- search the web
- retrieve memory
- reason deeply
- critique outputs
- reflect on weaknesses
- improve responses iteratively

---

## ✅ Vector Memory System

Persistent semantic memory using:

- Qdrant Vector Database
- Sentence Transformers Embeddings

Supports:

- long-term memory
- retrieval augmented generation
- semantic search

---

## ✅ Tool Usage

Integrated tools:

- Web Search
- PDF Parsing
- Browser Scraping
- Logging System
- Code Execution
- Memory Retrieval

---

# 🧠 System Architecture

```text
User Goal
    ↓
Supervisor Agent
    ↓
Planner Agent
    ↓
Memory Retrieval
    ↓
Research Agent
    ↓
Reasoning Agent
    ↓
Critic Agent
    ↓
Reflection Agent
    ↓
Autonomous Retry Loop
    ↓
Final Response Agent
    ↓
Memory Storage
    ↓
Streamlit UI
```

---

# 📂 Project Structure

```text
agentic-ai-system/
│
├── app.py
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── .gitignore
│
├── agents/
│   ├── supervisor_agent.py
│   ├── planner_agent.py
│   ├── research_agent.py
│   ├── reasoning_agent.py
│   ├── critic_agent.py
│   ├── reflection_agent.py
│   ├── response_agent.py
│   └── tool_router_agent.py
│
├── tools/
│   ├── llm_tool.py
│   ├── embedding_tool.py
│   ├── retrieval_tool.py
│   ├── memory_tool.py
│   ├── search_tool.py
│   ├── browser_tool.py
│   ├── pdf_tool.py
│   ├── logging_tool.py
│   └── code_execution_tool.py
│
├── workflows/
│   ├── agent_graph.py
│   └── autonomous_loop.py
│
├── memory/
│
├── logs/
│
└── outputs/
```

---

# ⚙️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Groq |
| Agent Framework | LangGraph |
| Vector Database | Qdrant |
| Embeddings | SentenceTransformers |
| UI | Streamlit |
| Web Search | Tavily |
| Language | Python |

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone YOUR_REPO_URL
```

---

## 2. Create Virtual Environment

```bash
py -3.11 -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🌐 Streamlit Deployment

Recommended deployment:

- Streamlit Community Cloud

After deployment:

Add secrets:

```toml
GROQ_API_KEY="your_key"
TAVILY_API_KEY="your_key"
```

inside:

```text
Streamlit Dashboard → Settings → Secrets
```

---

# ⚠️ Groq Rate Limit Issue (IMPORTANT)

Because this is a true multi-agent system, a single query may trigger many LLM calls:

- Supervisor
- Planner
- Reasoning
- Critique
- Reflection
- Retry Loops

This may hit Groq free-tier token limits.

---

## ✅ Recommended Fix

Reduce retry loops.

Inside:

```python
workflows/autonomous_loop.py
```

Change:

```python
for _ in range(3):
```

to:

```python
for _ in range(1):
```

---

## ✅ Reduce Token Usage

Inside:

```python
tools/llm_tool.py
```

Add:

```python
max_tokens=300
```

inside the LLM request.

---

## ✅ Development Mode Recommendation

Temporarily disable:

- reflection loops
- autonomous retries

during debugging to reduce token consumption.

---

# 🧠 What Makes This Agentic AI?

This system:

✅ plans tasks  
✅ uses tools autonomously  
✅ retrieves memory  
✅ critiques responses  
✅ improves outputs iteratively  
✅ performs multi-step reasoning  
✅ stores long-term memory  
✅ orchestrates multiple agents collaboratively

This is much closer to real Agentic AI architectures than standard chatbot systems.

---

# 🚀 Future Upgrades

Potential future improvements:

- Docker deployment
- Kubernetes orchestration
- Redis memory cache
- Browser automation
- Voice interaction
- Autonomous scheduling
- Multi-agent debate systems
- Knowledge graph memory
- LangSmith observability
- Qdrant Cloud deployment
- GPU inference pipelines

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Varun Bukka

AI / ML / Agentic AI / Autonomous Systems
