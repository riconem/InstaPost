import os
import InstaPost
import load_image as load
import time
import schedule
import random

hashtags = "#hashtag1, #hashtag2, #hashtag3"
name = 'name'
pwd = 'password'

driverpath = os.path.dirname(os.path.realpath(__file__)) + "/assets/chromedriver"

#opens browser and login
status = load.queue_is_filled()
if status == False:
    print("Nothing to Upload!")
else:
    uploading = load.new_image_upload()
    post = InstaPost.InstaPost(name, pwd, driverpath)
    post.signIn()
    post.newpost(uploading, hashtags)
    post.closeBrowser()