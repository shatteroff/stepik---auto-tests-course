import math
import time

import pytest
from selenium import webdriver


def getAnswer():
    return math.log(int(time.time()))


link0 = "https://stepik.org/lesson/236895/step/1"
link1 = "https://stepik.org/lesson/236896/step/1"
link2 = "https://stepik.org/lesson/236897/step/1"
link3 = "https://stepik.org/lesson/236898/step/1"
link4 = "https://stepik.org/lesson/236899/step/1"
link5 = "https://stepik.org/lesson/236903/step/1"
link6 = "https://stepik.org/lesson/236904/step/1"
link7 = "https://stepik.org/lesson/236905/step/1"


# link_list = (link, link1, link2, link3, link4, link5, link6, link7)

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print('\nquit browser..')
    browser.quit()


@pytest.mark.parametrize('link_list', [link0, link1, link2, link3, link4, link5, link6, link7])
def test_enter_the_answer(browser, link_list):
    link = link_list
    browser.get(link)
    text_answer = browser.find_element_by_class_name('textarea')
    text_answer.send_keys(str(getAnswer()))
    button_submit = browser.find_element_by_class_name('submit-submission')
    button_submit.click()
    text_cor = browser.find_element_by_class_name('smart-hints__hint').text
    assert text_cor == 'Correct!', f'Should be Correct here, we have {text_cor}'
