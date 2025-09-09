# API Test Automation Framework (Pytest + Jenkins + Allure)

This project is a **REST API test automation framework** built with Python, Pytest, and Requests, fully integrated with **Jenkins CI/CD** and **Allure reporting**.

The goal is to provide a **scalable, maintainable, and CI/CD-ready automation setup** that can be reused for professional API testing projects.

---

## ✅ Features
- **Test Framework:** Built on [Pytest](https://docs.pytest.org/) (simple, powerful, extensible).  
- **HTTP Requests:** Uses Python [requests](https://docs.python-requests.org/) for REST API calls.  
- **Schema Validation:** JSON Schema validation using [jsonschema](https://pypi.org/project/jsonschema/).  
- **Data-Driven Testing:** External test data managed via Excel ([openpyxl](https://openpyxl.readthedocs.io/)).  
- **CI/CD Integration:** Automated pipeline via **Jenkins** with GitHub integration.  
- **Test Reports:** Rich **Allure Reports** + **JUnit XML test results**.  
- **Scalable Structure:** Organized modules for utilities, schemas, tests, and reports.  

---

## 📂 Project Structure
```
pytest-api-automation-framework/
│── libraries/ # Utility functions
│ └── util.py # Excel reader, helpers
│
│── schemas/ # JSON schemas for validation
│ └── user_schema.json
│
│── tests/ # Test cases
│ └── test_users.py
│
│── requirements.txt # Python dependencies
│── Jenkinsfile # Jenkins pipeline definition
│── README.md # Project documentation
```


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/rijukrroy/pytest-api-automation-framework.git

cd pytest-api-automation-framework

2️⃣ Create & activate Python virtual environment

python3 -m venv venv

source venv/bin/activate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         # Linux/Mac

venv\Scripts\activate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      # Windows

3️⃣ Install dependencies

pip install --upgrade pip

pip install -r requirements.txt

4️⃣ Run tests locally

pytest --alluredir=allure-results --junitxml=allure-results/junit-results.xml

🏗 Jenkins Pipeline Setup

Open Jenkins → New Item → Pipeline.

Connect GitHub repo:

Repository URL: https://github.com/rijukrroy/pytest-api-automation-framework.git

Branch: main

Jenkins automatically detects the Jenkinsfile.

Pipeline stages:

✅ Checkout code

✅ Setup Python virtual environment

✅ Install dependencies

✅ Run tests with Pytest

✅ Archive results (JUnit XML)

✅ Generate & publish Allure Report

📊 Allure Reporting
Local Machine
allure serve allure-results

In Jenkins

Allure report is generated automatically in the pipeline.

View the report from Jenkins job → Build Artifacts → Allure Report.

🛠 Tech Stack

Language: Python 3.12

Test Framework: Pytest

HTTP Client: Requests

Validation: JSONSchema

Reporting: Allure, JUnit XML

CI/CD: Jenkins Pipeline (Groovy, Declarative)

📷 Screenshots (To Be Added)

Jenkins pipeline stages

Allure report dashboard

Test results summary

## 📊 Allure Reports

Below are sample reports generated using **Allure** for this project:

### Overview
![Allure Overview](docs/allure_overview.png)

### Test Suites
![Allure Suites](docs/allure_suites.png)

### Trends
![Allure Trends](docs/allure_trends.png)

### Jenkins Stage View
![Stage View](docs/Stage_view.png)
