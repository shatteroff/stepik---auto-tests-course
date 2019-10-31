from selenium import webdriver
import time
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    first_name_element = browser.find_element_by_name("firstname")
    last_name_element = browser.find_element_by_name("lastname")
    email_element = browser.find_element_by_name("email")
    send_file_element = browser.find_element_by_id("file")
    but = browser.find_element_by_class_name("btn") 
    
    first_name_element.send_keys("firstname")
    last_name_element.send_keys("lastname")
    email_element.send_keys("email")    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')
    my_file = open(file_path, 'w') 
    # Закрываем файл
    my_file.close()    
    send_file_element.send_keys(file_path)
    

       
    but.click()
finally:
    time.sleep(10)

    browser.quit()
