from selenium.webdriver.common.by import By
import time


def test_example(wd):
    wd.get("http://localhost/litecart/admin/")
    wd.find_element("name", "username").send_keys("admin")
    wd.find_element("name", "password").send_keys("admin")
    time.sleep(1)
    wd.find_element("name", "login").click()
    time.sleep(1)
    wd.find_element(By.CLASS_NAME, "fa-sign-out").click()
