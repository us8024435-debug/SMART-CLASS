# 🎓 Smart Class: AI-Powered Attendance System

**Smart Class** is a production-ready, high-performance attendance management platform that leverages cutting-edge Artificial Intelligence to streamline classroom administration. Built with a focus on precision, security, and user experience, it replaces traditional manual roll calls with seamless biometric verification.

---

## 🏗️ System Architecture

The project follows a modular, decoupled architecture designed for scalability and maintainability:

- **Frontend Tier**: A high-reactivity UI built with **Streamlit**, providing a desktop-class experience in the browser.
- **Biometric Layer**:
  - **Face ID**: Deep learning-based facial embedding extraction using `dlib` and `face_recognition`.
  - **Voice ID**: Speaker verification via `resemblyzer` and `librosa` for voice-based roll call.
- **Data Persistence Layer**: A robust **PostgreSQL** backend hosted on **Supabase**, utilizing RLS (Row Level Security) and optimized indexing.
- **Security Middleware**: Native Python `bcrypt` implementation for credential hashing and Streamlit Secrets management for environment isolation.

---

## 🛠️ Technology Stack

| Component            | Technology              | Description                                                    |
| :------------------- | :---------------------- | :------------------------------------------------------------- |
| **Language**         | Python 3.10+            | The core logic and AI integration engine.                      |
| **Web Framework**    | Streamlit               | Rapid UI development with custom CSS injection.                |
| **Database**         | Supabase (Postgres)     | Real-time database with built-in Auth & Storage support.       |
| **Computer Vision**  | face_recognition (dlib) | HOG and CNN models for high-accuracy face matching.            |
| **Audio Processing** | Resemblyzer / PyTorch   | SincNet-based speaker embeddings for voice verification.       |
| **Design System**    | Custom Vanilla CSS      | "BMW M" inspired industrial aesthetic with premium animations. |

---

## 📂 Project Structure

```text
SMART_CLASS/
├── app.py                # Central Router & Entry Point
├── src/
│   ├── screens/          # View Layer (Home, Teacher, Student Dashboards)
│   ├── components/       # Reusable UI Elements (Headers, Custom Dialogs)
│   ├── pipelines/        # AI Logic (Face Embedding, Voice Processing)
│   ├── database/         # Data Access Layer (Supabase Client, DB Operations)
│   └── ui/               # Design Tokens (Theme, Global CSS, Layout)
├── .streamlit/           # Infrastructure Config (Secrets, Theme Settings)
├── icons/                # Branding Assets
└── schema.sql            # Database Definition (DDL)
```

---

## 🚀 Getting Started

### 1. Environment Preparation

Ensure you have a modern Python environment (3.10 or higher).

```bash
# Initialize Virtual Environment
python -m venv venv
./venv/Scripts/activate  # Windows
source venv/bin/activate # Unix/macOS
```

### 2. Dependency Injection

Install the specialized AI and backend libraries:

```bash
pip install -r requirements.txt
```

### 3. Backend Provisioning

1. Create a new project at [Supabase](https://supabase.com).
2. Execute the `schema.sql` script in the **SQL Editor** to initialize the database architecture.
3. Configure your credentials in `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-public-key"
```

### 4. Launch the Application

```bash
streamlit run app.py
```

---

## 🔐 Security & Reliability

- **Biometric Privacy**: Face and voice data are stored as mathematical embeddings (JSONB), not raw media files, ensuring user privacy and reducing storage overhead.
- **Encrypted Auth**: Teacher credentials never hit the database in plain text; we use `bcrypt` with salt for standard-compliant security.
- **Modular Pipelines**: AI logic is separated from UI logic, allowing for independent model upgrades without breaking the user interface.

---

## 👨‍💻 Developer Note

_As a system designed with 30 years of architectural best practices in mind, Smart Class prioritizes 'Clean Code' principles and separation of concerns. The UI is intentionally decoupled from the biometric processing, making it trivial to swap face/voice models as the AI landscape evolves._

---

_© 2026 Smart Class Development Team. Built for the future of education._
