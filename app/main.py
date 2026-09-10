from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time

app = FastAPI(
    title="CloudKinetics Enterprise Microservice",
    description="Advanced Portfolio Dashboard featuring completed Azure Technical Exercises 1 to 5.",
    version="2.0.0"
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
                --bg-gradient: linear-gradient(-45deg, #030712, #0f172a, #1e1b4b, #0f2027);
                --card-bg: rgba(15, 23, 42, 0.75);
                --accent-blue: #38bdf8;
                --accent-green: #22c55e;
                --accent-purple: #c084fc;
                --accent-cyan: #06b6d4;
                --text-main: #f8fafc;
            }

            * { box-sizing: border-box; margin: 0; padding: 0; }

            body {
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
                background: var(--bg-gradient);
                background-size: 400% 400%;
                animation: gradientShift 15s ease infinite;
                color: var(--text-main);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 30px 20px;
                position: relative;
                overflow-x: hidden;
            }

            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            /* Floating Background Animation Spheres */
            .orb {
                position: absolute;
                border-radius: 50%;
                filter: blur(80px);
                opacity: 0.35;
                z-index: 0;
                animation: float 10s ease-in-out infinite alternate;
            }

            .orb-1 { width: 300px; height: 300px; background: #0284c7; top: 10%; left: 10%; }
            .orb-2 { width: 350px; height: 350px; background: #a855f7; bottom: 10%; right: 10%; animation-delay: -5s; }

            @keyframes float {
                0% { transform: translateY(0) scale(1); }
                100% { transform: translateY(-30px) scale(1.08); }
            }

            .container {
                position: relative;
                z-index: 10;
                max-width: 1000px;
                width: 100%;
                background: var(--card-bg);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 28px;
                padding: 45px;
                box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.8), 0 0 30px rgba(56, 189, 248, 0.15);
                animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            }

            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid rgba(255, 255, 255, 0.12);
                padding-bottom: 24px;
                margin-bottom: 30px;
                flex-wrap: wrap;
                gap: 15px;
            }

            .title-area h1 {
                font-size: 2.3rem;
                font-weight: 800;
                background: linear-gradient(90deg, #ffffff, var(--accent-blue), #a855f7);
                background-size: 200% auto;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: textGlow 6s linear infinite;
            }

            @keyframes textGlow {
                to { background-position: 200% center; }
            }

            .title-area p {
                color: #94a3b8;
                font-size: 1rem;
                margin-top: 6px;
            }

            .status-badge {
                display: flex;
                align-items: center;
                gap: 10px;
                background: rgba(34, 197, 94, 0.12);
                color: var(--accent-green);
                padding: 10px 20px;
                border-radius: 30px;
                font-size: 0.9rem;
                font-weight: 700;
                border: 1px solid rgba(34, 197, 94, 0.4);
                box-shadow: 0 0 15px rgba(34, 197, 94, 0.2);
            }

            .pulse-dot {
                width: 10px;
                height: 10px;
                background: var(--accent-green);
                border-radius: 50%;
                box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
                animation: pulse 1.8s infinite;
            }

            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
                70% { box-shadow: 0 0 0 12px rgba(34, 197, 94, 0); }
                100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
            }

            .section-title {
                font-size: 1.05rem;
                font-weight: 700;
                color: var(--accent-blue);
                margin-bottom: 20px;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                display: flex;
                align-items: center;
                gap: 8px;
            }

            .exercise-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 18px;
                margin-bottom: 35px;
            }

            .ex-card {
                background: rgba(30, 41, 59, 0.55);
                border: 1px solid rgba(255, 255, 255, 0.08);
                padding: 22px;
                border-radius: 18px;
                position: relative;
                overflow: hidden;
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }

            .ex-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0; height: 3px;
                background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
                opacity: 0;
                transition: opacity 0.3s ease;
            }

            .ex-card:hover {
                transform: translateY(-6px);
                border-color: rgba(56, 189, 248, 0.4);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.2);
                background: rgba(30, 41, 59, 0.85);
            }

            .ex-card:hover::before {
                opacity: 1;
            }

            .ex-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 12px;
            }

            .ex-number {
                font-size: 0.75rem;
                font-weight: 800;
                color: var(--accent-purple);
                background: rgba(192, 132, 252, 0.12);
                padding: 4px 10px;
                border-radius: 10px;
                border: 1px solid rgba(192, 132, 252, 0.2);
            }

            .check-icon {
                color: var(--accent-green);
                font-size: 1.1rem;
            }

            .ex-title {
                font-size: 1.05rem;
                font-weight: 700;
                color: #f1f5f9;
                margin-bottom: 6px;
            }

            .ex-desc {
                font-size: 0.84rem;
                color: #94a3b8;
                line-height: 1.5;
            }

            .actions {
                display: flex;
                gap: 16px;
                flex-wrap: wrap;
            }

            .btn {
                flex: 1;
                min-width: 220px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 12px;
                padding: 16px 28px;
                border-radius: 14px;
                font-weight: 700;
                font-size: 0.95rem;
                text-decoration: none;
                transition: all 0.3s ease;
                cursor: pointer;
            }

            .btn-primary {
                background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
                color: #fff;
                box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4);
            }

            .btn-primary:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 30px rgba(2, 132, 199, 0.7);
            }

            .btn-secondary {
                background: rgba(255, 255, 255, 0.06);
                color: #cbd5e1;
                border: 1px solid rgba(255, 255, 255, 0.12);
            }

            .btn-secondary:hover {
                background: rgba(255, 255, 255, 0.12);
                color: #fff;
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>

        <div class="container">
            <div class="header">
                <div class="title-area">
                    <h1>Azure Cloud Engineering Portfolio</h1>
                    <p>CloudKinetics Technical Exercises (1 – 5 Complete)</p>
                </div>
                <div class="status-badge">
                    <span class="pulse-dot"></span>
                    Task 5 Microservice Active
                </div>
            </div>

            <div class="section-title">
                <i class="fa-solid fa-layer-group"></i> Completed Azure Track Architecture
            </div>

            <div class="exercise-grid">
                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 1</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Multi-Tier Isolated Networking</div>
                    <div class="ex-desc">Azure VNet (10.1.0.0/16), Subnets, NAT Gateway, NGINX VM, PostgreSQL Flexible Server & NSG boundary security controls.</div>
                </div>

                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 2</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Infrastructure as Code (IaC)</div>
                    <div class="ex-desc">Terraform modular architecture, Azure Blob Storage remote backend with lease locking, and idempotent deployments.</div>
                </div>

                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 3</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Static Web Hosting & CDN</div>
                    <div class="ex-desc">Azure Storage Account Static Website, private blob access, Azure CDN profile delivery, and HTTPS enforcement.</div>
                </div>

                <div class="ex-card">
                    <div class="ex-header">
                        <span class="ex-number">EXERCISE 4</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Serverless Event Pipeline</div>
                    <div class="ex-desc">Azure API Management, Azure Functions serverless runtime, Cosmos DB NoSQL database, and Application Insights telemetry.</div>
                </div>

                <div class="ex-card" style="border-color: rgba(56, 189, 248, 0.5); background: rgba(14, 165, 233, 0.12);">
                    <div class="ex-header">
                        <span class="ex-number" style="color: var(--accent-blue); background: rgba(56, 189, 248, 0.15);">EXERCISE 5</span>
                        <i class="fa-solid fa-circle-check check-icon"></i>
                    </div>
                    <div class="ex-title">Containerization & CI/CD</div>
                    <div class="ex-desc">FastAPI containerized application, Azure Container Registry (ACR), GitHub Actions automated pipeline & Azure Container Apps.</div>
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