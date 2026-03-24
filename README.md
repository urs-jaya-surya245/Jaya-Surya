# Selenium + Manual Testing Project (GitHub Ready)

This repository is a **starter QA project** that combines:

1. **Manual testing artifacts** (test plan, test cases, bug report template)
2. **Selenium automation starter** using Python + Pytest

It is designed so you can upload directly to GitHub and use it as a portfolio/testing project.

---

## Project Structure

```text
.
├── README.md
├── .gitignore
├── manual-testing
│   ├── TEST_PLAN.md
│   ├── TEST_CASES.md
│   └── BUG_REPORT_TEMPLATE.md
└── selenium-automation
    ├── requirements.txt
    ├── pytest.ini
    ├── pages
    │   └── login_page.py
    └── tests
        └── test_login.py
```

---

## Manual Testing Scope

Target sample app: [SauceDemo](https://www.saucedemo.com/)

Use the manual docs under `manual-testing/` to:
- Execute functional tests
- Track expected vs actual results
- Log defects in a standard format

---

## Selenium Automation Setup (Python)

### 1) Create virtual environment

```bash
cd selenium-automation
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate   # Windows PowerShell
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run tests

```bash
pytest -v
```

> The tests use Selenium Manager to auto-resolve browser driver with recent Selenium versions.

---

## Suggested GitHub Upload Steps

```bash
git init
git add .
git commit -m "Add Selenium + manual testing starter project"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

---

## Extend This Project

- Add API tests (Postman/Newman or pytest + requests)
- Add CI with GitHub Actions
- Add cross-browser test matrix
- Add test reports (Allure / HTML reports)

