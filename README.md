# text-to-query
A project to create a text to mongodb query using Langchain.

## Running Locally

**1. Clone Repo**

```bash
git clone https://github.com/jorgegperez/text-to-query.git
```

**2.1 Run using Docker**

```bash
docker compose build
docker compose up
```
To visit the FastAPI documentation of the resulting service, visit http://localhost:8000/docs with a web browser.
To visit the streamlit UI, visit http://localhost:8501.

**2.2 Run locally**

```bash
source venv/bin/activate
```

**2.2.1 Streamlit Client**

```bash
cd apps/client
pip install -r requirements.txt
streamlit run app.py
```

**2.2.2 FastAPI**

```bash
cd apps/api
pip install -r requirements.txt
uvicorn app:app
```