import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

# === User inputs the TikTok username ===
username = input("Enter the TikTok username: ")

# === Set up Selenium with an undetected driver ===
options = webdriver.ChromeOptions()
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")  # Random User-Agent to prevent detection
options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

driver = webdriver.Chrome(options=options)

# === Open TikTok & Go to the User's Profile ===
driver.get(f"https://www.tiktok.com/@artspace")
time.sleep(random.uniform(5, 10))  # Randomized delay

def random_delay():
    """Generates a random delay to mimic human-like interaction."""
    time.sleep(random.uniform(3, 7))

# === Engage with videos ===
try:
    videos = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/video/"]')
    
    for i, video in enumerate(videos[:3]):  # Interact with the first 3 videos
        print(f"Interacting with video {i + 1}")

        video.click()
        random_delay()

        # Like the video
        try:
            like_button = driver.find_element(By.CSS_SELECTOR, 'span[data-e2e="like-icon"]')
            like_button.click()
            print("✅ Liked the video!")
        except:
            print("❌ Like button not found.")

        # Comment on the video
        try:
            comments = ["🔥 Nice!", "Loved this!", "Cool video!", "🔥🔥🔥"]
            comment_box = driver.find_element(By.CSS_SELECTOR, 'div[data-e2e="comment-textarea"]')
            comment_box.click()
            random_delay()
            comment_box.send_keys(random.choice(comments))
            comment_box.send_keys(Keys.RETURN)
            print("✅ Commented on the video!")
        except:
            print("❌ Could not comment.")

        random_delay()
        driver.execute_script("window.history.go(-1)")  # Go back to the profile page
        random_delay()

except Exception as e:
    print(f"⚠ Error: {e}")

# === Close Browser After Engagement ===
random_delay()
driver.quit()
