# TalentSphere Elevate

**An AI-powered recruitment platform and Applicant Tracking System (ATS)** that helps recruiters post jobs, rank candidates, and schedule interviews, while candidates build profiles, upload resumes, and apply to roles.

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

**Live demo:** <LIVE_DEMO_URL>

---

## Overview

TalentSphere Elevate connects two sides of hiring in one web application. Recruiters get a dashboard for managing job listings, ranking applicants against job requirements, scheduling interviews, and tracking hiring analytics. Candidates get a profile, resume upload with automated parsing, and a way to apply for jobs and follow their application status.

The project was built by a student team as a multi-milestone group project.

## Features

**For recruiters**
- Post and manage job listings (active / inactive)
- Candidate ranking using skill matching between resumes and job requirements
- Interview scheduling and tracking
- Analytics dashboard: jobs posted, applications received, candidates shortlisted and interviewed, weekly and monthly activity
- Company profile and account settings

**For candidates**
- Registration and login with role-based access
- Candidate profile with photo
- Resume upload with NLP-based parsing (PDF and Word)
- Job applications with status tracking
- Job recommendations

**Platform**
- Separate recruiter and candidate flows after login
- Request rate limiting and CORS configuration
- Environment-based configuration for secrets

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Python, Django 6 |
| NLP / resume parsing | spaCy (`en_core_web_sm`), PyMuPDF, pdfplumber, PyPDF2, python-docx |
| Frontend | Django templates, HTML, CSS, JavaScript |
| Database | SQLite (local development) |
| Utilities | python-dotenv, django-cors-headers, django-ratelimit |
| Deployment | Vercel |

## Project structure

```
TalentSphere-Elevate/
└── milestone1/backend/
    ├── accounts/          # registration, login, user roles
    ├── candidate/         # candidate dashboard, profiles, applications
    ├── recruiter/         # jobs, ranking, interviews, analytics, settings
    ├── recommendations/   # recommendation logic
    ├── backend/           # project settings, URLs, WSGI
    ├── templates/         # HTML templates
    ├── static/            # CSS, JS, images
    ├── demo_data.json     # demo recruiter account (fixture)
    ├── manage.py
    └── requirements.txt
```

## Getting started

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
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
# paste the printed value into .env as DJANGO_SECRET_KEY=...

# 5. Create the database
python manage.py migrate

# 6. Start the development server
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

### Load the demo account (optional)

```bash
python manage.py loaddata demo_data.json
```

Or simply use the **Register** page to create your own recruiter or candidate account.

## Demo account

| Role | Username | Password |
|---|---|---|
| Recruiter | `recruiter` | `recruit@4321` |

This is a shared demo account. Please do not enter real personal data.

## Deployment

The project is configured for [Vercel](https://vercel.com) using Django's WSGI entrypoint.

1. Import the repository in Vercel and set the **Root Directory** to `milestone1/backend`.
2. Add the environment variable `DJANGO_SECRET_KEY`.
3. Deploy.

On Vercel the database runs on a temporary SQLite file and is rebuilt from `demo_data.json` on startup. Accounts created on the live site and uploaded files do not persist between restarts. For permanent storage, connect a hosted PostgreSQL database (via `DATABASE_URL`) and external file storage.

<!--
## Screenshots
Add images to docs/screenshots/ and reference them here:
![Recruiter dashboard](docs/screenshots/recruiter-dashboard.png)
-->

## Team

| Name | Role | GitHub |
|---|---|---|
| _Your name_ | _e.g. Backend / Recruiter module_ | [@username](https://github.com/username) |
| _Teammate_ | _e.g. Candidate module_ | [@username](https://github.com/username) |
| _Teammate_ | _e.g. Resume NLP_ | [@username](https://github.com/username) |
| _Teammate_ | _e.g. Analytics_ | [@username](https://github.com/username) |

## License

Released under the [MIT License](LICENSE).
