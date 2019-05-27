import os
import shutil
import sys
import datetime

filepath = os.path.dirname(os.path.realpath(__file__))
projectpath = '%s/files' %filepath
imagepath = '%s/queue' %projectpath
uploadedpath = '%s/uploaded' %projectpath
uploaded_log = '%s/logs/uploaded.txt' %projectpath
uploaded_count = '%s/logs/uploaded_img.txt' %projectpath

uploading = '%s/uploading.jpg' %projectpath

def move_upload_image():
	for file in os.listdir(projectpath):
		if file != "queue" and file != "logs" and file != "uploaded":
			uploaded = '%s/%s' %(projectpath, file)
			shutil.move(uploaded, uploadedpath)

def writelog(text):
	if os.path.exists(uploaded_log):
		log = open(uploaded_log, "a+")
		log.write("\n")
		log.write("%s" %text)
	else:
		log = open(uploaded_log, "w")
		log.write("%s" %text)

def check_image(image):
	if os.path.exists(uploaded_log):
		file = open(uploaded_log, "r")
		for line in file.readlines():
			nline = line.replace("\n", "")
			string = nline.split("; ")
			if image == string[1]:
				return True

def get_uploaded_count():
	if os.path.exists(uploaded_log):
		count=0
		file = open(uploaded_log, "r")
		for line in file.readlines():
			count += 1
		opencount = open(uploaded_count, "w")
		opencount.write("%s" %count)

def new_image_upload():
	images = []
	for image in os.listdir(imagepath):
		real_imagepath = "%s/%s" %(imagepath, image)
		if ".jpg" in image or ".JPG" in image or ".jpeg" in image or ".PNG" in image or ".png" in image:
			if check_image(image) == True:
				os.remove(real_imagepath)
			else: images.append(image)
		else: os.remove(real_imagepath)

	if len(images) > 0:
		images.sort(reverse=True)
		upload_image = images[0]
		upload_image_path = "%s/%s" %(imagepath, upload_image)
		print("\nUploading: %s\n" %upload_image_path)
		log ="%s; %s" %(datetime.datetime.now().date(), upload_image)
		writelog(log)
		get_uploaded_count()
		return upload_image_path
	else: 
		print("Done! All images uploaded in queue.")
		return False
def queue_is_filled():
	images=[]
	for image in os.listdir(imagepath):
		images.append(image)
	if len(images) == 0:
		return False
	else: return True
