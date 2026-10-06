from fastapi import FastAPI
from app.api.alerts import router as alerts_router
from app.api.incidents import router as incidents_router

app = FastAPI(
    title="Agentic SOC - Investigation Platform",
    description="Autonomous Agentic Security Operations Center Investigation API",
    version="1.0.0",
)

app.include_router(alerts_router)
app.include_router(incidents_router)


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint to verify API readiness."""
    return {"status": "healthy"}
