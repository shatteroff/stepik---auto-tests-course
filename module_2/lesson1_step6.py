from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
    
time.sleep(10)

browser.quit()
