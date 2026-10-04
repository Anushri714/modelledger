from fastapi import FastAPI

app = FastAPI(title="ModelLedger API")


@app.get("/")
def home():
    return {"message": "ModelLedger is running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}
