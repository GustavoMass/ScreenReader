from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

driver = webdriver.Chrome()
driver.get("https://app.liquidium.fi/portfolio")
time.sleep(2)
connectButton = driver.find_element(By.XPATH, "//button[text()='Connect']").click()
time.sleep(2)
dialog = driver.switch_to.active_element
time.sleep(2)
# selectWallet = driver.find_element(By.XPATH, "//img[text()='Xverse']").click()
selectWallet = locate_with(By.TAG_NAME, "button").above({By.XPATH, "//div[text()='Xverse']"})
time.sleep(2)
clickWallet = selectWallet.click()
# clickWallet = driver.find_element(selectWallet).click()
# clickWallet = driver.(selectWallet).click()
time.sleep(2)
# elem = driver.find_element(By.XPATH, "//span[text()='Lending']")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

print("---------------------------")
print(selectWallet)

# alertAccept = driver.switch_to.alert.accept


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# para que ele aceite a transação, ainda falta uma etapa


#pro código ficar bom de verdade, tenho q usar os waits, não time.sleep