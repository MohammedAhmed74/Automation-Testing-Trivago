from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
PATH = 'C:/Users/10/Documents/chromedriver_win32/chromedriver'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(PATH))
driver.get('https://www.trivago.com/')
wait = WebDriverWait(driver, 5)
#                        - How many options exist before login?
numOfOptionsBeforeLogin = len(driver.find_elements(By.CLASS_NAME, 'h-full.list-none.flex.relative'))
driver.find_element(By.CSS_SELECTOR,"button[data-testid='header-login']").click()
wait = WebDriverWait(driver, 5)
# enter email
driver.find_element(By.ID,'email').send_keys('mmmm@gmail.com')
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait = WebDriverWait(driver, 10)
password = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
# enter password
password.send_keys('PasswordPassword')
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(1)
# show password
driver.find_element(By.ID,'toggle-icon').click()
wait = WebDriverWait(driver, 5)
# login
driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
wait = WebDriverWait(driver, 5)

time.sleep(5)
#                        - How many options exist after login?
numOfOptionsAfterLogin = len(driver.find_elements(By.CLASS_NAME, 'h-full.list-none.flex.relative'))

#                        - login option is no longer exists
class Test_Login():    
    def test_morningMsgFound(self):
        assert numOfOptionsBeforeLogin > numOfOptionsAfterLogin
