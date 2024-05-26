import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException

EMAIL = "talukdersuvam@gmail.com"
PASSWORD = "suvamtalukder321"

# Keep Edge browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# Create and configure the Edge webdriver
driver = webdriver.Edge(options=edge_options)

# Navigate to the (fake) newsletter registration page
driver.get("https://tinder.com/")

time.sleep(2)
cookie_decline = driver.find_element(By.XPATH, '//*[@id="c315867768"]/div/div[2]/div/div/div[1]/div[2]/button')
cookie_decline.click()

time.sleep(2)
log_in = driver.find_element(By.XPATH, '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

# time.sleep(2)
# more_options = driver.find_element(By.XPATH, '//*[@id="c537208204"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
# more_options.click()

time.sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="c537208204"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
fb_email = driver.find_element(value="email")
fb_email.send_keys(EMAIL)
fb_password = driver.find_element(value="pass")
fb_password.send_keys(PASSWORD, Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
location_allow = driver.find_element(By.XPATH, '//*[@id="c537208204"]/main/div/div/div/div[3]/button[1]')
location_allow.click()

time.sleep(2)
notification_button = driver.find_element(By.XPATH, '//*[@id="c537208204"]/main/div/div/div/div[3]/button[2]')
notification_button.click()

i=3
time.sleep(5)
dislike = driver.find_element(By.XPATH, '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
dislike.click()
for like in range(5):
    time.sleep(5)
    try:
        print("called")

        dislike = driver.find_element(By.XPATH, '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        dislike.click()

    except ElementClickInterceptedException:
        try:
            print("Don't know what happened?")
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            print("passed")
            pass

    i+=1
    time.sleep(2)

    # '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button'
    # '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'
    # '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'
    # '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'
    # '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'