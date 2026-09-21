<div align="center">

# 🌐 TalentSphere Elevate

**AI-Powered Recruitment Platform & Applicant Tracking System**

[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)
[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Vercel-black?style=for-the-badge)](https://your-live-demo-url.vercel.app)

![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django_6-092E20?style=flat-square&logo=django&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)

> An AI-powered recruitment platform that connects recruiters and candidates in one application. Recruiters post jobs, rank applicants using NLP skill matching, schedule interviews, and track hiring analytics. Candidates build profiles, upload resumes with automated parsing, and apply to roles.

</div>

---

## 🎯 Overview

TalentSphere Elevate connects both sides of hiring in one web application.

**Recruiters** get a dashboard for managing job listings, ranking applicants against job requirements, scheduling interviews, and tracking hiring analytics.

**Candidates** get a profile, resume upload with automated NLP parsing, job application tracking, and job recommendations.

---

## ✨ Features

### 👔 For Recruiters
- Post and manage job listings (active / inactive)
- Candidate ranking using NLP skill matching between resumes and job requirements
- Interview scheduling and tracking
- Analytics dashboard — jobs posted, applications received, candidates shortlisted and interviewed, weekly and monthly activity
- Company profile and account settings

### 👤 For Candidates
- Registration and login with role-based access
- Candidate profile with photo
- Resume upload with NLP-based parsing (PDF and Word)
- Job applications with status tracking
- Job recommendations

### 🔧 Platform
- Separate recruiter and candidate flows after login
- Request rate limiting and CORS configuration
- Environment-based configuration for secrets

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Django 6 |
| NLP / Resume Parsing | spaCy (`en_core_web_sm`), PyMuPDF, pdfplumber, PyPDF2, python-docx |
| Frontend | Django Templates, HTML, CSS, JavaScript |
| Database | SQLite (local development) |
| Utilities | python-dotenv, django-cors-headers, django-ratelimit |
| Deployment | Vercel |

---

## 📁 Project Structure

```
TalentSphere-Elevate/
└── milestone1/backend/
    ├── accounts/          # Registration, login, user roles
    ├── candidate/         # Candidate dashboard, profiles, applications
    ├── recruiter/         # Jobs, ranking, interviews, analytics, settings
    ├── recommendations/   # Recommendation logic
    ├── backend/           # Project settings, URLs, WSGI
    ├── templates/         # HTML templates
    ├── static/            # CSS, JS, images
    ├── demo_data.json     # Demo recruiter account (fixture)
    ├── manage.py
    └── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or newer
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Sriveena47/TalentSphere-Elevate.git
cd TalentSphere-Elevate/milestone1/backend

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
# Paste the printed value into .env as DJANGO_SECRET_KEY=...

# 5. Create the database
python manage.py migrate

# 6. Start the development server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

### Load Demo Account (optional)

```bash
python manage.py loaddata demo_data.json
```

Or use the **Register** page to create your own recruiter or candidate account.

---

## 🔑 Demo Account

| Role | Username | Password |
|---|---|---|
| Recruiter | recruiter | recruit@321 |

> This is a shared demo account. Please do not enter real personal data.

---

## 🌐 Deployment

The project is configured for Vercel using Django's WSGI entrypoint.

1. Import the repository in Vercel and set the **Root Directory** to `milestone1/backend`
2. Add the environment variable `DJANGO_SECRET_KEY`
3. Deploy

> On Vercel the database runs on a temporary SQLite file and is rebuilt from `demo_data.json` on startup. For permanent storage, connect a hosted PostgreSQL database (via `DATABASE_URL`) and external file storage.

---

## 👥 Team

| Name | Role |
|---|---|
| Pavan Subramanyam Sai Kumar Dangeti | Backend / Recruiter Module |
| Sriveena | Candidate Module |
| Teammate | Resume NLP |
| Teammate | Analytics |

---

## 🗺️ Roadmap

- [ ] PostgreSQL migration for production
- [ ] AI-powered cover letter suggestions
- [ ] Real-time interview notifications
- [ ] Mobile-responsive UI
- [ ] CI/CD pipeline

---

## 📄 License

Released under the [MIT License](./LICENSE).

---

<div align="center">

🌐 **TalentSphere Elevate — Smarter hiring, powered by AI.**

*Built as a multi-milestone group project.*

</div>
