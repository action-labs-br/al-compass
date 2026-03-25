# Technical Challenge — AI/ML Engineer

## Scenario

**Sentinel** is a road safety platform that supports emergency dispatch on Brazilian federal highways. Sentinel's core feature is a fatality risk model that estimates the probability of a fatal outcome based on the information available in the initial accident report, helping dispatch teams prioritize response and allocate resources.

The engineering team needs you to build the backend: a classification endpoint for fatality risk, exposed via API.

> **Note:** This dataset represents Brazilian federal highway accident records and is used purely as a technical exercise. We value depth over breadth — a well-engineered ML pipeline with clear EDA matters more than implementing every feature.

---

## About the data

The dataset contains **~60,000 accident records** from Brazilian federal highways. The prediction target is **`is_fatal`** — a boolean indicating whether the accident resulted in at least one death. Features include temporal, geographic, road condition, and accident detail columns. See `data/data_dictionary.md` for the full column reference.

Not all dataset columns are available as API inputs — check `app/models.py` for the request contract. Start with an EDA. Understand the features and their relationships with the target. Document your feature selection decisions in the notebook.

---

## What you need to build

### Required: `POST /predict`

Predict whether an accident is likely to be fatal based on its circumstances.

**Request:**
```json
{
  "highway": "BR-116",
  "km_marker": 402.5,
  "state": "MG",
  "municipality": "Governador Valadares",
  "accident_cause": "Falta de atenção",
  "accident_type": "Colisão traseira",
  "day_of_week": "Segunda",
  "hour": 18,
  "vehicles_involved": 2
}
```

The API may receive additional optional fields from the dataset. Your endpoint should accept them gracefully.

**Response:**
```json
{
  "is_fatal": false,
  "fatality_probability": 0.12
}
```

### Bonus: `POST /chat`

Natural language question → agent response. The agent decides between searching documents (RAG) or querying the prediction model (tool calling). **Implement this after the prediction pipeline is solid.**

**Example:**
```json
// Request
{"message": "What are the most common causes of fatal accidents on BR-116?"}

// Response
{
  "response": "The most common causes include speeding and driver inattention...",
  "sources": ["highway_risk_profiles.md", "accident_causes.md"],
  "tools_used": ["search_documents"]
}
```

Schemas are in `app/models.py`. The `/health` endpoint is already done.

---

## Deliverables

1. **Working API** — `docker compose up` starts the application on port 8000 with `/health` and `/predict` functional
2. **EDA notebook** — `notebooks/exploration.ipynb` showing your data exploration, feature engineering, model selection, and evaluation
3. **Bonus:** `/chat` endpoint with RAG and tool-calling

You design the module structure. The only contract is the API schemas in `app/models.py` and the endpoint paths in `app/main.py`.

---

## Provided files

You may add files and dependencies, but keep the existing API schemas — the interface is the contract.

| File | Description |
|------|-------------|
| `app/main.py` | FastAPI endpoints — `/health` (done), `/predict` and `/chat` (to implement) |
| `app/models.py` | Pydantic request/response schemas |
| `app/config.py` | Environment variables (API key, model name) |
| `data/accidents.csv` | ~60,000 accident records from Brazilian federal highways |
| `data/data_dictionary.md` | Column descriptions and metadata |
| `notebooks/exploration.ipynb` | Starter notebook for EDA and model development |
| `data/docs/` | 7 markdown documents — knowledge base for the chat agent (bonus) |
| `Dockerfile` | Docker configuration |
| `docker-compose.yml` | Docker Compose configuration |
| `requirements.txt` | Python dependencies |

---

## Technical requirements

- **Python 3.11+**
- **FastAPI** for the API
- **Docker** — `docker compose up` must start the entire application on port **8000**
- **ML framework**: free choice (scikit-learn, XGBoost, LightGBM, etc.)
- **For the bonus chat endpoint:** LLM via [OpenRouter](https://openrouter.ai) (free tier available), RAG framework of your choice

---

## Getting started

1. **Download the contents** of this repository and create a new public repository on GitHub
2. **Set up the environment** — copy `.env.example` to `.env` and fill in your API key (needed for the bonus chat endpoint):
   ```bash
   cp .env.example .env
   ```
3. **Explore the data** — start with the notebook, understand what you're working with
4. **Implement the prediction pipeline** — design your own module structure in `app/`
5. **Make sure Docker works** — `docker compose up` must start the complete application
6. **Test the endpoints** — `/health` and `/predict` (required), `/chat` (bonus)

---

## A note on tools

You may use any tools you normally use when working — including AI assistants, code generators, and documentation tools. We evaluate your engineering judgment, not your typing speed.

Be prepared to walk through your solution, explain your decisions, and extend your work in a follow-up conversation.

---

## What we evaluate

We use a combination of automated tests and manual code review.

**Automated (run against your API):**
- API contract compliance — schemas, validation, error handling
- Prediction quality — classification performance on a holdout set (AUC)
- Prediction sanity — do results reflect real-world expectations?

**Manual code review:**
- ML pipeline — feature engineering, model selection, evaluation methodology, and the reasoning behind your decisions
- EDA notebook — genuine analysis, not just code. Show the trade-offs you considered and the decisions you made
- Code quality — architecture, error handling, clean structure
- Bonus: RAG implementation, tool orchestration, prompt engineering

We value clear thinking and justified decisions over model complexity. A simple model with well-reasoned feature selection will score higher than a complex model that uses every column without questioning it.

This challenge is designed to be completed in **~4-6 hours**. Focus on a solid core pipeline rather than trying to implement everything.

No hosting required. Publish to a public GitHub repository and share the link.
