# importing libs / packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import random
# importig local classes
from home_page import HomePage
from login_page import LoginPage
from search_bar import SearchBar

# setting environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# taking the tags to use as hashtag
tags_req = requests.get('http://api.quotable.io/tags').json()

# putting the tags on a list
tag_list = []

for tag in range(len(tags_req)):
    tag = tags_req[tag]['name']
    tag_list.append(tag)

# removing the tag 'famous-quotes' - no hashtag on instagram
tag_list.remove('famous-quotes')

# choosing a random tag
random_tag = random.choice(tag_list)

# installing and using theb chrome drive
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5)

# acessing the instagram home page
home_page = HomePage(browser)

# logging in the instagram with email and password (env variables)
login_page = LoginPage(browser)
login_page.login(EMAIL, PASSWORD)

# searching tags
search_bar = SearchBar(browser)
search_bar.search_hashtag(random_tag)

# closing the instagram bot
browser.close()


