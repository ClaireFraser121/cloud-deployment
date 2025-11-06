
🌍 The Big Picture — From Laptop → Cloud → App

╔═══════════════════════════════════════════════════════════╗
║ 💻 Your Laptop                                            ║
║ ───────────────────────────────────────────────────────── ║
║  • You write & edit code (app.py, Dockerfile, deploy.sh)  ║
║  • You run: ./deploy.sh                                   ║
║  • Sends files to your EC2 server via SSH & scp           ║
╚═══════════════════════════════════════════════════════════╝
             │
             │ (SSH / SCP)
             ▼
╔══════════════════════════════════════════════════════════╗
║ ☁️  AWS EC2 Instance (Amazon Linux 2023)                 ║
║ ──────────────────────────────────────────────────────── ║
║  • A virtual Linux computer running in AWS               ║
║  • Receives your files and builds your Docker image      ║
║  • Runs Docker to start your container                   ║
║                                                          ║
║  🐳 Docker (on EC2)                                      ║
║  ─────────────────────────────────────────────────────   ║
║   • Creates a lightweight sandbox for your app            ║
║   • Uses your Dockerfile to install Flask, copy code, etc ║
║   • Starts your Flask app inside the container            ║
║                                                          ║
║   [Container: message-server]                            ║
║     → Runs: python app.py                                ║
║     → Listens on port 5002 (inside container)            ║
║     → Exposed as 0.0.0.0:5002 on EC2                     ║
║                                                          ║
║  EC2 Security Group: allows inbound TCP :5002            ║
╚══════════════════════════════════════════════════════════╝
             │
             │ (Internet)
             ▼
╔══════════════════════════════════════════════════════════╗
║ 🧠 AWS RDS (PostgreSQL Database)                         ║
║ ──────────────────────────────────────────────────────── ║
║  • Stores your app’s data securely                       ║
║  • Flask app connects here via environment variables      ║
║    (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, …)   ║
╚══════════════════════════════════════════════════════════╝
             │
             ▼
╔══════════════════════════════════════════════════════════╗
║ 🌐 Your Browser / Client                                 ║
║ ──────────────────────────────────────────────────────── ║
║  • You visit http://18.130.226.174:5002                  ║
║  • Request travels → EC2 → Docker → Flask → RDS          ║
║  • Response comes all the way back to you                ║
╚══════════════════════════════════════════════════════════╝

🧭 How to think about it
| Layer      | Role                    | You interact via          |
| ---------- | ----------------------- | ------------------------- |
| **Laptop** | Development workstation | Terminal, VS Code, Git    |
| **EC2**    | Remote Linux host       | SSH                       |
| **Docker** | App runtime sandbox     | `docker` CLI              |
| **Flask**  | Your running code       | Browser or `curl`         |
| **RDS**    | Database backend        | Flask’s connection string |

⚙️ Request flow (step-by-step)
🧑‍💻 You → browser: http://18.130.226.174:5002
🌐 AWS routes to your EC2 public IP
🐧 EC2 receives the request on port 5002
🐳 Docker forwards 5002 → Flask app inside container
🧩 Flask handles request (maybe queries RDS)
🧠 RDS returns data to Flask
🌍 Flask → Docker → EC2 → Internet → your browser

🔍 Quick tip to “see where you are”
| Prompt looks like               | Where you are    | Can run                           |
| ------------------------------- | ---------------- | --------------------------------- |
| `(secure_venv) ➜ simple_server` | 💻 Laptop        | `./deploy.sh`, `git`, edit code   |
| `[ec2-user@ip-172-31-26-1 ~]$`  | ☁️ EC2           | `docker ps`, `curl`, `sudo dnf`   |
| `root@a1b2c3d4:/#`              | 🐳 Inside Docker | `python`, inspect container files |
