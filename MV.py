from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def GoOA2():
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
        browser.get("https://www.74mv.ru/")
        browser.find_element(By.XPATH, '/html/body/div[1]/header/nav/div[1]/div/ul/li[2]/a').click()
        price = browser.find_element(By.XPATH, '//*[@id="productPrice3"]/div[2]/span[2]')
        return(price.text.partition(',')[0])
    except:
        return("-")
    
