from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_example(wd):
    wd.get("https://www.google.ru/")
    wd.find_element("name", "q").send_keys("webdriver")
    time.sleep(1)
    wd.find_element("name", "btnK").click()
    WebDriverWait(wd, 10).until(EC.title_is("webdriver - Поиск в Google"))
