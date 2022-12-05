from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_country(wd):
    wd.get("http://localhost/litecart/admin/")
    wd.find_element("name", "username").send_keys("admin")
    wd.find_element("name", "password").send_keys("admin")
    time.sleep(1)
    wd.find_element("name", "login").click()
    wd.find_element(By.CSS_SELECTOR, "#app-:nth-child(3)").click() # нашли страну из меню
    '''
    list1 = []
    lists = wd.find_elements(By.CSS_SELECTOR, ".dataTable .row > td:nth-child(5)") #выбрали столбец с названием стран из таблицы
    for list in lists:
        l1 = list.get_attribute("innerText") # Выбрали значение страны
        list1.append(l1)
    list2 = sorted(list1)
    assert list1 == list2 # Проверка совпадения списков
    '''
    geos = wd.find_elements(By.CSS_SELECTOR, ".dataTable .row > td:nth-child(6)") #выбрали столбец с количеством зон из таблицы
    for geo in geos:
        g1 = geo.get_attribute("innerText")
        if g1 != '0':
            print(str(g1))
            #wd.find_element(By.CSS_SELECTOR, ".dataTable .row > td:nth-child(7)").click()
    #list2 = sorted(list)
