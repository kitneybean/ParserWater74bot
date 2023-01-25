from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def Zhka2():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get('https://живаякапля.рф/')
        try:
            browser.find_element(By.XPATH, '//*[@id="popup_iframe_wrapper"]/div[2]/a').click()
        except:
            pass
        price = browser.find_element(By.XPATH, '//*[@id="bx_2875157043_891"]/div/table/tbody/tr/td[1]/div/div/div/div[1]/form/div[2]/div/div[2]')
        price = int(price.text.partition('.')[0])/2
        return(str(price).partition('.')[0])
    except:
        return("-")
    

def Zhka1():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get('https://живаякапля.рф/')
        try:
            browser.find_element(By.XPATH, '//*[@id="popup_iframe_wrapper"]/div[2]/a').click()
        except:
            pass
        browser.find_element(By.XPATH, '//*[@id="bx_2875157043_891"]/div/table/tbody/tr/td[1]/div/div/div/div[1]/form/div[1]/div[1]/div[2]/button[1]').click()
        price = browser.find_element(By.XPATH, '//*[@id="bx_2875157043_891"]/div/table/tbody/tr/td[1]/div/div/div/div[1]/form/div[2]/div/div[2]')
        price = price.text
        return(price.partition('.')[0])
    except:
        return("-")
    