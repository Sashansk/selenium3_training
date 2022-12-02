from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def test_adminka (wd):
    wd.get("http://localhost/litecart/admin/")
    wd.find_element("name", "username").send_keys("admin")
    wd.find_element("name", "password").send_keys("admin")
    time.sleep(1)
    wd.find_element("name", "login").click()
    time.sleep(1)
    i = 0
    j = 0
    while i < len(menu):
        menu = wd.find_elements(By.CSS_SELECTOR, "#app- span.name:nth-child(1)") #Нашли все элементы меню
        menu[i].click() #зашли в меню
        while j < len(list):
            list[j] = menu[i].wd.find_elements(By.CSS_SELECTOR, "#doc-template (тут должен вернуться список подменю) > a > span:nth-child(1)") #выбрали элементы подменю
            list[j].click() # перешли на выбранную страницу подменю
            list[j].find_element(By.TAG_NAME, "h1") # находим тег с заголовком
            j += 1
        i += 1
