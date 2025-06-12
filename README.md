# Automated Web Application Testing 

This project demonstrates automated testing of a web application's login functionality using *Selenium WebDriver* and *PyTest. It includes both **positive and negative test cases*, screenshot capture on test failure, and a structured test framework.



## Project Structure

automated-testing-project/
│
├── tests/                            # Test scripts go here
│   ├── test_login.py                 # Test case for valid login
│   └── test_login_invalid.py         # Test case for invalid login
│
├── test_config/                      # Configuration files
│   └── config.py                     # Contains URL, email, password
│
├── reports/                          # (Optional) Allure reports output
│
├── screenshots/                      # Stores screenshots on test failure
│ 
│
├── .venv/                            # Virtual environment (auto-created)
│
├── conftest.py                       # Shared fixtures (e.g., setup_browser)
│
├── requirements.txt                  # List of dependencies
│
├── README.md                         # Project description and usage
│
└── .gitignore                        # (Optional) Ignore unnecessary files



##  Features

-  Tests valid and invalid login scenarios
-  Takes screenshots on test failure
-  Easy-to-edit config for URL and credentials
-  PyTest-based test runner
-  Allure Reporting (optional)
-  Clean folder structure



##  Tech Stack

- *Language*: Python
- *Framework*: PyTest
- *Automation Tool*: Selenium WebDriver
- *Reporting*: Allure (optional)
- *IDE*: PyCharm



##  Setup Instructions

1. Clone the Repository

bash
git clone https://github.com/your-username/automated-testing-project.git
cd automated-testing-project

2. Create a Virtual Environment (Optional but Recommended)

python -m venv .venv
source .venv/bin/activate     # On Linux/macOS
.venv\Scripts\activate        # On Windows

3. Install Dependencies

pip install -r requirements.txt



## Running the Tests

Run All Tests:

pytest

Run Specific Test:

pytest tests/test_login.py




## Screenshot on Failure

If a test fails, a screenshot will be saved in the screenshots/ folder automatically.




## Generating Allure Report (Optional)

If you have Allure installed:

allure serve reports/



## Credentials & Configuration

Edit the file test_config/config.py to change:

URL = "https://practicetestautomation.com/practice-test-login/"
USERNAME = "Student"
PASSWORD = "Password123"




Author

Gade Akshaya

https://www.linkedin.com/in/akshayatejomandira/




Show Your Support

If you liked this project, consider giving it a ⭐ on GitHub or using it as part of your internship showcase!




