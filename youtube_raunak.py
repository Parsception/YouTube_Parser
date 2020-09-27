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


# search_title=''

# search_title=input("enter the name of the video you want to search: ")
# driver=webdriver.Chrome(PATH)
# driver.get("https:\\www.youtube.com")

# titles=[]

# search = driver.find_element_by_name("search_query")
# search.send_keys(search_title)
# search.send_keys(Keys.RETURN)

# action=ActionChains(driver)

# # try:
# outer_content=WebDriverWait(driver,15).until(
#     EC.presence_of_element_located((By.ID,"content"))
# )

# outer_content_2=outer_content.find_element_by_id('contents')


# inner_contents=outer_content_2.find_element_by_id("contents")


# contents=inner_contents.find_elements_by_tag_name("ytd-video-renderer")


# for content in contents:   
#     if(content.find_element_by_id("title-wrapper")):
#         heading=content.find_element_by_id("title-wrapper")
#         title=heading.find_element_by_tag_name("yt-formatted-string")
#         titles.append(title)
#         print(title.text)
#         i+=1
#         if i % 3==0:
#             ans=input("do you want more videos?(y/n): ")
#             if ans=='y':
#                 pass
#             else:
#                 break
# video_title=input("enter the video title: ")
# for title in titles:
#     if video_title in title.text:
#         action.move_to_element(title)
#         action.click()
#         action.perform()
# #playing/pausing youtube video            
# play_video='y'


# while play_video=='y':
#     driver.implicitly_wait(5)
#     player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
#     if player_status==-1:
#         try: 
#             ad=driver.find_element_by_class_name("ytp-ad-preview-container")
#             if ('ad' in ad.find_element_by_class_name('ytp-ad-text').text):
#                 pass  
#             elif not (driver.find_element_by_class_name("ytp-ad-preview-container").get_attribute('display')=='none'):
#                 driver.implicitly_wait(2)
#                 driver.find_element_by_class_name("ytp-ad-skip-button").click()
#                 driver.implicitly_wait(5)
#                 player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
#         except:
#             print('ad skipped or missed')    
#     elif player_status==1:
#         ans=input('do you want to pause the video? ')
#         if ans=='y':
#             driver.find_element_by_tag_name('body').send_keys('k')
#             driver.implicitly_wait(10)
            
#     elif player_status==2:
#         ans=input('do you want to play the video? ')
#         if ans=='y':
#             driver.find_element_by_tag_name('body').send_keys('k')
#             driver.implicitly_wait(10) 
#         else:
#             ans_video=input('do you want to quit the video? ')
#             if ans_video=='y':
#                 driver.execute_script("window.history.go(-1)")
#                 driver.implicitly_wait(10) 
#     elif player_status==0:
#         ans=input('do you want to play the video again? ')
#         if ans=='y':
#             driver.find_element_by_tag_name('body').send_keys('k')
#             driver.implicitly_wait(10)

#going back to the previous video


# except:
#     driver.quit() 