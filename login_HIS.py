

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://52.220.233.172:9080/hinai/login.html")

use_ele = driver.find_element_by_name("j_username")

print(use_ele.is_displayed())
print(use_ele.is_enabled())

pwd_ele = driver.find_element_by_name("j_password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

use_ele.send_keys("1418")
pwd_ele.send_keys("bappy0244")

driver.find_element_by_xpath("//*[@id='form-login']/button").click()
#driver.find_element_by_xpath("//*[@id='nav-app']/a").click()
link = driver.find_element_by_link_text("Apps")
link.click()

link1 = driver.find_element_by_link_text("Ambulatory Care")
link1.click()
driver.find_element_by_id("leftSiderBarForm:outpatientsMastersId").click()
#driver.find_element_by_id("leftSiderBarForm:priorRegLink").click()
#link2 = Select(driver.find_element_by_id("leftSiderBarForm:outpatientsMastersId"))
#link2.deselect_by_visible_text("Registration")
#driver.find_elements_by_class_name("rich-cm-attached").click()

element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leftSiderBarForm:registrationLeftSideLink']")))
element.click()

element1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='leftSiderBarForm:link_666337_666295']/span")))
element1.click()

ele = driver.find_element_by_id("navigation:patientType")
drp = Select(ele)
drp.select_by_visible_text('SKF')

ele1 = driver.find_element_by_id("navigation:patPrefix")
drp1 = Select(ele1)
drp1.select_by_visible_text('Mr')

ele2 = driver.find_element_by_id("navigation:genderCombo")
drp2 = Select(ele2)
drp2.select_by_visible_text('MALE')

driver.find_element_by_id("navigation:firstName").send_keys("Test1")

driver.find_element_by_id("navigation:patRegDOBInputDate").send_keys("10-9-2020")

driver.find_element_by_id("navigation:patMobileNo").send_keys("01682269024")

driver.find_element_by_id("navigation:normalEmail").send_keys("mbappy@praavahealth.com")

driver.find_element_by_id("navigation:singAddrhouseAddress").send_keys("House 31, Road 4, Block A")

driver.find_element_by_id("navigation:singAddrlocality").send_keys("Rampura, Dhaka")

driver.find_element_by_id("navigation:singAddractive").click()

driver.find_element_by_xpath("//*[@id='navigation:register_REGTYPES001Btn']").click()