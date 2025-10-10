import pickle

from selenium import webdriver

# initialize Chrome driver
driver = webdriver.Chrome()

driver.get("https://www.python.org")
# Save cookies
with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

# Load cookies
with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)


driver.quit()