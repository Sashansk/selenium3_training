import pytest
from selenium import webdriver


@pytest.fixture(scope= "session")
def wd(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd