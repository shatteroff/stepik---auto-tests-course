from selenium import webdriver
import time
import math

def sum(x,y): 
    return int(x)+int(y)


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    print (x_element.text)
    print (y_element.text)
    z = sum(x_element.text,y_element.text)    
    # m = z(x_element.text,y_element.text) 
    print (z)    


    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(z)) # ищем элемент с текстом "Python"
    
    but = browser.find_element_by_class_name("btn")
    but.click()
   
finally:
    time.sleep(10)

    browser.quit()
