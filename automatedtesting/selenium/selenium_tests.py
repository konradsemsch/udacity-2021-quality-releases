# #!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


def login(driver, user, password):
    """Login into the website with given user an password"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    print(f"Successfully logged into the website with user: {user} and password: {password}")

def add_to_cart(driver, n):
    """Add items to cart sequentially using the item number."""
    counter = 0
    for i in range(n):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name large_size']").text
        print(f"Added {product} to cart")
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
        counter += 1
    assert counter == n
    return counter

def remove_from_cart(driver, n):
    """Remove items from cart sequentially using the item number."""
    counter = 0
    for i in range(n):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_secondary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name large_size']").text
        print(f"Removed {product} from cart")
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
        counter += 1
    assert counter == n
    return counter

if __name__ == "__main__":
    print("Starting the browser...")
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print("Browser started successfully. Navigating to the demo page to login.")

    # Starting test-suite functions
    login(driver=driver, user="standard_user", password="secret_sauce")
    n_items_added = add_to_cart(driver, 6)
    n_items_removed = remove_from_cart(driver, n_items_added)
    assert n_items_added == n_items_removed

