sleep 1
export DISPLAY=":0.0"
screen -dmS IG sh -c 'python3 InstaPost/quickpost.py; exec bash'
sleep 1
screen -ls
