from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

options_config = webdriver.ChromeOptions()
options_config.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_config)
driver.get("https://ozh.github.io/cookieclicker/")

# sleep(5)

# try:
#     eng_btn = driver.find_element(By.ID, "langSelect-EN")
#     print("pressing english button")
#     eng_btn.click()
# except NoSuchElementException:
#     print("No element found...")

sleep(5)
# print("Completing loading")

cookie_btn = driver.find_element(By.ID, "bigCookie")

product_ids = [f"product{i}" for i in range(1,20)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie_btn.click()
    if time() > timeout:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            cookie_text = cookies_element.text
            print(cookie_text)
        except:
            print("Error")