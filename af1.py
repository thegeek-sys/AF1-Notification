from selenium import webdriver
import time
import telegram_send
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://www.nike.com/it/t/scarpa-air-force-1-07-lKPQ6q/CW2288-111")

while True:
    try:
        driver.find_element(By.CSS_SELECTOR, 'input#skuAndSize__25634213[disabled]')
    except NoSuchElementException:
        break

    print("not found")
    time.sleep(60)
    print('refreshing\n')
    driver.execute_script("location.reload(true);")

print("found")
telegram_send.send(messages=["✔️ Nike Air Force 1 '07 - Disponibili ✔️"])
telegram_send.send(messages=["https://www.nike.com/it/t/scarpa-air-force-1-07-lKPQ6q/CW2288-111"])


#skuAndSize__25634213 42

#skuAndSize__25634212 49