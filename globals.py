from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from home_page import Home_page
# from trending_page import trending


PATH = 'C:\\Users\\Raunak\\Desktop\\YouTube_Parser\\chromedriver.exe'

class global_class():
    titles=[]
    driver=webdriver.Chrome(PATH)
    action=ActionChains(driver)
    action1=ActionChains(driver)
    play_video='y'
    ans='n'
    i=0

    def get_contents(self,id):  
        if id==1:
            outer_content=WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.ID,"primary")))
            outer_content_2=outer_content.find_element_by_id('contents')
            inner_contents=outer_content_2.find_element_by_id("contents")
            contents=inner_contents.find_elements_by_tag_name("ytd-video-renderer")
            return contents

              
        elif id==2:
            outer_content=WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.TAG_NAME,"ytd-item-section-renderer")))
            outer_content_2=outer_content.find_element_by_id('contents')
            inner_contents=outer_content_2.find_element_by_id("contents")
            contents=inner_contents.find_elements_by_tag_name("ytd-video-renderer")
            return contents

            
        elif id==3:
            outer_content=WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.ID,"primary")))
            inner_contents=outer_content.find_element_by_id("contents")
            contents=inner_contents.find_elements_by_tag_name("ytd-rich-item-renderer")
            return contents

    def parse_contents(self,contents,id=1):
        for content in contents:   
            if (id==1) and (content.find_element_by_id("title-wrapper")):
                heading=content.find_element_by_id("title-wrapper")
                title=heading.find_element_by_tag_name("yt-formatted-string")
                self.titles.append(title)
                print(title.text)
                self.i+=1
                if self.i % 3==0:
                    self.ans=input("do you want more videos?(y/n): ")
                    if self.ans=='y':
                        pass
                    else:
                        break
            elif (id==0) and (content.find_element_by_id("details")):
                heading=content.find_element_by_id("details")
                title=heading.find_element_by_tag_name("yt-formatted-string")
                self.titles.append(title)
                print(title.text)
                self.i+=1
                if self.i%4==0:
                    self.ans=input("do you want more videos?(y/n): ")
                    if self.ans=='y':
                        pass
                    else:
                        break
    def watch_title_video(self,titles,video_title):
        for title in self.titles:
                if video_title in title.text:
                    self.action.move_to_element(title)
                    self.action.click()
                    self.action.perform()
        self.watch_video()

    def update_player_status(self):
            status=self.driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
            return status

    def send_key(self):
        self.driver.find_element_by_tag_name('body').send_keys('k')
        self.driver.implicitly_wait(10) 

    def process_ad(self):
        ad=self.driver.find_element_by_class_name("ytp-ad-preview-container")
        if ('ad' in ad.find_element_by_class_name('ytp-ad-text').text):
            pass  
        elif not (self.driver.find_element_by_class_name("ytp-ad-preview-container").get_attribute('display')=='none'):
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_class_name("ytp-ad-skip-button").click()
            self.driver.implicitly_wait(5)
            player_status = self.update_player_status()
            return player_status

    def watch_video(self):
        self.play_video='y'
        while self.play_video=='y':
                self.driver.implicitly_wait(5)
                player_status = self.update_player_status()
                if player_status==-1:
                    try: 
                        self.process_ad()
                    except:
                        print('ad skipped or missed')    
                elif player_status==1:
                    ans=input('do you want to pause the video? ')
                    if ans=='y':
                        self.send_key()
                                 
                elif player_status==2:
                    ans=input('do you want to play the video? ')
                    if ans=='y':
                        self.send_key()     
                    else:
                        ans_video=input('do you want to quit the video? ')
                        if ans_video=='y':
                            self.driver.execute_script("window.history.go(-1)")
                            self.play_video='n'
                elif player_status==0:
                    ans=input('do you want to play the video again? ')
                    if ans=='y':
                        self.send_key()
                    

# page_type = ""
# page = trending()
# trending_categories = page.get_categories(page.trending_categories)
# for i in range(len(trending_categories)):
#     print(trending_categories[i])