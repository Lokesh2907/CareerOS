from fastapi import FastAPI

app = FastAPI(
    title="CareerOS",
    description="Autonomous AI Career Assistant",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "application": "CareerOS",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }