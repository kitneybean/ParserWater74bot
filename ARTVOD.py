from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re


def Ld1():
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
        browser.get("https://artvod.ru/catalog/lider19-2/")
        price = browser.find_element(By.XPATH, '//*[@id="product-1183"]/div[3]/div[4]/table/tbody/tr[1]/td[3]')
        return(re.findall("\d+", price.text)[0]) 
    except:
        return("-")
    

def Ld2():
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
        browser.get("https://artvod.ru/catalog/lider19-2/")
        price = browser.find_element(By.XPATH, '//*[@id="product-1183"]/div[3]/div[4]/table/tbody/tr[2]/td[3]')
        return(re.findall("\d+", price.text)[0]) 
    except:
        return("-")
    

def LdPl1():
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
        browser.get("https://artvod.ru/catalog/lider-platinum-19/")
        price = browser.find_element(By.XPATH, '//*[@id="product-129"]/div[3]/div[4]/table/tbody/tr[1]/td[3]')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
    

def LdPl2():
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
        browser.get("https://artvod.ru/catalog/lider-platinum-19/")
        price = browser.find_element(By.XPATH, '//*[@id="product-129"]/div[3]/div[4]/table/tbody/tr[2]/td[3]')
        return(re.findall("\d+", price.text)[0])   
    except:
        return("-")
    

def LdPr1():
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
        browser.get("https://artvod.ru/catalog/lider-profi-19/")
        price = browser.find_element(By.XPATH, '//*[@id="product-688"]/div[3]/div[4]/table/tbody/tr[1]/td[3]')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
    

def LdPr2():
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
        browser.get("https://artvod.ru/catalog/lider-profi-19/")
        price = browser.find_element(By.XPATH, '//*[@id="product-688"]/div[3]/div[4]/table/tbody/tr[2]/td[3]')
        return(re.findall("\d+", price.text)[0])
    except:
        return("-")
    