# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def login(driver, user, password):
    """Login into the website with given user an password"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    print(f"Successfully logged into the website with user: {user} and password: {password}")

if __name__ == "__main__":
    print("Starting the browser...")
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print("Browser started successfully. Navigating to the demo page to login.")

    # Starting test-suite functions
    login(driver=driver, user="standard_user", password="secret_sauce")

