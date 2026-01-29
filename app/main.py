from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine

app = FastAPI(title="NBA Analytics API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-health")
def db_health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"db" : "ok"}
    