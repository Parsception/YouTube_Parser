from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from globals import global_class



class trending(global_class):
    def __init__(self):
        self.trending_categories=[]
        self.driver.get("https://www.youtube.com/feed/trending")

    def get_categories(self):
        try:
            outer_contents=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"sub-menu")))
            inner_contents=outer_contents.find_element_by_id("contents")
            categories=inner_contents.find_elements_by_tag_name("ytd-channel-list-sub-menu-avatar-renderer")
            for category in categories:
                if(category.find_element_by_id("title")):
                    category_name=category.find_element_by_id("title")
                    self.trending_categories.append(category_name)
                else:
                    print("no")
            self.select_category()
        except:
            self.driver.quit()
    def select_category(self):
        print("The categories are: ")
        for i in range(len(self.trending_categories)):
            print(self.trending_categories[i].text)
        print(self.trending_categories)

        category=input('enter the category you want to select: ')

        for trending_category in self.trending_categories:
            print(i)
            if category in trending_category.text:

                self.action1.move_to_element(trending_category)
                self.action1.click()
                self.action1.perform()
                break
        return


    def get_videos(self):
        contents = self.get_contents(2)
        self.parse_contents(contents)
    def video_title(self,video_title):
        self.watch_title_video(self.titles,video_title)
        
        return


