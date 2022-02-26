from selenium import webdriver
import time
import telegram_send
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from pyvirtualdisplay import Display
from datetime import datetime
import signal
import os

print("["+datetime.now().strftime("%H:%M:%S")+"] started")
telegram_send.send(messages=["["+datetime.now().strftime("%H:%M:%S")+"] started"])

#display = Display(visible=0, size=(982, 800))
#display.start()

def signal_handler(sig, frame):
    print("\n["+datetime.now().strftime("%H:%M:%S")+"] You pressed Ctrl+C!")
    #os.system("killall -9 chromium-browser")
    os.system("taskkill /IM chromedriver.exe /F")
    exit()

signal.signal(signal.SIGINT, signal_handler)

#ser = Service("/usr/lib/chromium-browser/chromedriver")
chrome_options = Options()
chrome_options.add_argument("--window-size=982,753")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.nike.com/it/t/scarpa-air-force-1-07-lKPQ6q/CW2288-111")

print("["+datetime.now().strftime("%H:%M:%S")+"] looking for shoes")
telegram_send.send(messages=["["+datetime.now().strftime("%H:%M:%S")+"] looking for shoes"])

driver.find_element(By.ID, "hf_cookie_text_cookieAccept").click()
while True:
    try:
        driver.find_element(By.CSS_SELECTOR, 'input#skuAndSize__25634213[disabled]')
        print("["+datetime.now().strftime("%H:%M:%S")+"] not found")
    except NoSuchElementException:
        now = datetime.now().strftime("%H:%M:%S")
        print("["+now+"] found")
        driver.save_screenshot("screenshot.png")
        with open("screenshot.png", "rb") as f:
            telegram_send.send(images=[f], captions=["["+now+"]\n✔️ Nike Air Force 1 '07 - Disponibili ✔️"])

    time.sleep(20)
    print("["+datetime.now().strftime("%H:%M:%S")+"] refreshing\n")
    driver.execute_script("location.reload(true);")

#skuAndSize__25634213 42

#skuAndSize__25634212 49