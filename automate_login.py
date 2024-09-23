# automate_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuration
LOGIN_URL = "http://127.0.0.1:5000/login"
USERNAME = "Maoz"  # Replace with your registered username
PASSWORD = "1234"  # Replace with your registered password

def automate_login():
    # Initialize the WebDriver (Chrome)
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH

    try:
        # Open the login page
        driver.get(LOGIN_URL)
        print("Opened login page.")

        # Wait for the page to load
        time.sleep(2)

        # Find the username and password fields
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Enter the credentials
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        print("Entered username and password.")

        # Submit the form
        password_field.send_keys(Keys.RETURN)
        print("Submitted the login form.")

        # Wait for the home page to load
        time.sleep(3)

        # Optionally, verify login success
        if "Welcome" in driver.page_source:
            print("Login successful!")
        else:
            print("Login failed.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    automate_login()
