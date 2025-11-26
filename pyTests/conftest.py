import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", help="browser_select"
    )

@pytest.fixture()
def browser_instance(request):
    browser_name = request.config.getoption("--browser-name")
    service_obj = Service()
    if browser_name =="chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name =="firefox":
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name =="edge":
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(4)

    yield driver
    driver.close()