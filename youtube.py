from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\\Users\\guppr\\Desktop\\YouTube\\chromedriver.exe'

driver=webdriver.Chrome(PATH)
driver.get("https:\\www.youtube.com")

search = driver.find_element_by_name("search_query")
search.send_keys("testing")
search.send_keys(Keys.RETURN)


try:
    outer_contents=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"contents"))
    )

    
    inner_contents=outer_contents.find_element_by_id("contents")

    contents=inner_contents.find_elements_by_class_name("ytd-item-section-renderer")

    
    for content in contents:
        if(content.find_element_by_id("video-title")):
            heading=content.find_element_by_id("video-title")
            # print(heading.title.encode("uft-8"),'abcdcdc')
            print(heading.text.encode("utf-8"))

finally:
    driver.quit()

