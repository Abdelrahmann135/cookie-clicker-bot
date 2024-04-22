from selenium import webdriver
from selenium.webdriver.common.by import By
import time

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_option)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
timeout = 5

timeout_start = time.time()
while True:
    cookie.click()
    while time.time() >= timeout_start + timeout:
        store = [element.text for element in driver.find_elements(By.CSS_SELECTOR, "#store b")[:8]]
        products = [product.split("-")[0].strip() for product in store]
        prices = [int(price.split("-")[1].strip().replace(",", "")) for price in store]
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        for price in prices[::-1]:
            if price <= money:
                element_wanted = f"buy{products[prices.index(price)]}"
                buy = driver.find_element(By.ID, element_wanted)
                buy.click()
                break
        timeout_start = time.time()
