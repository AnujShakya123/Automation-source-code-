Overview

This project automates the process of managing package types in the ECSPro application using Selenium WebDriver. The program logs into the application, navigates to the "Package Types" section, adds a new package manually, verifies its addition, and finally logs out. Additionally, the script includes functionality to verify if the package was successfully deleted.

Design Decisions

Modularity: The script is divided into logical steps (e.g., Login, Navigation, Form Submission) to make it easy to follow and debug.

Dynamic Data: Random values for package dimensions ensure the test is not static and simulates real-world usage.

Explicit Waits: Used WebDriverWait with explicit conditions to handle dynamic loading of web elements, ensuring robustness.

Error Handling: Wrapped the test in a try-finally block to guarantee that the browser closes even if an error occurs.

Approach

Setup and Login: The script initializes the WebDriver, maximizes the browser window, and performs a login using predefined credentials.

Navigation: It navigates to the "Package Types" section of the application.

Package Creation: A new package is created with a unique name and randomly generated dimensions.

Verification: Ensures the package appears in the list after creation.

Logout: Logs out of the application cleanly.

Deletion Verification: Re-logs into the application and verifies whether the package is deleted.

Prerequisites

Install Python 3.x.

Install the required dependencies using the following command:

pip install selenium

Download the ChromeDriver executable that matches your Google Chrome version and add it to your system PATH.

Steps to Execute

Clone or download this repository.

Open a terminal in the project directory.

Run the script using the command:

python selenium_automation.py

Observe the console output for the test results:

Confirmation of package addition.

Confirmation of successful logout.

Verification of package deletion.

The browser will close automatically after the test completes.


