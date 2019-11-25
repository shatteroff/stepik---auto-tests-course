import time


def test_add_to_card_button_enable(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_class_name('btn-add-to-basket')
