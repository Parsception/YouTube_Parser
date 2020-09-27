from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\\Users\\guppr\\Desktop\\YouTube\\chromedriver.exe'

class home_page:
    def __init__(self):
        chips=[]

    def get_chips(self):

        try:
            outer_contents=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID,"ytd-feed-filter-chip-bar-renderer"))
            )

            
            #inner_contents=outer_contents.find_element_by_id("scroll-container")

            chips=outer_contents.find_elements_by_class_name("yt-chip-cloud-chip-renderer")

            
            for chip in chips:
                if(content.find_element_by_id("text")):
                    chip_name=content.find_element_by_id("text")
                    # print(heading.title.encode("uft-8"),'abcdcdc')
                    print(chip_name.text.encode("utf-8"))

        finally:
            driver.quit()

