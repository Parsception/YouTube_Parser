from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\\Users\\guppr\\Desktop\\YouTube\\chromedriver.exe'

class trending:
    def __init__(self):
        self.trending_categories=[]

    def get_categories(self,trending_categories):

        try:
            driver=webdriver.Chrome(PATH)
            driver.get("https://www.youtube.com/feed/trending")   
            
            outer_contents=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"sub-menu")))
            inner_contents=outer_contents.find_element_by_id("contents")
            categories=outer_contents.find_elements_by_tag_name("ytd-channel-list-sub-menu-avatar-renderer")
            for category in categories:
                #inner=category.find_elements_by_class_name("yt-simple-endpoint style-scope ytd-channel-list-sub-menu-avatar-renderer")
                if(category.find_element_by_id("title")):
                    category_name=category.find_element_by_id("title")
                    # print(heading.title.encode("uft-8"),'abcdcdc')
                    trending_categories.append(category_name.text.encode("utf-8"))
                else:
                    print("no")

        finally:
            driver.quit()

        return trending_categories


