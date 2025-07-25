# 📚 Lisan: AI Tutor for Every Tongue

Lisan is an AI-powered multilingual tutoring platform designed to bridge the language gap in education. With zero-shot learning capabilities, Lisan supports underrepresented regional languages, enabling personalized, interactive learning experiences. It empowers learners to communicate, understand, and get real-time assistance in their native tongue using AI.

---

## ✨ Features
- 🌐 **Zero-Shot Multilingual Support** — Understands and responds in regional languages without prior training data.
- 🧑‍🏫 **AI-Powered Tutoring Assistant** — Interactive Q&A based learning experience.
- 🎙️ **Voice & Text Inputs** — Accepts both speech and text queries.
- 📊 **Knowledge Base Integration** — Fetches information from curated content and documents.
- 🚀 **Real-Time AI Response** — Fast and accurate AI-driven answers.
- 🔗 **Modular Microservices Architecture** — Scalable design for future enhancements.

---

## 🛠️ Tech Stack

| Frontend                  | Backend                     | AI/ML Services               | Database               | Others                     |
|---------------------------|-----------------------------|------------------------------|------------------------|----------------------------|
| HTML, CSS, JavaScript      | FastAPI (Python)             | OpenAI GPT APIs               | MySQL                   | Docker, Git, Postman       |
| Bootstrap (optional UI)    | Python (Pydantic, SQLAlchemy)| Speech-to-Text (Google API)   |                        | VSCode, Uvicorn ASGI Server |

---

## ⚙️ Setup Instructions (Local Development)

### Prerequisites:
- Python 3.10+
- MySQL Database
- Git
- Docker (Optional for containerized deployment)

### Steps:
1. **Clone the Repository**
   ```bash
   git clone https://github.com/fullstackcareeszone/ai-tutor-for-every-tongue.git
   cd ai-tutor-for-every-tongue/lisan-humaira
   ```

2. **Create Virtual Environment & Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # (On Windows: venv\Scripts\activate)
   pip install -r requirements.txt
   ```

3. **Setup MySQL Database**
   - Create a database named `task_manager`.
   - Update database credentials in `db_config.py`:
     ```python
     host="localhost"
     user="root"
     password="your_password"
     database="task_manager"
     ```

4. **Run the FastAPI Server**
   ```bash
   uvicorn main:app --reload
   ```
   - Server will start at: `http://127.0.0.1:8000`
   - API Docs: `http://127.0.0.1:8000/docs`

5. **Frontend Access**
   - Open `index.html` in a browser for basic interaction (optional frontend in `/frontend` folder).

---

## 📂 Project Structure
```
lisan-humaira/
│
├── api/
│   ├── services/
│   │   ├── qa_service.py
│   │   └── db_service.py
│   └── routes/
│       └── api_routes.py
│
├── database/
│   └── db_config.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── main.py              # FastAPI app entry point
├── requirements.txt     # Python dependencies
└── README.md             # Project documentation (you are here)
```

---

## 📝 Usage Instructions
1. Launch the FastAPI server.
2. Open `http://127.0.0.1:8000/docs` to test API endpoints.
3. For frontend testing, open `/frontend/index.html` directly in browser.
4. Input queries via text or voice and receive AI responses.
5. Database operations (e.g., logging questions) are handled in real-time.
6. Speech-to-text feature uses Google API (ensure your key setup).

---

## 🚀 Future Improvements
- Add full-fledged responsive frontend UI.
- Integrate more advanced speech synthesis (Text-to-Speech).
- Expand language models to include dialect-specific nuances.
- Implement user profiles and session-based learning.
- Deploy on cloud with scalable microservices (Kubernetes).
- Add Admin Dashboard for analytics & content curation.

---

## 👩‍💻 Author
Developed by **Humaira Batool**  
- Email: batoolhumaira37@gmail.com  
- University: Fatima Jinnah Women University  
---

## 📜 License
This project is licensed under the MIT License.
