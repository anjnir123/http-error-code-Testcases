import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ✅ Test URLs for different HTTP errors (use HTTP to avoid SSL issues)
test_urls = {
    "404 Not Found": "http://httpstat.us/404",
    "403 Forbidden": "http://httpstat.us/403",
    "401 Unauthorized": "http://httpstat.us/401",
    "500 Internal Server Error": "http://httpstat.us/500",
    "502 Bad Gateway": "http://httpstat.us/502",
    "503 Service Unavailable": "http://httpstat.us/503",
    "400 Bad Request": "http://httpstat.us/400",
    "200 OK": "http://httpstat.us/200",
    "418 I'm a teapot": "http://httpstat.us/418",
}

# ✅ Setup Chrome headless for Codespaces
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome"

# ✅ Use installed ChromeDriver path
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

def test_http_code(name, url):
    print(f"\n--- Testing {name} ---")
    try:
        response = requests.get(url)
        print(f"HTTP Status Code (requests): {response.status_code}")
        driver.get(url)
        time.sleep(1)
        print("Page title (Selenium):", driver.title)
    except Exception as e:
        print(f"Exception occurred: {e}")

# ✅ Run all test URLs
for name, url in test_urls.items():
    test_http_code(name, url)

driver.quit()
