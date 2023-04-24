from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # 1. Go to https://surveyrc.taxcreditco.com/automation-challenge
    page.goto('https://surveyrc.taxcreditco.com/automation-challenge')
    print("Step 1: Passed", end="\n")
    print("****************", end="\n")

    # 2. Fill all text fields under “Let’s begin by getting some basic information!” and click on Next button
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill("Jacob")
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill("Willis")
    page.get_by_label("Email Address").click()
    page.get_by_label("Email Address").fill("jakewill@jake.com")
    page.get_by_label("Street Address").click()
    page.get_by_label("Street Address").fill("Wilson street 45")
    page.get_by_label("City").click()
    page.get_by_label("City").fill("Minneapolis")
    page.get_by_label("Zip Code").click()
    page.get_by_label("Zip Code").fill("87654")
    page.get_by_role("button", name="Next").click()
    print("Step 2: Passed", end="\n")
    print("****************", end="\n")

    # 3. Answer “NO” to all questions under “At this time, please answer Yes or No to the following questions:” and click on Next button
    page.locator("#SurveyControl_Question11396").get_by_text("No").click()
    page.locator("#SurveyControl_Question11397").get_by_text("No").click()
    page.locator("#SurveyControl_Question914").get_by_text("No").click()
    page.locator("#SurveyControl_Question11361").get_by_text("No").click()
    page.locator("#SurveyControl_Question915").get_by_text("No").click()
    page.locator("#SurveyControl_Question1244").get_by_text("No").click()
    page.get_by_role("button", name="Next").click()
    print("Step 3: Passed", end="\n")
    print("****************", end="\n")

    # 4. Click on “Submit Form” button
    page.get_by_role("button", name="Submit form").click()
    print("Step 4: Passed", end="\n")
    print("****************", end="\n")

    # 5. Assert that you were redirected to “https://www.experian.com/employer-services”
    page.wait_for_timeout(5000)
    if 'https://www.experian.com/employer-services' in page.url:
        print("All Steps Passed", end="\n")
    
    browser.close()