from trending_page import trending
from youtube_raunak import search_youtube
from home_page import Home_page

# page = trending()
# page.get_categories()
# page.get_videos()
# page.video_title("Taaron Ke Shehar Song")
# you=search_youtube()
# you.search_video("test")
# you.video_title("This Crazy Test Can")

hp=Home_page()
hp.get_video_titles()
ans=input("enter title")
hp.video_title(ans)