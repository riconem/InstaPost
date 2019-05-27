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

def posting():
	status = load.queue_is_filled()
	if status == False:
		print("Nothing to Upload!")
		return schedule.CancelJob
	#load new image to uploading stage
	uploading = load.new_image_upload()

	#opens browser and login
	post = InstaPost.InstaPost(name, pwd, driverpath)
	post.signIn()
	post.newpost(uploading, hashtags)
	post.closeBrowser()

schedule.every().day.at("16:02").do(posting)
#schedule.every(5).minutes.do(posting)

status = load.queue_is_filled()
if status == False:
	print("Nothing to Upload!")

while status == True:
	schedule.run_pending()
	time.sleep(10)