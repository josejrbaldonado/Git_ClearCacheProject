import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Reside all the fixtures for set up and tear down  that will be use in all test cases.
# The calling of the servers to be tested is initialized here.
# SOON:
# Test case running in multiple browser
# Data test driven


@pytest.fixture(scope="class")
def setup(request):
    browser = Service("C:/Users/JOSEJR.BALDONADO/OneDrive - DTN, LLC/Documents/chromedriver.exe")
    driver = webdriver.Chrome(service=browser)
    #driver.get("http://agonline-app-pre07.dtn.com:8080/agriculture/web/ag/home")
    driver.get("http://agonline-app-dev03.dtn.com:8080/agriculture/web/ag/home")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

    # This SYNTAX will be use if you want ther chrome driver to be downloaded automatically.
    # browser = Service()
    # driver = webdriver.Chrome(service=browser)











# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )


# @pytest.fixture(scope="class")
# def setup(request):
#     browser_name=request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         browser = Service()
#         driver = webdriver.Chrome(service=browser)
#     elif browser_name == "firefox":
#         browser = Service()
#         driver = webdriver.Firefox(service=browser)
#
#         driver.get("http://agonline-app-pre07.dtn.com:8080/agriculture/web/ag/home")
#         driver.maximize_window()
#         sleep(5)

        # request.cls.driver = driver
        # yield
        # driver.close()
