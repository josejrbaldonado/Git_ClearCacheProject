import logging
import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Reside all reusable class or method for the test cases.
# The conftest fixture is introduced in this Base class to be use.
# Additional code for logging information.


@pytest.mark.usefixtures("setup")
class BaseClass:
    # Implement logging into the framework
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    # Created Explicit wait implementation to be reusable by creating reusable methods.
    def verifyCSSPresence(self, css):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.app-content')))
        except:
            pytest.fail("Log In page not available")

    def verifyURLHSPresence(self, website):
        try:
            wait = WebDriverWait(self.driver, 10)
            #wait.until(EC.url_contains(
            #"http://agonline-app-pre07.dtn.com:8080/mydtn-public-core-portlet/common/link.do?symbolicName=/common/admin"))
            wait.until(EC.url_contains(
            "http://agonline-app-dev03.dtn.com:8080/mydtn-public-core-portlet/common/link.do?symbolicName=/common/admin"))
        except:
            pytest.fail("URL not accessible")

    def verifyLinkHSTxtPresence(self, text):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, '(+)com.dtn.agonline.entity.location.Location')))
            # For PRE and PROD env use this link (+)com.dtn.common.addons.cache.default
        except:
            pytest.fail("HS Cache not all cleared")

    def verifyURLEHPresence(self, website):
        try:
            wait = WebDriverWait(self.driver, 10)
            #wait.until(EC.url_contains(
            #"http://agonline-app-pre07.dtn.com:8080/agriculture/web/ag/home"))
            wait.until(EC.url_contains(
            "http://agonline-app-dev03.dtn.com:8080/agriculture/web/ag/home"))
        except:
            pytest.fail("Home URL not visible")

    def verifyLinkEHTxtPresence(self, text):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, '(+)RecentlyNotifiedOMTrialUsers')))
            # For PRE and PROD env use this link - (+)org.hibernate.cache.UpdateTimestampsCache
        except:
            pytest.fail("ES Cache not all cleared")
