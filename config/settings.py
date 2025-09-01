from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 3)
chrome_options = {
    "headless": False,
    "incognito": True
}

YOUTUBE_URL = "https://www.youtube.com/watch?v=I3GWzXRectE&pp=ygUhdW5pdmVyaXN5dCBvZiBveGZvcmQgY3NlIGxlY3R1cmVz"

OUTPUT_CSV = "data/comments.csv"

MAX_COMMENTS = 150