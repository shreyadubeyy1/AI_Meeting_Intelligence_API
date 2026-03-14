# 🚀 AI Meeting Intelligence API

AI Meeting Intelligence API is a backend service that analyzes meeting transcripts using Large Language Models (LLMs) and converts unstructured conversations into structured insights such as summaries, action items, decisions, and deadlines.

The project demonstrates how modern backend systems combine **FastAPI, JWT authentication, PostgreSQL, and AI APIs** to build intelligent automation services.

It is designed with a **modular architecture**, containerized using **Docker**, and built to be easily deployable on cloud platforms.

---

## 📌 Problem Statement

Meetings often generate long transcripts that are difficult to review later. Important information such as key decisions, action items, and deadlines can easily get lost.

This project solves that problem by automatically analyzing meeting transcripts using AI and converting them into structured insights that teams can quickly understand and act upon.

---

## ⚙️ How the System Works

1. User registers and logs into the system
2. A meeting transcript is submitted through the API
3. The backend sends the transcript to an LLM service
4. The AI extracts:
   - Meeting summary
   - Action items
   - Key decisions
   - Deadlines
5. The processed insights are returned via the API and can optionally be stored in the database

---

## 🧱 Features

- 🔐 **User Authentication** – Secure JWT-based login and registration
- 🤖 **AI Meeting Analysis** – Extract summaries, decisions, and action items from transcripts
- 🗂 **Meeting Management** – Store and manage meeting records
- 📊 **Structured AI Output** – Convert unstructured text into actionable insights
- 🧠 **LLM Integration** – Supports OpenAI or other LLM APIs
- 🐳 **Dockerized Deployment** – Run the project inside containers
- ☁ **Cloud Ready** – Deployable on AWS or other cloud providers
- 📦 **Modular Architecture** – Clean scalable backend structure

---

## 🗂 Project Structure
```
AI-Meeting-Intelligence/
│
├── app/
│   ├── api/            # API route definitions
│   ├── core/           # Core configurations (database, security, settings)
│   ├── models/         # Database models and Pydantic schemas
│   ├── services/       # Business logic and AI services
│   ├── utils/          # Helper utilities
│   └── main.py         # FastAPI application entry point
│
├── tests/              # Unit and integration tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## 🧰 Tech Stack

| Layer             | Technology           |
| ----------------- | -------------------- |
| Backend Framework | FastAPI              |
| Language          | Python               |
| Database          | PostgreSQL           |
| ORM               | SQLAlchemy           |
| Authentication    | JWT                  |
| AI Integration    | OpenAI / LLM APIs    |
| Containerization  | Docker               |
| Cloud Deployment  | AWS (EC2 / ECS / S3) |
| Configuration     | python-dotenv        |
| CI/CD (optional)  | GitHub Actions       |

---

## 🔌 API Endpoints

### Authentication

**Register User**
```
POST /auth/register
```

Request body:
```json
{
  "email": "user@example.com",
  "password": "1234"
}
```

**Login User**
```
POST /auth/login
```

Response:
```json
{
  "access_token": "JWT_TOKEN"
}
```

---

### AI Meeting Intelligence

**Analyze Meeting Transcript**
```
POST /api/v1/meeting/analyze
```

Request:
```json
{
  "transcript": "We discussed launching the product next month. Shreya will handle backend development."
}
```

Response:
```json
{
  "summary": "The team discussed launching the product next month.",
  "action_items": [
    "Shreya will handle backend development"
  ],
  "decisions": [
    "Product launch planned for next month"
  ]
}
```

---

## 🧪 Running the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ai-meeting-intelligence-api.git
cd ai-meeting-intelligence-api
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
```

Activate it:
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/meeting_ai_db
OPENAI_API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

### 5️⃣ Run the API
```bash
uvicorn app.main:app --reload
```

Open API documentation:
```
http://127.0.0.1:8000/docs
```

---

## 🐳 Running with Docker

Build the image:
```bash
docker build -t ai-meeting-intelligence .
```

Run the container:
```bash
docker run -p 8000:8000 ai-meeting-intelligence
```

---

## ☁ Deployment

This project can be deployed using:

- AWS EC2
- AWS ECS
- Docker containers
- Cloud platforms like Render or Railway

Docker images can also be published using **GitHub Container Registry** with CI/CD.

---

## 🔮 Future Improvements

- Role-based authentication and authorization
- Real-time meeting transcription integration
- Support for multiple AI models
- Meeting search and analytics dashboard
- Logging and monitoring for production
- Automatic AI summarization pipelines

---

---

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Docker Documentation](https://docs.docker.com/)

---

## 📄 License

MIT License — free to use and modify.
