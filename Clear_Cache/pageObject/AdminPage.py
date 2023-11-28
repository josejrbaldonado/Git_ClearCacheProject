from selenium.webdriver.common.by import By

# This three classes under the PageObject package is use to Implement Page Object Mechanism
# also to show a smarter way of returning Page objects from the Navigation methods.


class AdminPage:

    # Always define a constructor in a class by using __init__(self)
    def __init__(self, driver):
        self.driver = driver

    # create an object of the links define in the test case and this will be inherited in the child method.
    # self.driver.find_element(By.LINK_TEXT, "H.S. CACHE MANAGER").click()
    hs_button = (By.LINK_TEXT, "H.S. CACHE MANAGER")
    # self.driver.find_element(By.CSS_SELECTOR, "a[href$='/mydtn-public-core-portlet/view/admin/commandCacheManagement.do?command=clear&cacheName=___all']").click()
    hs_clr = (By.CSS_SELECTOR,
     "a[href$='/mydtn-public-core-portlet/view/admin/commandCacheManagement.do?command=clear&cacheName=___all']")

    # self.driver.find_element(By.LINK_TEXT, "EHCACHE MANAGER").click()
    eh_button = (By.LINK_TEXT, "EHCACHE MANAGER")

    # self.driver.find_element(By.XPATH, "//img[@title='Select/Deselect All Caches']").click()
    eh_all = (By.XPATH, "//img[@title='Select/Deselect All Caches']")

    # self.driver.find_element(By.CSS_SELECTOR, "input[value=Clear]").click()
    eh_clr = (By.CSS_SELECTOR, "input[value=Clear]")

    # self.driver.find_element(By.LINK_TEXT, "Back To Ag Online V4").click()
    eh_back = (By.LINK_TEXT, "Back To Ag Online V4")

    def getHS(self):
        return self.driver.find_element(*AdminPage.hs_button)

    def getHSclr(self):
        return self.driver.find_element(*AdminPage.hs_clr)

    def getEH(self):
        return self.driver.find_element(*AdminPage.eh_button)

    def getEHall(self):
        return self.driver.find_element(*AdminPage.eh_all)

    def getEHclr(self):
        return self.driver.find_element(*AdminPage.eh_clr)

    def getEHback(self):
        return self.driver.find_element(*AdminPage.eh_back)

