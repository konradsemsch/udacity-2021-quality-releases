# #!/usr/bin/env python

import os
import logging
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

def setup_logging(
    log_output_filename: str = "selenium-tests",
    path_log_output: str = "logs/tests/selenium",
    level=logging.INFO,
) -> None:
    Path(path_log_output).mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(message)s",
        handlers=[
            logging.FileHandler(
                os.path.join(
                    path_log_output, f"{log_output_filename}.log"
                )
            ),
            logging.StreamHandler(),
        ],
    )

def login(driver, user, password):
    """Login into the website with given user an password"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    logger.info(f"Successfully logged into the website with user: {user} and password: {password}")

def add_to_cart(driver, n):
    """Add items to cart sequentially using the item number."""
    counter = 0
    for i in range(n):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name large_size']").text
        logger.info(f"Added {product} to cart")
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
        logger.info(f"Removed {product} from cart")
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
        counter += 1
    assert counter == n
    return counter

if __name__ == "__main__":
    setup_logging()

    logger.info("Starting the browser...")
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome( options=options)
    logger.info("Browser started successfully. Navigating to the demo page to login.")

    # Starting test-suite functions
    logger.info("---- Login Test -----")
    login(driver=driver, user="standard_user", password="secret_sauce")
    logger.info("---- Add to Cart Test -----")
    n_items_added = add_to_cart(driver, 6)
    logger.info("---- Remove from Test -----")
    n_items_removed = remove_from_cart(driver, n_items_added)
    assert n_items_added == n_items_removed

