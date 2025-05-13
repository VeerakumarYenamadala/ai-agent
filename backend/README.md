# Personal Assistant Chat App

This backend uses FastAPI + LangGraph to orchestrate three agents:

1. **Workday Agent** (`agent=workday`)  
   - Answers questions about role, goals, and leaves from mock Workday data.

2. **Skill Gap Agent** (`agent=skills`)  
   - Computes missing skills by comparing current vs. goal skills.

3. **Pathway Agent** (`agent=pathway`)  
   - Takes skill gaps and invokes OpenAI to produce a 4-week learning pathway.

---

## 🛠️ Setup

1. **Clone & Install**  
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
