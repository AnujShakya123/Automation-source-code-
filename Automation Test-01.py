

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Constants
URL = "https://ecspro-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"

# Setup WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed and added to PATH
driver.get(URL)
driver.maximize_window()

try:
    # Step 01: Login
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/form/div[1]/input").send_keys(USERNAME)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/form/div[2]/input").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/form/div[5]/button").click()

    # Wait for home page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-home/div/div[2]/mat-card[8]/p[3]"))
    )

    # Step 02: Navigate to Package Types
    driver.find_element(By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-home/div/div[2]/mat-card[8]/p[2]/span").click()

    # Wait for Package Types page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/app-header/mat-toolbar/button[2]/span[1]/mat-icon"))
    )

    # Step 03: Click Add Manually
    driver.find_element(By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/app-header/mat-toolbar/button[2]/span[1]/mat-icon").click()

    # Step 04: Fill package details
    name = "Anuj_Shakya"
    length = random.randint(1, 20)
    width = random.randint(1, 20)
    height = random.randint(1, 20)

    # Fill in package name
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[1]/section[1]/div/mat-form-field/div/div[1]/div/input"))
    )
    driver.find_element(By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[1]/section[1]/div/mat-form-field/div/div[1]/div/input").send_keys(name)

    # Fill in dimensions (adjust field locators if necessary)
    driver.find_element(By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[2]/section[1]/div/mat-form-field/div/div[1]/div/input").send_keys(str(length))
    driver.find_element(By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[2]/section[2]/div/mat-form-field/div/div[1]/div/input").send_keys(str(width))
    driver.find_element(By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/perfect-scrollbar/div/div[1]/mat-card/form/div/div[2]/section[3]/div/mat-form-field/div/div[1]/div/input").send_keys(str(height))


   # Save the package
    driver.find_element(By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[2]/app-package-type-manage/mat-toolbar/button/span[1]/mat-icon").click()

    # Verify success
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/div/app-dashboard/div/div[1]/app-package-type-list/perfect-scrollbar/div/div[1]/mat-card[1]/div[1]"))
    )
    print(f"Package '{name}' added successfully with dimensions {length}x{width}x{height}.")

    # Step 06: Logout
     # Locate and click on the three-dot menu
    three_dot_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidenav/mat-sidenav-container/mat-sidenav-content/app-header/mat-toolbar/button[9]/span[1]/mat-icon"))  # Replace with actual locator
    )
    three_dot_menu.click()

       # Step 2: Wait for the Logout button to be clickable
    logout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/div/div/div/button[6]"))  # Replace with actual XPATH
    )

    # Step 3: Scroll into view (optional) and click
    driver.execute_script("arguments[0].scrollIntoView(true);", logout_button)
    time.sleep(1)  # Allow rendering time
    logout_button.click()
 
    print("Logged out successfully.")


finally:
    # Close the browser
    driver.quit()