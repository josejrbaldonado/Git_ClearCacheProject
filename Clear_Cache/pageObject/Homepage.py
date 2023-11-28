from selenium.webdriver.common.by import By

# This three classes under the PageObject package is use to Implement Page Object Mechanism
# also to show a smarter way of returning Page objects from the Navigation methods.


class Homepage:
    # Always define a constructor in a class by using __init__(self)
    def __init__(self, driver):
        self.driver = driver

    # create an object of the links define in the test case and this will be inherited in the child method.
    # self.driver.find_element(By.LINK_TEXT, "LOG IN").click()
    login = (By.LINK_TEXT, "LOG IN")
    # self.driver.find_element(By.ID, "_58_login").send_keys("AdminCache")
    username = (By.ID, "_58_login")
    # self.driver.find_element(By.ID, "_58_password").send_keys("P0p0yB0y$")
    password = (By.ID, "_58_password")
    # self.driver.find_element(By.CLASS_NAME, "btn.js-FormComponent-submitButton.btn_primary.btn-primary").click()
    submitbtn = (By.CLASS_NAME, "btn.js-FormComponent-submitButton.btn_primary.btn-primary")

    # create method of the links above and this will replace the links in the test cases.
    # always use * when inheriting the class object.
    def getLogin(self):
        return self.driver.find_element(*Homepage.login)

    def getUname(self):
        return self.driver.find_element(*Homepage.username)

    def getPwd(self):
        return self.driver.find_element(*Homepage.password)

    def getSubmitBtn(self):
        return self.driver.find_element(*Homepage.submitbtn)



