from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Task 5 Microservice",
    description="Containerized REST API deployed via GitHub Actions CI/CD to Azure Container Apps.",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CloudKinetics Microservice</title>
        <style>
            :root {
                --bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
                --card-bg: rgba(30, 41, 59, 0.7);
                --accent-blue: #38bdf8;
                --accent-green: #22c55e;
                --text-main: #f8fafc;
            }

            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: var(--bg-gradient);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
                color: var(--text-main);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .card {
                background: var(--card-bg);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 40px;
                max-width: 500px;
                width: 90%;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
                text-align: center;
                transform: translateY(30px);
                opacity: 0;
                animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            }

            @keyframes fadeInUp {
                to {
                    transform: translateY(0);
                    opacity: 1;
                }
            }

            .badge {
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: rgba(34, 197, 94, 0.15);
                color: var(--accent-green);
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 0.875rem;
                font-weight: 600;
                border: 1px solid rgba(34, 197, 94, 0.3);
            }

            .pulse-dot {
                width: 8px;
                height: 8px;
                background-color: var(--accent-green);
                border-radius: 50%;
                box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
                animation: pulse 2s infinite;
            }

            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
                70% { box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); }
                100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
            }

            h1 {
                font-size: 2.25rem;
                margin: 20px 0 10px;
                background: linear-gradient(90deg, #ffffff, var(--accent-blue));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            p {
                color: #94a3b8;
                line-height: 1.6;
                margin-bottom: 30px;
            }

            .btn {
                display: inline-block;
                width: 100%;
                padding: 14px 0;
                background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
                color: #ffffff;
                text-decoration: none;
                font-weight: 600;
                border-radius: 10px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
            }

            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(2, 132, 199, 0.6);
            }

            .metrics {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
                margin-top: 25px;
            }

            .metric-box {
                background: rgba(15, 23, 42, 0.5);
                padding: 12px;
                border-radius: 8px;
                border: 1px solid rgba(255, 255, 255, 0.05);
            }

            .metric-label {
                font-size: 0.75rem;
                color: #64748b;
                text-transform: uppercase;
            }

            .metric-value {
                font-size: 0.95rem;
                font-weight: 600;
                color: var(--accent-blue);
                margin-top: 4px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">
                <span class="pulse-dot"></span>
                System Operational
            </div>
            <h1>Task 5 Microservice</h1>
            <p>Containerized REST API deployed via GitHub Actions CI/CD to Azure Container Apps.</p>
            
            <a href="/docs" class="btn">View Interactive Swagger Docs</a>

            <div class="metrics">
                <div class="metric-box">
                    <div class="metric-label">Environment</div>
                    <div class="metric-value">Azure Apps</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Pipeline</div>
                    <div class="metric-value">GitHub CI/CD</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "task-5-api"}