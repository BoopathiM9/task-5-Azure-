from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time

app = FastAPI(
    title="CloudKinetics Enterprise Microservice",
    description="Production-grade FastAPI service running on Azure Container Apps.",
    version="1.0.0"
)

START_TIME = time.time()

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CloudKinetics Enterprise Dashboard</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            :root {
                --bg-gradient: linear-gradient(-45deg, #0f172a, #1e1b4b, #0f2027, #203a43);
                --card-bg: rgba(15, 23, 42, 0.75);
                --accent-cyan: #38bdf8;
                --accent-green: #22c55e;
                --accent-purple: #a855f7;
                --text-main: #f8fafc;
            }

            * { box-sizing: border-box; margin: 0; padding: 0; }

            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: var(--bg-gradient);
                background-size: 400% 400%;
                animation: gradientShift 12s ease infinite;
                color: var(--text-main);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }

            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .container {
                max-width: 900px;
                width: 100%;
                background: var(--card-bg);
                backdrop-filter: blur(16px);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 24px;
                padding: 40px;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
                animation: fadeIn 0.8s ease-out;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                padding-bottom: 24px;
                margin-bottom: 30px;
            }

            .title-area h1 {
                font-size: 2rem;
                font-weight: 700;
                background: linear-gradient(90deg, #ffffff, var(--accent-cyan));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .title-area p {
                color: #94a3b8;
                font-size: 0.95rem;
                margin-top: 4px;
            }

            .status-badge {
                display: flex;
                align-items: center;
                gap: 8px;
                background: rgba(34, 197, 94, 0.15);
                color: var(--accent-green);
                padding: 8px 16px;
                border-radius: 30px;
                font-size: 0.85rem;
                font-weight: 600;
                border: 1px solid rgba(34, 197, 94, 0.3);
            }

            .pulse-dot {
                width: 8px;
                height: 8px;
                background: var(--accent-green);
                border-radius: 50%;
                box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
                animation: pulse 1.8s infinite;
            }

            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
                70% { box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); }
                100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
                margin-bottom: 30px;
            }

            .card {
                background: rgba(15, 23, 42, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.08);
                padding: 20px;
                border-radius: 16px;
                transition: transform 0.2s ease, border-color 0.2s ease;
            }

            .card:hover {
                transform: translateY(-4px);
                border-color: var(--accent-cyan);
            }

            .card-icon {
                font-size: 1.25rem;
                color: var(--accent-cyan);
                margin-bottom: 10px;
            }

            .card-label {
                font-size: 0.75rem;
                color: #64748b;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }

            .card-value {
                font-size: 1.1rem;
                font-weight: 600;
                color: #f1f5f9;
                margin-top: 4px;
            }

            .actions {
                display: flex;
                gap: 16px;
                flex-wrap: wrap;
            }

            .btn {
                flex: 1;
                min-width: 200px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                padding: 14px 24px;
                border-radius: 12px;
                font-weight: 600;
                text-decoration: none;
                transition: all 0.2s ease;
                cursor: pointer;
            }

            .btn-primary {
                background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
                color: #fff;
                box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3);
            }

            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(2, 132, 199, 0.5);
            }

            .btn-secondary {
                background: rgba(255, 255, 255, 0.05);
                color: #cbd5e1;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }

            .btn-secondary:hover {
                background: rgba(255, 255, 255, 0.1);
                color: #fff;
            }

            .interactive-box {
                margin-top: 30px;
                background: rgba(0, 0, 0, 0.3);
                border-radius: 12px;
                padding: 16px;
                font-family: monospace;
                font-size: 0.85rem;
                color: var(--accent-cyan);
                border: 1px solid rgba(255, 255, 255, 0.05);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="title-area">
                    <h1>Task 5 Microservice</h1>
                    <p>Azure Container Apps Deployment • FastAPI</p>
                </div>
                <div class="status-badge">
                    <span class="pulse-dot"></span>
                    System Health: 100%
                </div>
            </div>

            <div class="grid">
                <div class="card">
                    <div class="card-icon"><i class="fa-solid fa-server"></i></div>
                    <div class="card-label">Runtime Engine</div>
                    <div class="card-value">Azure Container Apps</div>
                </div>
                <div class="card">
                    <div class="card-icon"><i class="fa-solid fa-cubes"></i></div>
                    <div class="card-label">Image Host</div>
                    <div class="card-value">Azure Container Registry</div>
                </div>
                <div class="card">
                    <div class="card-icon"><i class="fa-solid fa-code-branch"></i></div>
                    <div class="card-label">CI/CD Automation</div>
                    <div class="card-value">GitHub Actions</div>
                </div>
                <div class="card">
                    <div class="card-icon"><i class="fa-solid fa-bolt"></i></div>
                    <div class="card-label">Framework</div>
                    <div class="card-value">FastAPI + Async</div>
                </div>
            </div>

            <div class="actions">
                <a href="/docs" class="btn btn-primary">
                    <i class="fa-solid fa-book-open"></i> Explore Swagger Documentation
                </a>
                <a href="/health" class="btn btn-secondary" target="_blank">
                    <i class="fa-solid fa-heart-pulse"></i> Test /health Endpoint
                </a>
            </div>

            <div class="interactive-box" id="live-telemetry">
                $ > System status: Active. Listening on port 80. Security check: Passed.
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "app-task5-service",
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "region": "Central India",
        "environment": "Production"
    }