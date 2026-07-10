# SNAPCLASS

> Making attendance faster using AI — face and voice based attendance system built with Streamlit and Supabase.

## Table of contents

- Project overview
- Features
- Architecture / important files
- Requirements & recommended environment
- Local setup (Windows)
- Supabase / secrets
- Running the app
- Troubleshooting & tips (dlib, audio, models)
- Development notes
- Contributing
- License

## Project overview

SNAPCLASS is a Streamlit web app that provides automated attendance using face recognition and voice identification. It stores users and attendance logs in Supabase and includes pipelines for extracting face embeddings (dlib) and voice embeddings (`resemblyzer`).

## Features

- Teacher and student roles (login flows)
- Face-based attendance using precomputed embeddings and an SVM classifier
- Voice-based speaker identification for audio attendance
- Subject management and enrollment
- Supabase-backed persistent storage for users, subjects, and logs

## Architecture / important files

- `app.py` — Application entrypoint and routing to screens
- `requirements.txt` — Python dependencies
- `src/database/config.py` — Supabase client initialization (reads from Streamlit secrets)
- `src/database/db.py` — Database helper functions (create users, subjects, attendance)
- `src/pipelines/face_pipeline.py` — Face model loading, embedding extraction, classifier training/prediction
- `src/pipelines/voice_pipeline.py` — Voice encoder and audio processing utilities
- `src/screens/` — Streamlit UI screens (`home_screen.py`, `teacher_screen.py`, `student_screen.py`)
- `src/components/` — Dialogs and UI components

## Requirements & recommended environment

This project depends on several packages that require native binaries. On Windows, using Conda is strongly recommended for easier native dependency management.

- Python 3.9+ (3.10 recommended)
- Recommended: Conda (Miniconda/Anaconda) for `dlib`, `libsndfile`, and audio dependencies
- If using venv/pip you will need: Visual Studio Build Tools, CMake, and `ffmpeg` installed in PATH

Key dependencies (from `requirements.txt`):

- `streamlit`
- `numpy`, `pandas`
- `scikit-learn`, `dlib` (native), `face_recognition_models` (git)
- `supabase` (python client)
- `bcrypt`
- `pillow`, `segno`
- `librosa`, `resemblyzer` (audio)

## Local setup (Windows)

Option A — Conda (recommended):

```powershell
# create conda env
conda create -n snapclass python=3.10 -y
conda activate snapclass

# install common binary deps first
conda install -c conda-forge cmake dlib libsndfile ffmpeg pkg-config -y

# then pip install python packages
pip install -r requirements.txt
```

Option B — venv + pip (may require build tools):

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Notes:
- If `dlib` fails to build, install Visual Studio Build Tools and CMake, or use a prebuilt wheel.
- `face_recognition_models` is installed directly from GitHub (see `requirements.txt`).
- Install `ffmpeg` and ensure it's on PATH for audio processing.

## Supabase / secrets

The app reads Supabase credentials from Streamlit secrets. Create `.streamlit/secrets.toml` in the project root with:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-service-role-or-anon-key"
```

Alternatively, you can set these values as environment variables and update `src/database/config.py` accordingly.

## Running the app

Start Streamlit from the project root:

```powershell
.\\venv\\Scripts\\Activate.ps1   # or `conda activate snapclass`
streamlit run app.py
```

Open the local URL printed by Streamlit (usually `http://localhost:8501`).

## Troubleshooting & tips

- dlib build errors on Windows:
  - Install Visual Studio Build Tools (C++), CMake, and ensure they are on PATH.
  - Prefer Conda and `conda install -c conda-forge dlib` or use a prebuilt wheel for your Python version.

- face_recognition_models:
  - This package downloads pre-trained model files; allow network access during `pip install`.

- resemblyzer / librosa audio errors:
  - Install `libsndfile` (conda-forge) and `ffmpeg` system binary.
  - If `librosa` raises `audioread` errors, ensure `ffmpeg` is installed and in PATH.

- Performance / memory:
  - Face and voice models can be memory-heavy. For large classes, consider batching or smaller sample rates.

- Streamlit session state & secrets:
  - If Supabase keys are missing, the app will fail at `src/database/config.py`. Add secrets before running.

## Development notes

- To retrain face classifier the UI triggers `train_classifier()` which clears cached resources in `src/pipelines/face_pipeline.py`.
- Embeddings are stored per-student in Supabase (fields: `face_embedding`, `voice_embedding`).
- Database helper functions live in `src/database/db.py` — extend these for additional queries.

## Contributing

1. Fork the repo and create a feature branch.
2. Run tests (if added) and linters locally.
3. Submit a PR with a clear description of changes.

## License

This repository does not include a license file. If you want to open-source it, consider adding an `LICENSE` (MIT is common).

---

If you'd like, I can also:

- Add this README to the repo now (I will). 
- Add a short `CONTRIBUTING.md` or CI notes for Windows builds.
- Try installing the environment in your workspace and run `streamlit` to verify.
