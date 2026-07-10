<div align="center">

<img src="https://i.ibb.co/YTYGn5qV/logo.png" width="180">

# 🎓 SNAPCLASS

### AI-Powered Face & Voice Attendance System

<p>
  <a href="https://snapclass-ashish-main.streamlit.app/">
    <img src="https://img.shields.io/badge/Live-Demo-success?style=for-the-badge">
  </a>
  <a href="https://github.com/ashish117840/SNAPCLASS">
    <img src="https://img.shields.io/github/stars/ashish117840/SNAPCLASS?style=for-the-badge">
  </a>
  <a href="https://github.com/ashish117840/SNAPCLASS/network/members">
    <img src="https://img.shields.io/github/forks/ashish117840/SNAPCLASS?style=for-the-badge">
  </a>
</p>

<p>
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white">
</p>

**An AI-powered attendance management system using Face Recognition and Voice Recognition.**

🌐 **Live Website:** https://snapclass-ashish-main.streamlit.app/

</div>

---

# 📖 Overview

SNAPCLASS is an intelligent attendance management system that automates classroom attendance using Artificial Intelligence.

Instead of manually marking attendance, the application verifies each student through:

- 👤 Face Recognition
- 🎤 Voice Recognition

The attendance is securely stored in **Supabase PostgreSQL**, providing a fast, reliable, and paperless attendance system.

---

# ✨ Features

- ✅ Teacher Dashboard
- ✅ Student Registration
- ✅ Subject Management
- ✅ Face Recognition Attendance
- ✅ Voice Recognition Attendance
- ✅ AI-based Student Verification
- ✅ Attendance Logs
- ✅ Supabase Integration
- ✅ Streamlit Web Application
- 🚀 Fast & Lightweight

---

# 🏗️ System Architecture

```
                    Teacher

                       │
                       ▼

              Streamlit Web App

             ┌─────────┴─────────┐
             │                   │

             ▼                   ▼

      Face Recognition     Voice Recognition

             │                   │

             └─────────┬─────────┘
                       │

                       ▼

            AI Verification Engine

                       │

                       ▼

            Supabase PostgreSQL
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | Web Interface |
| Supabase | Database |
| PostgreSQL | Data Storage |
| OpenCV | Face Detection |
| dlib | Face Recognition |
| face_recognition_models | Face Embeddings |
| scikit-learn | SVM Classifier |
| Resemblyzer | Voice Embeddings |
| Librosa | Audio Processing |

---

# 📂 Project Structure

```
SNAPCLASS
│
├── app.py
├── requirements.txt
│
├── .streamlit
│   └── secrets.toml
│
├── src
│   ├── components
│   ├── database
│   │      ├── config.py
│   │      └── db.py
│   │
│   ├── pipelines
│   │      ├── face_pipeline.py
│   │      └── voice_pipeline.py
│   │
│   ├── ui
│   ├── models
│   └── utils
│
└── assets
```

---

# 🗄 Database

The application uses **Supabase PostgreSQL**.

## Tables

- teachers
- students
- subjects
- subject_students
- attendance_logs

Student records include:

- face_embedding
- voice_embedding

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/ashish117840/SNAPCLASS.git

cd SNAPCLASS
```

---

## Create Virtual Environment

### Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

### Conda (Recommended)

```powershell
conda create -n snapclass python=3.10

conda activate snapclass
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Configure Secrets

Create

```
.streamlit/secrets.toml
```

Add

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"

SUPABASE_KEY="YOUR_SUPABASE_KEY"
```

---

## Run

```bash
streamlit run app.py
```

---

# 📸 Screenshots

> Add screenshots here.

```
Home Screen

Teacher Dashboard

Student Registration

Attendance Screen
```

---

# 🌐 Live Demo

## https://snapclass-ashish-main.streamlit.app/

---

# 🚧 Future Improvements

- Mobile Application
- Admin Dashboard
- QR Attendance
- Attendance Analytics
- PDF Reports
- Excel Export
- Email Notifications
- Multi-Class Support

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.

2. Create a feature branch.

3. Commit your changes.

4. Push the branch.

5. Open a Pull Request.

---

# 👨‍💻 Author

**Ashish Kumar**

GitHub

https://github.com/ashish117840

LinkedIn

https://www.linkedin.com/in/ashish-kumar7000

---

# ⭐ Support

If you like this project,

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

---

# 📜 License

This project is licensed under the MIT License.
