from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import globals

class Home_page:
    titles=[]

    def get_name(self):
        try:
            outer_contents=WebDriverWait(globals.driver,10).until(
                EC.presence_of_element_located((By.ID,"contents"))
            )
            contents=outer_contents.find_elements_by_tag_name("ytd-rich-item-renderer")
            for content in contents:
                if(content.find_element_by_id("video-title-link")):
                    title=content.find_element_by_id("video-title-link").get_attribute("aria-label")
                    print(title)
                    self.titles.append(title)

        except:
            globals.driver.quit()

