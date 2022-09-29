from instaloader import Instaloader, Profile, Post
from utils.string import handle_url


class InstaLoaderAPI:
    def __init__(self, username):
        instaloader = Instaloader()

        self.username = username
        self.instaloader = instaloader
        self.profile = Profile.from_username(instaloader.context, username)

    def dowloadPost(self, url):
        shortCode = handle_url(url)
        post = Post.from_shortcode(self.instaloader.context, shortCode)
        self.instaloader.download_post(post, self.username)
