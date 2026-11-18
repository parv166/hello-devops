
import os

from flask import Flask, render_template_string, jsonify

app = Flask(__name__)
APP_ENV = os.getenv("APP_ENV", "development")
APP_TAGLINE = os.getenv("APP_TAGLINE", "My Kubernetes Homelab")
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello DevOps | Kubernetes Homelab</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            font-family: 'Segoe UI', sans-serif;
            background: #080d1b;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px 20px;
            overflow-x: hidden;
        }

        body::before {
            content: "";
            position: fixed;
            width: 400px;
            height: 400px;
            background: #653cff;
            filter: blur(150px);
            opacity: 0.25;
            top: -150px;
            left: -100px;
            z-index: -1;
        }

        body::after {
            content: "";
            position: fixed;
            width: 400px;
            height: 400px;
            background: #008cff;
            filter: blur(150px);
            opacity: 0.18;
            bottom: -150px;
            right: -100px;
            z-index: -1;
        }

        .container {
            width: 100%;
            max-width: 900px;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 70px;
        }

        .logo {
            font-size: 21px;
            font-weight: 700;
            letter-spacing: -0.5px;
        }

        .logo span {
            color: #8b7bff;
        }

        .badge {
            padding: 9px 15px;
            border: 1px solid #244b45;
            background: #102a27;
            border-radius: 30px;
            color: #55e6ad;
            font-size: 12px;
        }

        .badge::before {
            content: "●";
            margin-right: 8px;
            font-size: 10px;
        }

        .hero {
            text-align: center;
            padding: 50px 25px;
            border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.035);
            backdrop-filter: blur(15px);
            border-radius: 24px;
            box-shadow: 0 25px 80px rgba(0,0,0,0.25);
        }

        .tag {
            display: inline-block;
            color: #a99aff;
            background: rgba(139,123,255,0.12);
            border: 1px solid rgba(139,123,255,0.2);
            border-radius: 30px;
            padding: 8px 16px;
            font-size: 12px;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 28px;
        }

        h1 {
            font-size: clamp(38px, 7vw, 65px);
            letter-spacing: -2px;
            line-height: 1.15;
            margin-bottom: 20px;
        }

        h1 span {
            background: linear-gradient(90deg, #8b7bff, #44c5ff);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .description {
            max-width: 570px;
            margin: auto;
            color: #9ca8bd;
            font-size: 16px;
            line-height: 1.8;
        }

        .button {
            display: inline-block;
            margin-top: 32px;
            padding: 14px 27px;
            background: linear-gradient(90deg, #7357ef, #438bff);
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: 600;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(99,102,241,0.35);
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-top: 25px;
        }

        .stat-card {
            padding: 23px 12px;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 15px;
            text-align: center;
        }

        .stat-card h3 {
            font-size: 19px;
            margin-bottom: 8px;
            color: #b3a5ff;
        }

        .stat-card p {
            font-size: 12px;
            color: #8c99ad;
        }

        footer {
            text-align: center;
            margin-top: 35px;
            color: #68758b;
            font-size: 12px;
        }

        @media (max-width: 600px) {
            .navbar {
                margin-bottom: 35px;
            }

            .hero {
                padding: 40px 18px;
            }

            .stats {
                grid-template-columns: 1fr;
            }

            h1 {
                letter-spacing: -1px;
            }
        }
    </style>
</head>

<body>
    <main class="container">

        <nav class="navbar">
            <div class="logo">Hello<span>DevOps.</span></div>
            <div class="badge">Application Healthy</div>
        </nav>

        <section class="hero">
            <div class="tag">{{ app_tagline }}</div>

            <h1>
                Hello, <span>GitOps!</span>
            </h1>

            <p class="description">
                My first application running inside a containerized
                environment. Built with Python, powered by Docker,
                and ready for Kubernetes orchestration.
            </p>

            <a href="/health" class="button">
                Check Application Health →
            </a>
        </section>

        <section class="stats">
            <div class="stat-card">
                <h3>Python</h3>
                <p>Backend Framework</p>
            </div>

            <div class="stat-card">
                <h3>Docker</h3>
                <p>Containerization</p>
            </div>

            <div class="stat-card">
                <h3>Kubernetes</h3>
                <p>Orchestration</p>
            </div>
        </section>

        <footer>
            Built for learning DevOps · My Personal Homelab
        </footer>

    </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, app_tagline=APP_TAGLINE)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "environment": APP_ENV,
        "application": "Hello DevOps",
        "message": "Application is running successfully"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
