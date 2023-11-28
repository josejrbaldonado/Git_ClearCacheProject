from selenium.webdriver.common.by import By

# This three classes under the PageObject package is use to Implement Page Object Mechanism
# also to show a smarter way of returning Page objects from the Navigation methods.


class Dashboard:

    # Always define a constructor in a class by using __init__(self)
    def __init__(self, driver):
        self.driver = driver

    # create an object of the links define in the test case and this will be inherited in the child method.
    # self.driver.find_element(By.LINK_TEXT, "ADMIN").click()
    admin_log = (By.LINK_TEXT, "ADMIN")

    def getAdminLog(self):
        return self.driver.find_element(*Dashboard.admin_log)
