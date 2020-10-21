###### Update: This script isn't working anymore! 😐

# InstaPost
Short Python script to post pictures automatically on Instagram.
The main code is based on Tim Grossmanns automated Instagram Tool https://github.com/timgrossmann/InstaPy.



# Installation on Rasbian Desktop
A desktop environment is required for this script. I wasn't able to get it working in the background. :D
```
git clone "https://github.com/riconem/InstaPost.git"
cd InstaPost
chmod +x install.sh
./install.sh
```
# Setup your posts
Add your files you want to upload in ```files/queue```.
Edit login and hashtag in ```quickpost.py ``` or ```post24.py```.
```
hashtags = "#hashtag1, #hashtag2, #hashtag3"
name = 'name'
pwd = 'password'
```
## Execute
If you want to execute via ssh, export your Display variable
```
export DISPLAY="0.0"
python quickpost.py
```
## Execute by crontab weekly
```
crontab -e
```
Add your cronjob. This example will execute the script every Tuesday on 4 PM. 
```
0 16 * * TUE /home/pi/InstaPost/post.sh
```
