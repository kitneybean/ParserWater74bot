from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re

def Lubim2():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://vodalubima.ru/")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 1700)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 2300)")
        time.sleep(1)
        price = browser.find_element(By.XPATH, '//*[@id="rec42533675"]/div/div/div[1]/div/div[2]/div[2]')
        return(re.findall("(?<=\s)\d{3}(?=\s)", price.text)[0])
    except:
        return("-")   
        

def Lubim1():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://vodalubima.ru/")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 1700)")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 2300)")
        time.sleep(1)
        price = browser.find_element(By.XPATH, '/html/body/div[1]/div[7]/div/div/div[1]/div/div[2]/div[3]/div/div[1]')
        return (price.text)
    except:
        return("-")
    