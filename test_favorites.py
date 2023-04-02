from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
from selenium.webdriver.common.action_chains import ActionChains


ChromePATH = 'C:/Users/10/Documents/chromedriver_win32/chromedriver'
EdgePATH = 'C:/Users/10/Documents/edgedriver_win64/msedgedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromePATH))
# driver = webdriver.Edge(EdgePATH)

#                        - Open the website
driver.maximize_window()
driver.get('https://www.trivago.com/')



# //////////////////////////////////////// login process
wait = WebDriverWait(driver, 5)
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
# show password
driver.find_element(By.ID,'toggle-icon').click()
wait = WebDriverWait(driver, 5)
# login
driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
# //////////////////////////////////////// login process



time.sleep(5)
#                        - Go to favorites
driver.find_element(By.CSS_SELECTOR, "a[role='link']").click()

time.sleep(4)
#                        - How many lists exist before delete?
numOfListsBeforeDelete = driver.find_element(By.CSS_SELECTOR,".text-m.text-grey-900.mt-1.mb-3").text


#                        - Delete the old list
element = driver.find_element(By.CSS_SELECTOR, "img[alt='test1']")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(2) > main:nth-child(5) > div:nth-child(2) > section:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2) > span:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(2) > main:nth-child(5) > div:nth-child(2) > section:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > button:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'body > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)').click()

time.sleep(5)
#                        - How many lists exist after delete?
numOfListsAfterDelete = driver.find_element(By.CSS_SELECTOR,".text-m.text-grey-900.mt-1.mb-3").text

#                        - Test delete function
class Test_deleteFunction():    
    def test_numOfListsIslessNow(self):
        assert numOfListsBeforeDelete != numOfListsAfterDelete

time.sleep(1)
#                        - How many lists exist before add?
numOfListsBeforeAdd = driver.find_element(By.CSS_SELECTOR,".text-m.text-grey-900.mt-1.mb-3").text

#                        - Add Empty list
driver.find_element(By.CSS_SELECTOR, '.flex.items-center.gap-2').click()
time.sleep(1)
saveButton = driver.find_element(By.CSS_SELECTOR, 'body > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > button:nth-child(2) > span:nth-child(1)')
saveButton.click()
emptyNameMsg = driver.find_element(By.CSS_SELECTOR, '.p-1.mt-2.w-full.absolute.bottom.border.text-m.text-red-800.border-red-700.bg-white.FavoriteListForm_error__UGU7J').text


#                        - add real list
time.sleep(3)
inputListName = driver.find_element(By.NAME, 'hotelName')
inputListName.send_keys('new list')
saveButton = driver.find_element(By.CSS_SELECTOR, 'body > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > button:nth-child(2) > span:nth-child(1)')
saveButton.click()

time.sleep(1)
#                        - How many lists exist after add?
numOfListsAfterAdd = driver.find_element(By.CSS_SELECTOR,".text-m.text-grey-900.mt-1.mb-3").text

#                        - Test add function
class Test_addFunction():    
    def test_cantAddlistWithoutName(self):
        assert emptyNameMsg == 'Please name your list'

    def test_numOfListsIsMoreNow(self):
        assert numOfListsBeforeAdd != numOfListsAfterAdd