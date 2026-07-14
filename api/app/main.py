from fastapi import FastAPI

app = FastAPI(
    title="CloudGPU Advisor API"
)

@app.get("/")
def home():
    return {
        "message":
        "CloudGPU Advisor API Running"
    }