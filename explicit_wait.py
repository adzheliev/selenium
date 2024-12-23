from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get('https://suninjuly.github.io/explicit_wait2.html')

PRICE_LOCATOR = ('xpath', '//h5[@id="price"]')
price = wait.until(EC.text_to_be_present_in_element(PRICE_LOCATOR, '100'))
driver.find_element('xpath', '//button[@id="book"]').click()

driver.find_element('xpath', '//input[@id="answer"]').send_keys(math.log(abs(12*math.sin(int(driver.find_element('xpath', '//span[@id="input_value"]').text)))))
driver.find_element('xpath', '//button[@id="solve"]').click()

sleep(5)
