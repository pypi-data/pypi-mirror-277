from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

def load_cookies():
    print("Initializing driver... ⌛")
    
    cookies = {}
    
    options = Options()
    options.add_argument("--headless")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.vinted.fr")

        print("Started driver... ⌛")

        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

        cookies = driver.get_cookies()
        
        print("Cookies fetched ✅") 
    except WebDriverException as e:
        print("An error occurred while loading cookies:", e)   
    finally:
        driver.quit()
    
    return cookies

def load_auth_cookie():
    try:
        cookies = load_cookies()

        for cookie in cookies:
            name = "_vinted_fr_session"

            if cookie["name"] == name:
                sessionToken = cookie["value"]
                
                print("Auth cookie fetched ✅")
                
                return [name, sessionToken]
    except Exception as e:
        print("An error occurred while loading auth cookie:", e)
        return None

