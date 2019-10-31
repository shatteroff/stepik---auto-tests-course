from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    text_edit = browser.find_element_by_id("answer")
    text_edit.send_keys(y)


    check_box=browser.find_element_by_id("robotCheckbox")
    check_box.click()

    radio_but = browser.find_element_by_id("robotsRule")
    radio_but.click()

    but = browser.find_element_by_class_name("btn")
    but.click()
finally:
    time.sleep(10)

    browser.quit()
