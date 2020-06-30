from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://my.unt.edu")
user_id_elm = driver.find_element_by_id("userid")
user_id_elm.send_keys("sp1004")
user_pwd_elm = driver.find_element_by_id("pwd")
user_pwd_elm.send_keys("abcd",Keys.ENTER)
