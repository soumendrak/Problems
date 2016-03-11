# import time
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
 
 
def auth(driver, uname, pwd):
    driver.get("https://www.irctc.co.in")
    try:
        box = driver.wait.until(EC.presence_of_element_located((By.NAME, "j_username")))
        box.send_keys(uname)
        driver.find_element_by_name("j_password").send_keys(pwd)
        driver.find_element_by_name("j_captcha").send_keys(Keys.TAB)
#         driver.implicitly_wait(04)
#         box.send_keys(Keys.RETURN)        
    except TimeoutException:
        print("Box or Button not found in irctc")
 
 
if __name__ == "__main__":
    driver = init_driver()
    auth(driver, 'soumendra6','iTKOH@087C')
    Flag = raw_input('Do you want to close the browser?(Y/N)')
    if Flag == 'Y':
        driver.quit()