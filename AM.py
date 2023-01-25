from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

def Artenza2():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-artenza-19-l-oborotnaya-tara.html")
        price2 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price2.text))
    except:
        return("-")
    

def Artenza1():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-artenza-19-l-oborotnaya-tara.html")
        browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[2]/div[2]/button[1]').click()
        browser.find_element(By.XPATH, '//*[@id="optinfo"]/div/div[1]').click()
        price1 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price1.text))
    except:
        return("-")
    

def Sosn1():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-sosnovskaya.html")
        price2 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price2.text))
    except:
        return("-")
        

def Sosn2():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-sosnovskaya.html")
        browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[2]/div[2]/button[1]').click()
        browser.find_element(By.XPATH, '//*[@id="optinfo"]/div/div[1]').click()
        price1 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price1.text))
    except:
        return("-")
        

def Kukazar2():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-kukazar-19l-pet-tara.html")
        price2 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price2.text))
    except:
        return("-")
    

def Kukazar1():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-kukazar-19l-pet-tara.html")
        browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[2]/div[2]/button[1]').click()
        browser.find_element(By.XPATH, '//*[@id="optinfo"]/div/div[1]').click()
        price1 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price1.text))
    except:
        return("-")
    

def Irendik2():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-akva-irendyk.html") 
        price2 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price2.text))
    except:
        return("-")
    
def Irendik1():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-akva-irendyk.html") 
        browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[2]/div[2]/button[1]').click()
        browser.find_element(By.XPATH, '//*[@id="optinfo"]/div/div[1]').click()
        price1 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price1.text))
    except:
        return("-")
    

def Arhiz2():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/mineralalnaya-pitevaya-stolovaya-voda-legenda-gor-arhyz.html")   
        price2 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price2.text))
    except:
        return("-")
   

def Arhiz1():
    try:
        options = Options()
        options.headless = True
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument("--disable-infobars") 
        browser = webdriver.Chrome(options=options)
        browser.get("https://aqua-mobil.ru/voda-9-19-litrov/mineralalnaya-pitevaya-stolovaya-voda-legenda-gor-arhyz.html")   
        browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[2]/div[2]/button[1]').click()
        price1 = browser.find_element(By.XPATH, '//*[@id="ajax_change_block"]/form/div[1]/div[1]/div[2]/span')
        return(int(price1.text))
    except:
        return("-")
    
