from selenium import webdriver
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)    
  
    but = browser.find_element_by_class_name("btn")   
    but.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    text_edit = browser.find_element_by_id("answer")
    text_edit.send_keys(y)
    
    but = browser.find_element_by_class_name("btn")
    but.click()
    
    
finally:
    time.sleep(10)

    browser.quit()
