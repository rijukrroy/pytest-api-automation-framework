<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/pytest-tested-green.svg" alt="Pytest">
  <img src="https://img.shields.io/badge/allure-report-ff69b4.svg" alt="Allure">
  <img src="https://img.shields.io/badge/jenkins-CI-blue.svg" alt="Jenkins">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="License">
</p>

# 🚀 API Test Automation Framework (Pytest + Jenkins + Allure)

A **scalable REST API Test Automation Framework** using **Python, Pytest, Requests**, fully integrated with **Allure Reporting** and **CI/CD pipelines (Jenkins / GitHub Actions)**.  

👉 Designed for **clients and teams** who want:
- Maintainable, modular automation code
- Rich reporting (history, categories, trends)
- Easy CI/CD setup (Jenkins or GitHub)

---

## ✨ Features
- ✅ **REST API Testing** with `requests`  
- ✅ **Schema Validation** via `jsonschema`  
- ✅ **Data-Driven Tests** (Excel: `openpyxl`)  
- ✅ **Allure Reports** with history, categories & trends  
- ✅ **CI/CD Ready** (Jenkins Pipeline & GitHub Actions)  
- ✅ **Scalable Structure** for real-world projects  

---

## ⚡ Quick Start

```bash
# 1. Clone repo
git clone https://github.com/rijukrroy/pytest-api-automation-framework.git
cd pytest-api-automation-framework

# 2. Setup virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests & generate Allure results
pytest -v --alluredir=allure-results

# 5. View Allure report
allure serve allure-results
📂 Project Structure
project-root/
├── tests/            # API test cases
├── libraries/        # Utility functions & helpers
├── conftest.py       # Pytest fixtures (setup/teardown)
├── reports/          # Allure raw results
├── allure-report/    # Static HTML report
├── docs/             # Screenshots & diagrams
├── requirements.txt  # Dependencies
└── pytest.ini        # Pytest configuration

🏗 CI/CD Integration
GitHub Actions

Sample workflow (.github/workflows/tests.yml):

name: API Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.x"
      - run: pip install -r requirements.txt
      - run: pytest --alluredir=allure-results
      - uses: actions/upload-artifact@v3
        with:
          name: allure-results
          path: allure-results

Jenkins Pipeline

Checkout repo

Install dependencies

Run tests with Pytest

Publish Allure Report

📊 Allure Reports

Trends & history: Track results over time

Categories: Classify failures (e.g. Assertion vs Network)

Executor info: See if run was local / Jenkins / GitHub

allure serve allure-results

📷 Screenshots
Jenkins Pipeline Stages

Allure Dashboard (Summary)

Test Suites & Results

Allure Trends (History)

🛠 Tech Stack

Language: Python 3.12

Framework: Pytest

API Client: Requests

Validation: JSON Schema

Reporting: Allure + JUnit XML

CI/CD: Jenkins Pipeline / GitHub Actions

📌 Note for Clients

This framework is ready-to-use and customizable for any REST API project.
It can be extended with UI (Selenium/Playwright) tests, DB validations, and integrated into any CI/CD environment.