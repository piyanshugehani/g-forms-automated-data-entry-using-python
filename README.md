Google Form Automation Script

Overview: This script automates the process of logging into a Google account, navigating to a specified Google Form, and filling out the form with data extracted from an Excel sheet. The script is written in Python and uses Selenium, PyAutoGUI, and Pandas for automation and data handling.

Features:
- Logs into a Google account using pre-defined credentials.
- Navigates to a Google Form URL.
- Reads data from an Excel file and automatically fills out the form.
- Supports batch processing of multiple entries from the Excel file.

Requirements:
- Python 3.x
- Google Chrome
- Chromedriver (ensure it matches your Chrome version)

Python Libraries:
- selenium
- pyautogui
- pandas
You can install the necessary libraries using:
pip install selenium pyautogui pandas

Setup Instructions:
- Download and Install Chromedriver: Ensure that chromedriver is installed and its version matches your Google Chrome installation. You can download it from here.

- Prepare the Excel File: Place an Excel file (data2.xlsx) in the same directory as the script.

- Ensure the file contains the necessary columns:
Name: The name to be filled in the form.
NUMBER: The contact number or other relevant details.

- Update the Script: Modify the following in the script
username: Set this to your Google account username.
password: Set this to your Google account password.
link: Update this with the Google Form URL you want to automate.

- Run the Script: python script.py
- Enter the start and end row numbers from the Excel file when prompted.
  
Important Notes:
- Security Warning: The script currently has hardcoded credentials for logging into Google. Consider using more secure methods like environment variables or prompting for credentials at runtime.
- Captcha: Google might trigger captcha challenges if it detects automated behavior. Be aware that this script may not always work due to such protections.
- Excel Structure: Ensure your Excel file is correctly formatted, with no missing or extra columns.
- License: This project is licensed under the MIT License.
