from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import Select
# from selenium.webdriver import ActionChains
ChromePATH = 'C:/Users/10/Documents/chromedriver_win32/chromedriver'
EdgePATH = 'C:/Users/10/Documents/edgedriver_win64/msedgedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromePATH))
# driver = webdriver.Edge(EdgePATH)

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


time.sleep(4)
# place
driver.find_element(By.ID,"input-auto-complete").send_keys('Cairo')
time.sleep(0.5)
driver.find_element(By.XPATH, "//li[@class='cursor-pointer bg-grey-200']//div[@class='text-grey-900 text-l truncate']").click()

# driver.find_element(By.XPATH,"//button[@class='block px-2 bg-white text-left disabled:opacity-50 disabled:cursor-default w-full 2xl:rounded-l-sm flex items-center border-r-0 h-11']").click()
time.sleep(2)
start_date = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='block relative group text-center text-m w-10 h-9 cursor-pointer hover:bg-grey-700 hover:text-white rounded-xs']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][normalize-space()='1']")))
start_date.click()
time.sleep(2)
end_date = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='block relative group text-center text-m w-10 h-9 cursor-pointer hover:bg-grey-700 hover:text-white rounded-xs']//span[@class='absolute inset-0 flex justify-center items-center overflow-hidden -mt-px -ml-px border-transparent'][normalize-space()='25']")))
end_date.click()
time.sleep(2)

# rooms
# increase adults number
driver.find_element(By.XPATH, "//button[@data-testid='adults-amount-plus-button']").click()
driver.find_element(By.XPATH, "//button[@data-testid='adults-amount-plus-button']").click()
# increase children number
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='number-input-13']").send_keys('3')
# increase roomss number
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@data-testid='rooms-amount-plus-button']//span[@class='inline-flex leading-none transform self-center']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@data-testid='rooms-amount-plus-button']//span[@class='inline-flex leading-none transform self-center']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@data-testid='rooms-amount-plus-button']//span[@class='inline-flex leading-none transform self-center']").click()
time.sleep(0.5)
select = Select(driver.find_element(By.XPATH, "//select[@id='select-0']"))
select.select_by_value('10')
select = Select(driver.find_element(By.XPATH, "//select[@id='select-1']"))
select.select_by_value('8')
select = Select(driver.find_element(By.XPATH, "//select[@id='select-2']"))
select.select_by_value('4')
time.sleep(1)
driver.find_element(By.XPATH, "//button[@data-testid='guest-selector-apply']").click()
# select only hotels 
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,"label[for='accommodation-type-hotel']").click()
# search 
time.sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Search']").click()

wait = WebDriverWait(driver, 10)
searchResult = wait.until(EC.visibility_of_element_located((By.XPATH,"//strong[normalize-space()='Price / night']")))
class Test_search():    
    def test_resultsAppeared(self):
        assert searchResult.get_attribute('innerHTML') == 'Price / night'

# # driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div[1]/div[4]/div/form/div[4]/div/div/div[2]/div/div[1]/button/span[2]').click()
# # time.sleep(2)
# leftSlider = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[2]')
# rightSlider = driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[3]')
# time.sleep(2)
# ActionChains(driver).drag_and_drop_by_offset(rightSlider, 20, 0).perform()