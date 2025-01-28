from selene import have, browser
from allure import step


def test_search():
    browser.open('/')

    with step('Type search'):
        browser.element('#searchInput').type('AppImage')

    with step('Verify content found'):
        results = browser.all('.suggestion-link')
        results.should(have.size_greater_than(0))
        results.should(have.texts('AppImage'))  # Изменено на texts