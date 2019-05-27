#!/bin/bash
sudo apt-get update
sudo apt-get install chromium-browser

#required
mkdir files assets
mkdir files/logs files/queue
touch files/logs/uploaded.txt files/logs/uploaded_img.txt
chmod +w files/logs/uploaded.txt files/logs/uploaded_img.txt

cd assets
#if this driver won't work you have to download a newer version.It depends on your chromium-browser or chrome.
wget https://github.com/electron/electron/releases/download/v5.0.2/chromedriver-v5.0.2-linux-armv7l.zip
unzip chromedriver-v5.0.2-linux-armv7l.zip
