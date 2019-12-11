from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome("F:\Python\Projects\ChromeWebdriver\chromedriver.exe")

# Variables
my_mail = os.environ.get('MAIN_MAIL_USERNAME')
my_linkedin_password = os.environ.get('linkedinPassword')
SEARCH_WORDS = 'Full stack developer'
pages = 5
url = "https://www.linkedin.com/"

# Open the URL and click on the first Sign in button
driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_link_text('Sign in').click()
time.sleep(2)

# Enter email
username = driver.find_element_by_id('username')
username.click()
username.send_keys(my_mail)
# Enter password
password = driver.find_element_by_id('password')
password.click()
password.send_keys(my_linkedin_password)
# Click Sign in
driver.find_element_by_xpath('/html/body/div/main/div/form/div[3]/button').click()
time.sleep(3)

# Search by our words
search_bar = driver.find_element_by_xpath('/html/body/header/div/form/div/div/div/div/div[1]/div/input')
search_bar.send_keys(SEARCH_WORDS)
time.sleep(2)
search_bar.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)

# Filter by Israel
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[2]/form/button').click()
israel_checkbox = driver.find_element_by_id('geoRegion-il:0')
driver.execute_script("arguments[0].click();", israel_checkbox)
driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div/ul/li[2]/form/div/fieldset/div/div[2]/div/button[2]').click()
print("Filtering by Locations: Israel")


def connect_all_on_page():
    # Connect 10 people on page
    for _ in range(1,11):
        try:
            connect_btn = driver.find_element_by_xpath(f'/html/body/div[6]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[{_}]/div/div/div[3]/div/button')
            driver.execute_script("arguments[0].click();", connect_btn)
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
            print(f"Sent connect to number {_}")
            time.sleep(2)
        except:
            print(f"Can't connect to number {_}")


on_page = 1
while on_page <= pages:
    print(f'Page: {on_page}')
    connect_all_on_page()
    # Scroll to the bottom
    time.sleep(2)
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.END)
    time.sleep(2)
    # Clicking Next page
    try:
        next_page = driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[2]/artdeco-pagination/button[2]')
    except:
        next_page = driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/artdeco-pagination/button[2]')
    driver.execute_script("arguments[0].click();", next_page)
    on_page += 1
    time.sleep(2)
