import allure
import requests
from dotenv import load_dotenv
import os
import pytest

def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png,
                  name='Screenshot',
                  attachment_type=allure.attachment_type.PNG)


def add_xml(browser):
    xml_dump = browser.driver.page_source
    allure.attach(body=xml_dump,
                  name='XML screen',
                  attachment_type=allure.attachment_type.XML)

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

# def add_video(session_id):
#
#     bstack_session = requests.get(
#         f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
#         auth=(os.getenv("BSTACK_USER_NAME"), os.getenv("BSTACK_ACCESS_KEY")),
#     ).json()
#     print(bstack_session)
#     video_url = bstack_session['automation_session']['video_url']
#
#     allure.attach(
#         '<html><body>'
#         '<video width="100%" height="100%" controls autoplay>'
#         f'<source src="{video_url}" type="video/mp4">'
#         '</video>'
#         '</body></html>',
#         name='video recording',
#         attachment_type=allure.attachment_type.HTML,
#     )