import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver service
#it checks chrome driver version in the system
#service checks the driver version and service download that driver
#proble is if vpn that not download the driver
#if version is very low but if there is no library new version
#it will not work

#you can manually add the chromedriver and path in this
#so for this there is class
#service_obj = Service("D:/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
#Edge  - Edge Driver instead of Chrome
#Firefox (GeckoDriver) instead if Firefox

'''
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print("Title: ", driver.title)
print("Url: ",driver.current_url)
'''

'''
driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print("Title: ", driver.title)
print("Url: ",driver.current_url)
'''

driver = webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com/")

driver.maximize_window()
print("Title: ", driver.title)
print("Url: ",driver.current_url)




















time.sleep(2)
