from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

def VlKl():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("http://vlasovkluch.ru/cat/product/item_6.html")
        browser.refresh()
        price = browser.find_element(By.CLASS_NAME, 'price-inf-info-card-product')
        return(re.findall("\d+", price.text)[0])        
    except:
        return("-")
