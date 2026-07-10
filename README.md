# 🎓 SNAPCLASS – AI Video & Voice Attendance System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge\&logo=streamlit)
![Supabase](https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge\&logo=supabase)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

### Intelligent Attendance Management using AI-powered Face & Voice Recognition

🌐 **Live Demo:** https://snapclass-ashish-main.streamlit.app/

</div>

---

## 📖 Overview

**SNAPCLASS** is an AI-powered attendance management system that automates classroom attendance using **face recognition** and **voice recognition**. It eliminates manual attendance, improves accuracy, and provides teachers with an easy-to-use dashboard for managing classes and attendance records.

The application is built with **Python**, **Streamlit**, and **Supabase**, making it lightweight, scalable, and easy to deploy.

<!-- Improved README: clearer structure, badges, logo, and concise instructions -->
# SNAPCLASS

![SNAPCLASS logo](https://i.ibb.co/YTYGn5qV/logo.png)

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-%3E%3D1.0-orange)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-ADD--LICENSE-lightgrey)](LICENSE)

Streamline classroom attendance using AI — face recognition (dlib + pre-trained models) and speaker identification (resemblyzer). Built with Streamlit and Supabase for storage.

## Quick links

- Entrypoint: `app.py`
- Pipelines: `src/pipelines/face_pipeline.py`, `src/pipelines/voice_pipeline.py`
- Database helpers: `src/database/db.py`
- Config: `src/database/config.py`

## Quick start (copy-paste)

1. Clone the repo and change directory:

```bash
git clone https://github.com/ashish117840/SNAPCLASS.git
cd SNAPCLASS
```

2. Recommended: create a Conda environment (Windows):

```powershell
conda create -n snapclass python=3.10 -y
conda activate snapclass
conda install -c conda-forge cmake dlib libsndfile ffmpeg pkg-config -y
pip install -r requirements.txt
```

Alternative (venv + pip):

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

3. Add Supabase secrets (create `.streamlit/secrets.toml`):

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-service-role-or-anon-key"
```

4. Run the app:

```powershell
streamlit run app.py
```

Open the URL printed by Streamlit (default: `http://localhost:8501`).

## What this project does

- Uses `dlib` and `face_recognition_models` to extract 128-d face embeddings and an SVM classifier for identification.
- Uses `resemblyzer` + `librosa` to create voice embeddings and perform speaker identification.
- Stores users, subjects, enrollments, and attendance logs in Supabase tables (`teachers`, `students`, `subjects`, `subject_students`, `attendance_logs`).

## Important notes & troubleshooting

- Native dependencies: `dlib`, `libsndfile`, and some audio tooling require native libraries — use Conda on Windows to avoid build issues.
- If `dlib` fails to build: install Visual Studio Build Tools (C++), CMake, or use a prebuilt wheel for your Python version.
- `face_recognition_models` downloads pretrained model files during install; allow network access.
- For audio processing: ensure `ffmpeg` is installed and in `PATH` and `libsndfile` is available (conda-forge package).

## Development notes

- Embeddings are stored on the student records in Supabase (`face_embedding`, `voice_embedding`).
- `train_classifier()` in `src/pipelines/face_pipeline.py` clears cached resources and retrains the SVM from embeddings in the database.

## Contributing

1. Fork the repository.
2. Create a topic branch and implement features / fixes.
3. Run checks and open a pull request with a clear description.

If you'd like, I can add a `CONTRIBUTING.md`, CI (GitHub Actions) to run lint/tests, or prepare a Dockerfile for consistent runtime.

## License

This repo currently has no license. Add a `LICENSE` file (e.g., MIT) to make the project open-source.

---

File: `README.md` updated and pushed to the `main` branch on GitHub.
### 4. Install dependencies
