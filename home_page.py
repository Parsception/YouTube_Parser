from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from globals import global_class

class Home_page(global_class):

    def __init__(self):
        self.driver.get("https:\\www.youtube.com")

    def get_video_titles(self):
        contents=self.get_contents(3)
        self.parse_contents(contents,0)
        return
    def video_title(self,video_title):
        self.watch_title_video(self.titles,video_title)
        return
