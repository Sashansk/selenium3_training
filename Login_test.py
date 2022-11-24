import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def wdrv(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(wdrv, name="admin", pwd="admin"):
    wdrv.get("http://localhost/litecart/admin/")
    wdrv.find_element("name", "username").send_keys(name)
    wdrv.find_element("name", "password").send_keys(pwd)
    time.sleep(1)
    wdrv.find_element("name", "login").click()
    time.sleep(1)
    wdrv.find_element(By.CLASS_NAME, "fa-sign-out").click()
