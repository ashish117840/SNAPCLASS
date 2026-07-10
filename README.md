# 🎓 SnapClass — AI-Powered Video & Voice Attendance System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Supabase](https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge&logo=supabase)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

### Intelligent classroom attendance using AI-powered face & voice recognition

🌐 **Live Demo:** [snapclass-ashish-main.streamlit.app](https://snapclass-ashish-main.streamlit.app/)

---

## 📖 Overview

**SnapClass** automates classroom attendance by combining **facial recognition** and **voice/speaker identification**, removing the need for manual roll calls. Teachers get a simple dashboard to manage subjects, students, and attendance logs — all backed by a lightweight, cloud-hosted database.

Built entirely in **Python**, powered by **Streamlit** for the interface and **Supabase** for storage, SnapClass is easy to run locally and simple to deploy.

---

## ✨ Features

- 🎥 **Face recognition attendance** — identifies students from a live camera feed using facial embeddings
- 🎙️ **Voice recognition attendance** — verifies identity through speaker recognition as a secondary/alternate check
- 👩‍🏫 **Teacher dashboard** — manage subjects, enroll students, and review attendance records
- ☁️ **Cloud-backed storage** — all student, subject, and attendance data stored in Supabase
- ⚡ **Lightweight & deployable** — runs locally or on Streamlit Community Cloud with minimal setup

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Web App / UI | Streamlit |
| Database | Supabase |
| Face Recognition | `dlib`, `face_recognition_models` (128-d embeddings + SVM classifier) |
| Voice Recognition | `resemblyzer`, `librosa` |

---

## 🧩 Models Used

| Model | Task | Output |
|---|---|---|
| `dlib` face detector + shape predictor | Face detection & alignment | Bounding box + aligned face |
| `face_recognition_models` (pre-trained) | Face embedding | 128-d face vector |
| SVM (trained on collected embeddings) | Face classification | Predicted student identity |
| `resemblyzer` (pre-trained encoder) | Speaker embedding | 256-d voice vector |

---

## 📂 Project Structure

```
SNAPCLASS/
├── app.py                          # Streamlit entrypoint
├── requirements.txt                # Python dependencies
├── src/
│   ├── pipelines/
│   │   ├── face_pipeline.py        # Face embedding + SVM classifier training
│   │   └── voice_pipeline.py       # Voice embedding + speaker identification
│   └── database/
│       ├── db.py                   # Database helper functions
│       └── config.py               # Supabase configuration
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ashish117840/SNAPCLASS.git
cd SNAPCLASS
```

### 2. Set up your environment

**Recommended (Conda — best for Windows, avoids native build issues):**

```bash
conda create -n snapclass python=3.10 -y
conda activate snapclass
conda install -c conda-forge cmake dlib libsndfile ffmpeg pkg-config -y
pip install -r requirements.txt
```

**Alternative (venv + pip):**

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1      # Windows
# source venv/bin/activate       # macOS/Linux

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 3. Configure Supabase

Create a `.streamlit/secrets.toml` file in the project root:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-service-role-or-anon-key"
```

### 4. Run the app

```bash
streamlit run app.py
```

Open the URL Streamlit prints in your terminal (default: `http://localhost:8501`).

---

## 🧠 How It Works

SnapClass verifies each student through two independent biometric signals — face and voice — before marking attendance.

```
                Student
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
     Camera                Microphone
        │                     │
        ▼                     ▼
 Face Detection         Voice Recording
        │                     │
        ▼                     ▼
 Face Embedding         Voice Embedding
        │                     │
        └──────────┬──────────┘
                    ▼
          Student Verification
                    ▼
           Attendance Marked
                    ▼
          Supabase Database
```

**Face pipeline**
1. **Detection & alignment (`dlib`)** — locates the face in the camera frame as a bounding box, then aligns it (eyes horizontal, nose centered) to normalize pose before recognition.
2. **Embedding (`face_recognition_models`)** — converts each aligned face into a **128-dimensional embedding**, a compact numerical fingerprint of that person's facial features, instead of storing raw images.
3. **Classification (SVM)** — a Support Vector Machine is trained on the embeddings collected per student during registration. At attendance time, it predicts the closest matching student from a live embedding. SVM was chosen because it's fast, accurate, and works well on the small-to-medium datasets typical of a classroom roster.

**Voice pipeline**
1. **Preprocessing (`librosa`)** — loads, resamples, and cleans the audio sample.
2. **Speaker embedding (`resemblyzer`)** — generates a **256-dimensional embedding** that captures *vocal characteristics*, not spoken words — this is speaker recognition ("who is speaking"), not speech-to-text.
3. **Verification** — the live voice embedding is compared against the student's stored embedding as a secondary identity check alongside the face match.

**Why embeddings instead of raw images/audio?** Embeddings are compact, fast to compare, and easy to classify — full images/audio clips are far more expensive to store and match at scale.

**Why not train a deep model from scratch?** Face and voice recognition here rely on pre-trained deep learning models (via `dlib`/`face_recognition_models` and `resemblyzer`) to generate embeddings — this is transfer learning. Only the final identity classification step (the SVM) is trained on your own data, which needs far less data and compute than training a CNN from scratch.

**Data model:** Student, subject, enrollment, and attendance records live in Supabase (PostgreSQL) tables — `teachers`, `students`, `subjects`, `subject_students`, and `attendance_logs`. Each student's face and voice embeddings are stored directly on their record rather than as local files.

**Retraining:** `train_classifier()` in `src/pipelines/face_pipeline.py` clears cached resources and retrains the SVM whenever new student embeddings are added.

---

## 🩺 Troubleshooting

| Issue | Fix |
|---|---|
| `dlib` fails to build | Install Visual Studio Build Tools (C++) and CMake, or use a prebuilt wheel matching your Python version |
| Native dependency errors (`dlib`, `libsndfile`) | Prefer Conda on Windows — these require native libraries that pip alone can struggle with |
| `face_recognition_models` install hangs | It downloads pretrained model files during install — make sure you have network access |
| Audio processing errors | Ensure `ffmpeg` is installed and on your `PATH`, and `libsndfile` is available (install via `conda-forge`) |

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a topic branch for your feature or fix
3. Run checks locally and open a pull request with a clear description of your changes

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ashish Kumar** ([@ashish117840](https://github.com/ashish117840))

---

<p align="center">⭐ If you find this project useful, consider giving it a star!</p>
