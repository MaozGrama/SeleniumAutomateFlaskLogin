Here’s a quick **README** for your project:

---

# Flask Login Selenium Project

This project is a simple web application built using **Flask**. It features a basic login system where users can register and log in. Additionally, Selenium is used to automate the login process by filling in the login credentials.

## Features
- User registration with password hashing
- User login functionality
- Automated login using Selenium

## Technologies Used
- **Flask**: Micro web framework for building the application
- **Flask-SQLAlchemy**: ORM for handling SQLite database
- **Flask-Login**: User session management
- **Selenium**: Browser automation for testing the login process
- **Jinja2**: Template engine used in Flask for rendering HTML pages
- **Werkzeug**: Password hashing and security utilities
- **SQLite**: Database used for storing user credentials

## Installation

### Prerequisites:
- Python 3.x
- `pip` (Python package manager)
- WebDriver for Selenium (e.g., ChromeDriver)

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd flask_login_selenium
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. The application should be running on `http://127.0.0.1:5000/`.

### Selenium Setup:
1. Download the appropriate WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)).
2. Ensure the WebDriver is in your system’s PATH or provide the full path when initializing Selenium in your script.

## File Structure

```
flask_login_selenium/
│
├── app.py                    # Main application script
├── models.py                 # Database models
├── forms.py                  # Registration and login forms
├── templates/
│   ├── login.html            # Login page
│   ├── register.html         # Registration page
├── static/                   # Static files (CSS, JS, images)
├── venv/                     # Virtual environment (optional)
└── README.md                 # This README file
```

## Automated Login using Selenium

1. Update the Selenium script in `app.py` with your browser’s WebDriver path.
2. Run the Selenium script to automate the login process.

### Example Code:
```python
from selenium import webdriver

driver = webdriver.Chrome(executable_path='path/to/chromedriver')
driver.get("http://127.0.0.1:5000/login")

# Automating the login process
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")
login_button = driver.find_element_by_name("submit")

username_input.send_keys("your_username")
password_input.send_keys("your_password")
login_button.click()
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

For any questions or support, feel free to contact the author at [MaozGram@example.com]."# SeleniumAutomateFlaskLogin" 
