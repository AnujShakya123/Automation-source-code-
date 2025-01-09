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

