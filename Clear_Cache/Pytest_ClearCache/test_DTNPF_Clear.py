from time import sleep

from pageObject.AdminPage import AdminPage
from pageObject.Dashboard import Dashboard
from pageObject.Homepage import Homepage
from utilities.BaseClass import BaseClass

# Below are the actual test case to be run from Login -- Access Admin page -- clearing of cache


class TestDTNPF(BaseClass):

    # Going to Homepage
    def test_pf(self):
        log = self.getLogger()
        self.verifyCSSPresence('.app-content')

        homePage = Homepage(self.driver)
        homePage.getLogin().click()

        self.verifyCSSPresence('.tabs-list.tabs-list_3up')

        homePage.getUname().send_keys("AdminCache")
        homePage.getPwd().send_keys("P0p0yB0y$")
        homePage.getSubmitBtn().click()

        print("<<<<<<<<<< AdminCache Log In was successful >>>>>>>>>>>")
        log.info("<<<<<<<<<< AdminCache Log In was successful >>>>>>>>>>>")
        sleep(5)

    # LogIn to the Dashboard
    def test_dashboard(self):
        log = self.getLogger()
        getadmin = Dashboard(self.driver)
        getadmin.getAdminLog().click()

        print("<<<<<<< Admin selected >>>>>>>>")
        log.info("<<<<<<< Admin selected >>>>>>>>")
        sleep(5)

    # Access the AdminPage
    # Clearing the HS Cache
    def test_hs_cache(self):
        log = self.getLogger()
        self.verifyURLHSPresence("http://agonline-app-dev03.dtn.com:8080/mydtn-public-core-portlet/common/link.do?symbolicName=/common/admin")

        hscache = AdminPage(self.driver)
        hscache.getHS().click()

        self.verifyLinkHSTxtPresence('(+)com.dtn.agonline.entity.location.Location')
        # For PRE and PROD env use this link (+)com.dtn.common.addons.cache.default

        hscache.getHSclr().click()

        print("<<<<<<< HS Cache CLEARED >>>>>>>>")
        log.info("<<<<<<< HS Cache CLEARED >>>>>>>>")

    # Clearing the EH Cache
    def test_eh_cache(self):
        log = self.getLogger()
        ehcache = AdminPage(self.driver)
        ehcache.getEH().click()

        self.verifyLinkEHTxtPresence('(+)RecentlyNotifiedOMTrialUsers')
        # For PRE and PROD env use this link - (+)org.hibernate.cache.UpdateTimestampsCache

        ehcache.getEHall().click()

        ehcache.getEHclr().click()

        self.verifyLinkEHTxtPresence('(+)RecentlyNotifiedOMTrialUsers')
        # For PRE and PROD env use this link - (+)org.hibernate.cache.UpdateTimestampsCache

        ehcache.getEHback().click()

        self.verifyURLEHPresence("http://agonline-app-dev03.dtn.com:8080/agriculture/web/ag/home")

        print("<<<<<<< EH Cache CLEARED >>>>>>>>")
        log.info("<<<<<<< EH Cache CLEARED >>>>>>>>")



# THIS THE TEST CASE WITHOUT ANY PAGE OBJECT, CUSTOM UTILITIES AND PARAMETERIZATION
# To Rollback remove all Page Object and then just write pass in the Base Class
#
# class TestDTNPF(BaseClass):
#
#     # Going to Homepage
#     def test_pf(self):
#         wait = WebDriverWait(self.driver, 5)
#         wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.app-content')))
#         #self.driver.find_element(By.LINK_TEXT, "LOG IN").click()
#         wait = WebDriverWait(self.driver, 5)
#         wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tabs-list.tabs-list_3up')))
#         self.driver.find_element(By.ID, "_58_login").send_keys("AdminCache")
#         self.driver.find_element(By.ID, "_58_password").send_keys("P0p0yB0y$")
#         self.driver.find_element(By.CLASS_NAME, "btn.js-FormComponent-submitButton.btn_primary.btn-primary").click()
#         sleep(5)
#
#     # Going to Dashboard
#     def test_admin(self):
#         self.driver.find_element(By.LINK_TEXT, "ADMIN").click()
#         sleep(5)
#
#     # Going to AdminPage
#     def test_hs_cache(self):
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.url_contains(
#             "http://agonline-app-pre07.dtn.com:8080/mydtn-public-core-portlet/common/link.do?symbolicName=/common/admin"))
#         self.driver.find_element(By.LINK_TEXT, "H.S. CACHE MANAGER").click()
#              # self.driver.execute_script("window.scrollTo (0, document.body.scrollHeight);")
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located((By.LINK_TEXT, '(+)com.dtn.agonline.entity.location.Location')))
#         self.driver.find_element(By.CSS_SELECTOR, "a[href$='/mydtn-public-core-portlet/view/admin/commandCacheManagement.do?command=clear&cacheName=___all']").click()
#
#     def test_eh_cache(self):
#         self.driver.find_element(By.LINK_TEXT, "EHCACHE MANAGER").click()
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located((By.LINK_TEXT, "(+)org.hibernate.cache.UpdateTimestampsCache")))
#         self.driver.find_element(By.XPATH, "//img[@title='Select/Deselect All Caches']").click()
#         self.driver.find_element(By.CSS_SELECTOR, "input[value=Clear]").click()
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located((By.LINK_TEXT, "(+)org.hibernate.cache.UpdateTimestampsCache")))
#         self.driver.find_element(By.LINK_TEXT, "Back To Ag Online V4").click()
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.url_contains("http://agonline-app-pre07.dtn.com:8080/agriculture/web/ag/home"))

