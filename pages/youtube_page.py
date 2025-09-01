from config import settings
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import pandas as pd

class YoutubePage:

    def __init__(self, driver):
        self.driver = driver
        self.max_comments = settings.MAX_COMMENTS
        self.wait = WebDriverWait(driver, 10)

    def load_page(self):
        self.driver.get(settings.YOUTUBE_URL)

    def youtube_comments(self, driver):
        self.driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)

        # Wait for comments section
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="comments"]')))
        comments_section = self.driver.find_element(By.XPATH, '//*[@id="comments"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comments_section)
        time.sleep(3)

        data = []
        seen_comments = set()  # To avoid duplicates

        while len(data) < self.max_comments:
            comments_block = driver.find_element(By.XPATH, '//*[@id="comments"]//div[@id="contents"]')
            name_elems = comments_block.find_elements(By.XPATH, './/*[@id="author-text"]')
            comment_elems = comments_block.find_elements(By.XPATH, './/*[@id="content-text"]')
            like_elems = comments_block.find_elements(By.XPATH, './/*[@id="vote-count-middle"]')

            for name, comment, like in zip(name_elems, comment_elems, like_elems):
                text = comment.text.strip()
                if text in seen_comments:
                    continue  # skip duplicates
                seen_comments.add(text)

                data.append({
                    "name": name.text.strip(),
                    "comment": text,
                    "likes": like.text.strip() if like.text.strip() else "0"
                })

                if len(data) >= self.max_comments:
                    break

            # Scroll more aggressively to load new comments
            self.driver.execute_script("window.scrollBy(0, 2000);")
            time.sleep(3)

        df = pd.DataFrame(data)
        os.makedirs("data", exist_ok=True)
        df.to_csv(settings.OUTPUT_CSV, index=False)
        return df





