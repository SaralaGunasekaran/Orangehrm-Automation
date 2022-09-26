import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

service=ChromeService(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

def test_url():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(2)
    driver.find_element(By.NAME,value="username").send_keys("Admin")
    time.sleep(2)
    driver.find_element(By.NAME,value="password").send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH,value="//button[@type='submit']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(2)
    ##driver.find_element(By.XPATH,"//a[contains(text(),'Add Employee')]").click()
    ##time.sleep(2)
    driver.find_element(By.NAME,"firstName").send_keys("Sarala")
    driver.find_element(By.NAME, "middleName").send_keys("Gunasekaran")
    driver.find_element(By.NAME,"lastName").send_keys("Karky")
    time.sleep(1)
    driver.find_element(By.XPATH,"//div//label//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,'(//div//input[@class="oxd-input oxd-input--active"])[3]').send_keys("sarala")
    time.sleep(2)
    driver.find_element(By.XPATH, '(//div//input[@class="oxd-input oxd-input--active" and @type="password"])[1]').send_keys("Qwerty@123")
    time.sleep(2)
    driver.find_element(By.XPATH, '(//div//input[@type="password"])[2]').send_keys("Qwerty@123")
    time.sleep(5)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Admin").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,'(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[1]').click()
    time.sleep(2)
    #driver.find_element(By.XPATH,'//div[2]//div[2]//div[2]//div[1]//div[1][contains(text(),"Admin")]').click()
    #driver.find_element(By.XPATH,'//div[contains(text(),"Admin") and @tabindex="0"]').click()
    #driver.find_element(By.XPATH, '(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[2]').click()
    time.sleep(2)
    #driver.find_element(By.XPATH, '(//div[@class="oxd-select-text--after"][1])').click()
    #time.sleep(2)
    driver.find_element(By.XPATH,'//input[@placeholder="Type for hints..."]').send_keys("Sarala")
    time.sleep(2)
    driver.find_element(By.XPATH,'(//div//input[@class="oxd-input oxd-input--active"])[2]').send_keys("sarala123")
    time.sleep(2)
    driver.find_element(By.XPATH,'(//input[@type="password"])[1]').send_keys("Qwerty@123")
    time.sleep(2)
    driver.find_element(By.XPATH, '(//input[@type="password"])[2]').send_keys("Qwerty@123")
    time.sleep(2)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Admin").click()
    time.sleep(2)
    driver.find_element(By.XPATH,'(//div//input[@class="oxd-input oxd-input--active"])[2]').send_keys("sarala123")
    time.sleep(2)
    driver.find_element(By.XPATH,'(//div[1][@class="oxd-select-text-input"])[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@placeholder="Type for hints..."]').send_keys("Sarala")
    time.sleep(2)
    driver.find_element(By.XPATH, '(//div[1][@class="oxd-select-text-input"])[2]').click()
    time.sleep(2)
    #driver.find_element(By.XPATH,'//div[@class="oxd-form-actions"]/child::button[@type="submit"]').click()
    #time.sleep(10)
    driver.find_element(By.XPATH,'//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"Logout").click()



test_url()