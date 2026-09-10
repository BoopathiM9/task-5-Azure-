import os
import time
from datetime import datetime, timezone
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="CloudKinetics Enterprise Microservice",
    description="High-performance, containerized REST API with integrated telemetry.",
    version="1.0.0"
)

START_TIME = time.time()

class FeedbackRequest(BaseModel):
    user_id: str = Field(..., example="usr_9981", description="Unique identifier for the user")
    rating: int = Field(..., ge=1, le=5, example=5, description="Rating scale from 1 to 5")
    comments: str = Field(..., example="Flawless deployment!", description="Feedback commentary")

@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CloudKinetics Microservice</title>
        <style>
            :root { --primary: #0078D4; --bg: #0F172A; --card: #1E293B; --text: #F8FAFC; --accent: #10B981; }
            body { font-family: sans-serif; background: var(--bg); color: var(--text); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background: var(--card); border-radius: 12px; padding: 2.5rem; max-width: 500px; border: 1px solid #334155; }
            .status { background: rgba(16, 185, 129, 0.1); color: var(--accent); padding: 0.25rem 0.75rem; border-radius: 9999px; font-weight: 600; }
            h1 { font-size: 1.875rem; margin-top: 1rem; }
            .btn { display: inline-block; background: var(--primary); color: white; text-decoration: none; padding: 0.75rem 1.25rem; border-radius: 6px; font-weight: 600; margin-top: 1rem; }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="status">System Operational</span>
            <h1>Task 5 Microservice</h1>
            <p>Containerized REST API deployed via GitHub Actions CI/CD to Azure Container Apps.</p>
            <a href="/docs" class="btn">View Swagger Docs</a>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health", tags=["Telemetry"])
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "uptime_seconds": round(time.time() - START_TIME, 2)
    }

@app.post("/api/v1/process", status_code=status.HTTP_201_CREATED, tags=["Business Logic"])
def process_data(payload: FeedbackRequest):
    return {
        "status": "success",
        "message": "Feedback processed successfully",
        "data": {
            "user_id": payload.user_id,
            "rating": payload.rating,
            "processed_at": datetime.now(timezone.utc).isoformat()
        }
    }
