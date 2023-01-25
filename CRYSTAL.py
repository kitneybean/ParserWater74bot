from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import time

def Cr1():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://voda174.ru/")
        browser.execute_script("window.scrollTo(0, 1500)")
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="1497b26fd43a4d25bdb11c90d1a40b9e"]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div').click()
        time.sleep(2)
        price = browser.find_element(By.XPATH, '//*[@id="product-popup"]/div[2]/div/div[3]/div[1]/div[3]/div[1]/span[1]')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
    

def Cr2():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://voda174.ru/")
        browser.execute_script("window.scrollTo(0, 1500)")
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="1497b26fd43a4d25bdb11c90d1a40b9e"]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="product-popup"]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/label').click()
        price2 = browser.find_element(By.XPATH, '//*[@id="product-popup"]/div[2]/div/div[3]/div[1]/div[3]/div[1]/span[1]')
        price2 = int(re.findall("\d+", price2.text)[0])/2
        return(str(price2).partition('.')[0])
    except:
        return("-")
    