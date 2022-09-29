from InstaLoaderAPI import InstaLoaderAPI

username = "p4bl1sk1_t3st"  # input("Insert a profile name: ")
url = 'https://www.instagram.com/p/Ch_5wqpDAqB/'


instaLoaderAPI = InstaLoaderAPI(username)

instaLoaderAPI.dowloadPost(url)
