import allure

def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png,
                  name='Screenshot',
                  attachment_type=allure.attachment_type.PNG)