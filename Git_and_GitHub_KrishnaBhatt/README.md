# Git & GitHub — DevOps Assignment

Flask + MongoDB project created for practising the complete Git workflow.

## Features
- Flask `/api` endpoint
- To-Do frontend
- `/submittodoitem` POST API
- MongoDB storage
- Item ID, UUID and Hash fields
- Git branching, merging, reset and rebase workflow

## Setup

```bash
python -m venv venv
# Windows
venv\Scripts\activate

pip install -r requirements.txt
copy .env.example .env
python app.py
```

Make sure MongoDB is running locally.

Open:
- http://127.0.0.1:5000/
- http://127.0.0.1:5000/api

## GitHub
Create a GitHub repository and add its SSH remote:

```bash
git remote add origin git@github.com:YOUR_USERNAME/Git_and_GitHub_KrishnaBhatt.git
git push -u origin main
```
