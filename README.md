# 🐍 Pytest API Automation Framework

A simple yet scalable **API Automation Framework** built using **Pytest**, **Requests**, and **Allure Reports**.  
This framework demonstrates best practices for REST API testing, including data-driven tests, schema validation, logging, and reporting.

---

## 🚀 Features
- API test automation with **pytest**
- Data-driven testing from Excel (via `openpyxl`)
- JSON Schema validation (`jsonschema`)
- Centralized test configuration with `pytest.ini`
- **Allure Reports** integration for beautiful reporting
- Fixtures for base URL, headers, and reusable setup
- Built-in **logging** in `conftest.py` for better debugging
- Extensible structure for scaling to multiple APIs

---

## 🛠️ Tech Stack
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)  
![Requests](https://img.shields.io/badge/Requests-20232A?style=for-the-badge&logo=python&logoColor=white)  
![Allure](https://img.shields.io/badge/Allure%20Reports-FF69B4?style=for-the-badge&logo=allure&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📂 Project Structure
```bash
pytest-api-automation-framework/
├── tests/
│   └── test_users.py        # Example API test
├── utils/
│   └── api_client.py        # Helper for API requests
├── libraries/
│   └── util.py              # Excel reader, reusable utilities
├── reports/                 # Allure results directory
├── conftest.py              # Fixtures (base_url, headers, logging)
├── requirements.txt         # Project dependencies
├── pytest.ini               # Config (env variables, pytest options)
└── README.md                # Documentation

---
```bash
## ⚙️ Setup & Installation

**Clone the repo:**
```bash
git clone https://github.com/rijukrroy/pytest-api-automation-framework.git
cd pytest-api-automation-framework

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run tests:

pytest tests/test_users.py


Generate Allure report:

pytest --alluredir=reports/allure-results
allure serve reports/allure-results