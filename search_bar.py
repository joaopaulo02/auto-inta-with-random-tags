'''Classe to search hashtags in instagram'''

from time import sleep

class SearchBar:
    def __init__(self, browser):
        self.browser = browser

    def search_hashtag(self, hashtag):
        '''searching hashtags'''
        search_bar = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(hashtag)
        self.browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        sleep(5)


        
