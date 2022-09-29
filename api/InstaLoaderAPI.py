from instaloader import Instaloader, Profile, Post
from utils.string import handle_url


class InstaLoaderAPI:
    def __init__(self, username = "instagram", password  = None):
        instaloader = Instaloader()
        instaloader.save_metadata = False
        instaloader.download_video_thumbnails = False
        instaloader.post_metadata_txt_pattern = ''

        self.instaloader = instaloader

        if (username and password):
            self.username = username
            self.instaloader.login(self.username, password)

    def dowloadPostFromShortCode(self, shortCode):
        post = Post.from_shortcode(self.instaloader.context, shortCode)
        self.instaloader.download_post(post, self.username)

    def dowloadPostFromURL(self, url):
        shortCode = handle_url(url)
        self.dowloadPostFromShortCode(shortCode)
