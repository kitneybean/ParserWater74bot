from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re


def NiPre2():
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
        browser.get("https://niagara74.ru/")
        browser.execute_script("window.scrollTo(0, 1000)")
        price = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]')  
        return(re.findall("\d+", price.text)[0])        
    except:
        return("-")


def NiPre1():
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
        browser.get("https://niagara74.ru/")
        browser.execute_script("window.scrollTo(0, 1000)")
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/noindex/div').click()
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/noindex/div').click() 
        price2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/span')
        return(re.findall("\d+", price2.text)[0])        
    except:
        return("-")   


def NiPreKa1():
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
        browser.get("https://niagara74.ru/")
        browser.execute_script("window.scrollTo(0, 1000)")
        price3 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[1]')  
        return(re.findall("\d+", price3.text)[0])        
    except:
        return("-")


def NiPreKa2():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://niagara74.ru/")
        browser.execute_script("window.scrollTo(0, 1000)")
        browser.find_element(By.XPATH, '//*[@id="bx_1970176138_3919_4ab978e8bec606ce72388dc8980b7e26_buy_link"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="bx_1970176138_3919_4ab978e8bec606ce72388dc8980b7e26_quant_up"]').click()
        time.sleep(1)
        price4 = browser.find_element(By.ID, 'bx_1970176138_3919_4ab978e8bec606ce72388dc8980b7e26_price')
        return(re.findall("\d+", price4.text)[0])        
    except:
        return("-")


def Ni1():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://niagara74.ru/")
        browser.execute_script("window.scrollTo(0, 1000)")
        price5 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/div[2]/div[1]') 
        return(re.findall("\d+", price5.text)[0])        
    except:
        return("-")


def Ni2():
    try:
        chrome_options = webdriver.ChromeOptions()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://niagara74.ru/")
        browser.execute_script("window.scrollTo(0, 1000)")
        browser.find_element(By.XPATH, '//*[@id="bx_1970176138_401_0564dce275e0399e557aae3bf75c32cd_buy_link"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[@id="bx_1970176138_401_0564dce275e0399e557aae3bf75c32cd_quant_up"]').click()
        time.sleep(1)
        price6 = browser.find_element(By.ID, 'bx_1970176138_401_0564dce275e0399e557aae3bf75c32cd_price')
        return(re.findall("\d+", price6.text)[0])        
    except:
        return("-")
