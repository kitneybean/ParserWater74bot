from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import time


def Lu_Vo1():
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
        browser.get("https://l-w.ru/catalog/voda/voda_19l/")
        time.sleep(2)
        price = browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div[1]/div[1]/div[2]')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
    

def Lu_Vo2():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://l-w.ru/catalog/voda/")
        time.sleep(2)
        price = browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[2]/div[3]/div[2]/div')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
    

def Luxic1():
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
        browser.get("https://l-w.ru/catalog/voda/lyuksik_19l/")
        time.sleep(4)
        price = browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div[1]/div[1]/div[2]')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
    

def Luxic2():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://l-w.ru/catalog/voda/")
        time.sleep(3)
        price = browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div[1]/div[3]/div[2]/div')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
   



