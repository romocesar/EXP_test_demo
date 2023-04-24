# EXP_test_demo
A simple testing script to demonstrate Playwright capabilities for web automation

## Running Test
Install Python 
Install Playwright
Clone repo in local computer
Run test from your terminal (after navigating to projet folder) with the command: python main.py

## Test Notes
In the last step, the assertion of the URL has been modified so that it passes the test. Instead of an assertion on the URL string, there is an assertion in the substring of the URL. This was done because the website yielded an unexpected string at the end of the URL for example: "conf=714507"

Code snippet:
 if 'https://www.experian.com/employer-services' in page.url:
        print("All Steps Passed", end="\n")
