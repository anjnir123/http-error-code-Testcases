import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

test_urls = {
    "404 Not Found": "https://httpstat.us/404",
    "403 Forbidden": "https://httpstat.us/403",
    "401 Unauthorized": "https://httpstat.us/401",
    "500 Internal Server Error": "https://httpstat.us/500",
    "502 Bad Gateway": "https://httpstat.us/502",
    "503 Service Unavailable": "https://httpstat.us/503",
    "400 Bad Request": "https://httpstat.us/400",
    "200 OK": "https://httpstat.us/200",
    "418 I'm a teapot": "https://httpstat.us/418",
}

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def test_http_code(name, url):
    print(f"\n--- Testing {name} ---")
    
    try:
        response = requests.get(url)
        status_code = response.status_code
        print(f"HTTP Status Code: {status_code}")

        driver.get(url)
        time.sleep(2)

        print("Page title:", driver.title)

    except Exception as e:
        print(f"Exception occurred: {e}")

for name, url in test_urls.items():
    test_http_code(name, url)

driver.quit()
