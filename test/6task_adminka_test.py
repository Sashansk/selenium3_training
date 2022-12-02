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
    menu = wd.find_elements(By.CSS_SELECTOR, "#app- span.name:nth-child(1)")
    list = menu.wd.find_element(By.CSS_SELECTOR, "#doc-template > a > span")
    list.find_element(By.TAG_NAME, "h1")
    wd.find_element(By.CSS_SELECTOR, "#doc-logotype > a > span").click()
    wd.find_element(By.TAG_NAME, "h1")
    wd.find_element(By.CSS_SELECTOR, ("#app- > a > span.name")[1]).click()
    time.sleep(3)
    wd.find_element(By.CSS_SELECTOR, "#doc-catalog > a > span").click()
    wd.find_element(By.TAG_NAME, "h1")
    wd.find_element(By.CSS_SELECTOR, "#doc-product_groups > a > span").click()
    wd.find_element(By.TAG_NAME, "h1")
    #p = page.find.element(By.CSS_SELECTOR = "#content > h1").
    #a = elem.find_element()
    time.sleep(4)
    #    wd.find_element("id", "doc-template").click()
    # wd.find_element("id", "doc-logotype").click()


