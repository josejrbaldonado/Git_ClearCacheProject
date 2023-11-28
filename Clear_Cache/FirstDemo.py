from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://google.com")

service_obj = Service(r"C:\Users\JOSEJR.BALDONADO\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)
driver.close()




#print("Hello")

# Write comments here

