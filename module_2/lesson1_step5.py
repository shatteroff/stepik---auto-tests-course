from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
    
    
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

text_edit = browser.find_element_by_id("answer")
text_edit.send_keys(y)


check_box=browser.find_element_by_id("robotCheckbox")
check_box.click()

radio_but = browser.find_element_by_id("robotsRule")
radio_but.click()

but = browser.find_element_by_class_name("btn")
but.click()

time.sleep(10)

browser.quit()
