from fastapi import FastAPI

app = FastAPI(title="NBA Analytics API")

@app.get("/health")
def health():
    return {"status": "ok"}