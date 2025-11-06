# app.py
# ─────────────────────────────────────────────────────────────────
# WHERE:   Your laptop (source code). Copied to EC2 during deploy.
# WHAT:    Minimal Flask app; reads config from environment.
# WHY:     Makes the container image generic; no secrets in code.
# ─────────────────────────────────────────────────────────────────

import os
from flask import Flask

app = Flask(__name__)

# Read environment to know how to behave (set in .env.prod on EC2)
APP_ENV = os.getenv("APP_ENV", "DEVELOPMENT")

# Database settings (the container receives these via --env-file .env.prod)
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "postgres")

@app.get("/")
def home():
    # Simple response so you can prove which mode/instance is serving you
    return f"message-server is up (env={APP_ENV})"

if __name__ == "__main__":
    # Bind to all interfaces INSIDE the container on the configured port.
    # Default to 5002 so it can live alongside your 5001 demo.
    port = int(os.getenv("PORT", "5002"))
    app.run(host="0.0.0.0",
            port=port,
            debug=(APP_ENV != "PRODUCTION"))  # debug off in prod
