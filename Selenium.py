#1
# from selenium import webdriver
# browser=webdriver.Firefox()
# browser.get('http://www.google.com')

#2
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# # driver.close()

#3
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class PythonOrgSearch(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         print '1'

#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("https://www.python.org")
#         try:
#             self.assertIn("Python", driver.title)       #It reassures that the title name is Python to avoid further complication of the matter
#             elem = driver.find_element_by_name("q")
#             elem.send_keys("soumendra")
#             elem.send_keys(Keys.RETURN)
#         except:
#             assert "No results found." not in driver.page_source
#             print '2'


#     def tearDown(self):
#         self.driver.close()
#         print '3'

# if __name__ == "__main__":
#     print 'main'
#     unittest.main()

#4
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
 
 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver, query):
    driver.get("http://www.google.com")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        box.send_keys(query)
        box.send_keys(Keys.RETURN)        
    except TimeoutException:
        print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, 'soumendra')
    Flag = raw_input('Do you want to close the browser?(Y/N)')
    if Flag == 'Y':
        driver.quit()