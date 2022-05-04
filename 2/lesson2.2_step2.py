from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = (browser.find_element_by_css_selector("#num1")).text
    y = (browser.find_element_by_css_selector("#num2")).text
    z= str(int(x)+int(y))
    select = Select(browser.find_element_by_tag_name("select")) 
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print_answer(browser)
    

finally:
    time.sleep(5)
    browser.quit()