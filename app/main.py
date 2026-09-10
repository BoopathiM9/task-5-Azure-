from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time

app = FastAPI(
    title="CloudKinetics Enterprise Microservice",
    description="Azure Portfolio Dashboard featuring completed Exercises 1 through 5.",
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
        <title>Azure Cloud Engineering Portfolio</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            :root {
                --bg-gradient: linear-gradient(-45deg, #0b1120, #1e1b4b, #0f172a, #1e293b);
                --card-bg: rgba(15, 23, 42, 0.8);
                --accent-blue: #38bdf8;
                --accent-green: #22c55e;
                --accent-purple: #c084fc;
                --text-main: #f8fafc;
            }

            * { box-sizing: border-box; margin: 0; padding: 0; }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: var(--bg-gradient);
                background-size: 400% 400%;
                animation: gradientShift 15s ease infinite;
                color: var(--text-main);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 30px 20px;
            }

            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .container {
                max-width: 950px;
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
                flex-wrap: wrap;
                gap: 15px;
            }

            .title-area h1 {
                font-size: 2.2rem;
                font-weight: 700;
                background: linear-gradient(90deg, #ffffff, var(--accent-blue));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .title-area p {
                color: #94a3b8;
                font-size: 1rem;
                margin-top: 4px;
            }

            .status-badge {
                display: flex;
                align-items: center;
                gap: 8px;
                background: rgba(34, 197, 94, 0.15);
                color: var(--accent-green);
                padding: 8px 18px;
                border-radius: 30px;
                font-size: 0.88rem;
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

            .section-title {
                font-size: 1.1rem;
                font-weight: 600;
                color: var(--accent-blue);
                margin-bottom: 16px;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }

            .exercise-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
                gap: 16px;
                margin-bottom: 35px;
            }

            .ex-card {
                background: rgba(30, 41, 59, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.08);
                padding: 20px;
                border-radius: 16px;
                transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
            }

            .ex-card:hover {
                transform: translateY(-4px);
                border-color: var(--accent-blue);
                box-shadow: 0 10px 20px rgba(56, 189, 248, 0.15);
            }

            .ex-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }

            .ex-number {
                font-size: 0.8rem;
                font-weight: 700;
                color: var(--accent-purple);
                background: rgba(192, 132, 252, 0.1);
                padding: 4px 10px;
                border-radius: 12px;
            }

            .check-icon {
                color: var(--accent-green);
            }

            .ex-title {
                font-size: 1rem;
                font-weight: 600;
                color: #f1f5f9;
                margin-bottom: 6px;
            }

            .ex-desc {
                font-size: 0.82rem;
                color: #94a3b8;
                line-height: 1.4;
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
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="title-area">
                    <h1>Azure Cloud Engineering Portfolio</h1>
                    <p>CloudKinetics Technical Exercises (1 – 5 Complete)</p>
                </div>
                <div class="status-badge">
                    <span class="pulse-dot"></span>
                    Task 5 Deployed
                </div>
            </div>

            <div class="section-title">Completed Azure Track Exercises</div>

            <div class="exercise-grid">
                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 1</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Isolated Networking</div>
                    <div class="ex-desc">Azure VNet, Subnets, NGINX VM, PostgreSQL Flexible Server & NSG controls.</div>
                </div>

                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 2</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Infrastructure as Code</div>
                    <div class="ex-desc">Terraform modules, Azure Blob state locking, and automated deployments.</div>
                </div>

                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 3</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Static Web & CDN</div>
                    <div class="ex-desc">Azure Storage Static Website, Azure CDN Profile, and HTTPS enforcement.</div>
                </div>

                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 4</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Serverless Event Pipeline</div>
                    <div class="ex-desc">Azure Functions, Cosmos DB NoSQL integration, and Application Insights[cite: 1].</div>
                </div>

                <div class="ex-card" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(14, 165, 233, 0.1);">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 5</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Containerized CI/CD</div>
                    <div class="ex-desc">FastAPI container, Azure Container Registry (ACR), GitHub Actions & Container Apps[cite: 1].</div>
                </div>
            </div>

            <div class="actions">
                <a href="/docs" class="btn btn-primary">
                    <i class="fa-solid fa-book-open"></i> Test Interactive Swagger UI
                </a>
                <a href="/health" class="btn btn-secondary" target="_blank">
                    <i class="fa-solid fa-heart-pulse"></i> Live Health Check Endpoint
                </a>
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
        "track": "Azure Cloud Engineering Track (Exercises 1-5)",
        "environment": "Azure Container Apps"
    }