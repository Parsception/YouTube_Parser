from trending_page import trending
from youtube_raunak import search_youtube

page = trending()
page.get_categories()
page.get_videos()
page.video_title("Taaron Ke Shehar Song")
# you=search_youtube()
# you.search_video("test")
# you.video_title("This Crazy Test Can")