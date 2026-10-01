# Git_and_GitHub_KrishnaBhatt
DevOps assignment demonstrating Git and GitHub workflow with Flask, MongoDB, branching, merging, conflict resolution, reset, and rebase.
# Git & GitHub — DevOps Assignment

A Flask + MongoDB project created for practising the complete Git and GitHub workflow.

## Features

* Flask `/api` endpoint
* To-Do frontend
* `/submittodoitem` POST API
* MongoDB database integration
* Item ID, UUID and Hash fields
* Git branching and merging
* Conflict resolution
* Sequential commits
* Git reset
* Git rebase

## Tech Stack

* Python
* Flask
* MongoDB
* Git & GitHub
* HTML, CSS, JavaScript

## Run Locally

```bash
git clone git@github.com:krishnabhatt/Git_and_GitHub_KrishnaBhatt.git
cd Git_and_GitHub_KrishnaBhatt

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

API:

```text
http://127.0.0.1:5000/api
```

## Project Structure

```text
Git_and_GitHub_KrishnaBhatt/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── data/
    └── sample.json
```

## Assignment

This project was developed as part of a DevOps assignment to demonstrate practical Git and GitHub concepts including:

* SSH authentication
* Branching
* Merging
* Conflict resolution
* Commit history
* Git reset
* Git rebase
* GitHub repository management
