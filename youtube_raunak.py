from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from globals import global_class



class search_youtube(global_class):
    
    def __init__(self):
        self.driver.get("https:\\www.youtube.com")

    def search_video(self,title):
        search = self.driver.find_element_by_name("search_query")
        search.send_keys(title)
        search.send_keys(Keys.RETURN)
        self.search_results()
    
    def search_results(self):
        contents=self.get_contents(1)
        self.parse_contents(contents)
        return

    def video_title(self,video_title):
        self.watch_title_video(self.titles,video_title)
        return