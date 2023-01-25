from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def ChIs1():
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
        browser.get("https://chebistok.ru/")
        price1 = browser.find_element(By.XPATH, '//*[@id="buy_water"]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[1]/input')
        price1 = price1.get_attribute('data-oneprice')
        return(price1)
    except:
        return("-")
    
def ChIs2():
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
        browser.get("https://chebistok.ru/")
        price2 = browser.find_element(By.XPATH, '//*[@id="buy_water"]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[1]/input')
        price2 = price2.get_attribute('data-price')
        return(price2)
    except:
        return("-")
    

