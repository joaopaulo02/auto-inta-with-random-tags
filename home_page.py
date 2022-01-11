'''Classe to access the instagram home page'''

from time import sleep
from login_page import LoginPage

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')