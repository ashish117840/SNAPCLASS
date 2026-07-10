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

---

## ✨ Features

* 👨‍🏫 Teacher Dashboard
* 👨‍🎓 Student Management
* 📚 Subject Management
* 🤖 AI-Based Face Recognition
* 🎤 Voice Recognition Support
* ✅ Automatic Attendance Marking
* 📊 Attendance Logs
* ☁️ Supabase Database Integration
* 🌐 Responsive Streamlit Interface
* 🔒 Secure Authentication (Planned)

---

## 🛠️ Tech Stack

| Technology         | Purpose              |
| ------------------ | -------------------- |
| Python             | Backend Logic        |
| Streamlit          | Web Application      |
| Supabase           | Database & Backend   |
| PostgreSQL         | Data Storage         |
| OpenCV             | Face Detection       |
| Speech Recognition | Voice Recognition    |
| NumPy              | Numerical Operations |
| Pandas             | Data Processing      |

---

## 📂 Project Structure

```text
SNAPCLASS/
│
├── assets/
├── docs/
├── src/
│   ├── components/
│   ├── database/
│   ├── models/
│   ├── ui/
│   ├── utils/
│   └── services/
│
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
```

---

## 🚀 Live Demo

Experience the application here:

**https://snapclass-ashish-main.streamlit.app/**

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashish117840/SNAPCLASS.git
```

### 2. Move into the project

```bash
cd SNAPCLASS
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Streamlit Secrets

Create:

```text
.streamlit/secrets.toml
```

Example:

```toml
SUPABASE_URL="your_supabase_url"
SUPABASE_KEY="your_supabase_anon_key"
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 🗄️ Database

The project uses **Supabase PostgreSQL**.

Main tables include:

* Teachers
* Students
* Subjects
* Subject Students
* Attendance Logs

---

## 📸 AI Modules

### Face Recognition

* Face detection
* Face embedding generation
* Student identification

### Voice Recognition

* Voice embedding
* Speaker verification
* Attendance confirmation

---

## 📊 Future Improvements

* Email Notifications
* QR Code Attendance
* Multi-Class Support
* Attendance Analytics
* Export to Excel/PDF
* Admin Dashboard
* Mobile Application
* AI Performance Optimization

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 👨‍💻 Author

**Ashish Kumar**

* GitHub: https://github.com/ashish117840

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

---

## 📄 License

This project is licensed under the **MIT License**.
