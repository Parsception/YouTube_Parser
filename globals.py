from selenium import webdriver
from home_page import home_page
from trending_page import trending

PATH = 'C:\\Users\\guppr\\Desktop\\YouTube\\chromedriver.exe'


global driver, page_type, page
page_type = ""
page = trending()
trending_categories = page.get_categories(page.trending_categories)
for i in range(len(trending_categories)):
    print(trending_categories[i])