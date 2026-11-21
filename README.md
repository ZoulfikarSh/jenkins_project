# Lab 10 – Jenkins CI/CD Pipeline for Python

**Student:** Zoulfikar Shokor

A small Python app built, checked and deployed by a Jenkins pipeline.

## Pipeline stages (`Jenkinsfile_Zoulfikar_Shokor`)

1. **Setup** – creates a virtual environment and installs `requirements.txt`
2. **Lint** – `flake8` on the app, deploy script and tests
3. **Test** – `pytest` with a JUnit report
4. **Coverage** – `coverage.py`; fails below 80%, archives XML and HTML reports
5. **Security Scan** – `bandit`; fails on medium/high findings, archives a JSON report
6. **Deploy** – `deploy.py` copies the app to `~/jenkins_deploy/python-ci-cd` and runs a smoke test

The Jenkinsfile runs on Linux (`sh`) and Windows (`bat`) agents.

## Jenkins job setup

- New Item → **Pipeline** named `Python-CI-CD`
- Pipeline → **Pipeline script from SCM** → Git → this repository's URL
- Branch: `*/main`
- Script Path: `Jenkinsfile_Zoulfikar_Shokor`

## Run locally

```
python -m venv venv
venv/bin/pip install -r requirements.txt      # Windows: venv\Scripts\pip
python -m pytest
python -m coverage run -m pytest && python -m coverage report
python -m bandit app.py deploy.py
python deploy.py
```
