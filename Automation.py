import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

# Set up undetected Chrome driver
options = webdriver.ChromeOptions()
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")  # Random user agent
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
driver = webdriver.Chrome(options=options)

# Open TikTok
driver.get("https://www.tiktok.com/login")
time.sleep(15)  # Give time for manual login

def random_delay(min_time=3, max_time=7):
    """Generate a random delay to mimic human behavior."""
    time.sleep(random.uniform(min_time, max_time))

def engage_with_hashtag(hashtag, comment_text):
    """Searches for videos by hashtag, likes, comments, and follows users."""
    driver.get(f"https://www.tiktok.com/search?q={hashtag}")
    random_delay(5, 10)

    videos = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/video/"]')
    
    for i, video in enumerate(videos[:5]):  # Engage with first 5 videos
        try:
            print(f"Engaging with video {i + 1}")
            video.click()
            random_delay(5, 10)
            
            # Like the video
            try:
                like_button = driver.find_element(By.CSS_SELECTOR, 'span[data-e2e="like-icon"]')
                like_button.click()
                print("✅ Liked a video!")
            except:
                print("❌ Like button not found.")

            # Follow the user
            try:
                follow_button = driver.find_element(By.XPATH, '//button[contains(text(), "Follow")]')
                follow_button.click()
                print("✅ Followed the user!")
            except:
                print("❌ Follow button not found.")

            # Comment on the video
            try:
                comment_box = driver.find_element(By.CSS_SELECTOR, 'div[data-e2e="comment-textarea"]')
                comment_box.click()
                random_delay()
                comment_box.send_keys(comment_text)
                comment_box.send_keys(Keys.RETURN)
                print("✅ Commented on a video!")
            except:
                print("❌ Could not comment.")

            random_delay(5, 10)

            # Scroll to simulate browsing
            driver.execute_script("window.scrollBy(0, 500);")
            random_delay(5, 10)

            # Go back
            driver.execute_script("window.history.go(-1)")
            random_delay(5, 10)
        
        except Exception as e:
            print(f"⚠ Error engaging with video {i + 1}: {e}")

# Run engagement with multiple hashtags
hashtags = ["moviebites", "whattowatch", "moviescenes"]
comments = ["🔥 This is inspiring!", "Great content! 💯", "Keep going! 🚀"]

for hashtag in hashtags:
    engage_with_hashtag(hashtag, random.choice(comments))

# Close browser after engagement
random_delay(5, 10)
driver.quit()
