from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.camskra.com/")
elem = driver.find_element_by_name("ctl00$tbPanSrch")
elem.clear()
elem.send_keys("AAAPL1234C")
elem.send_keys(Keys.RETURN)
assert "HEAVY" not in driver.page_source
driver.close()

