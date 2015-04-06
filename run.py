"""
Run this to keep the tweet stream open till the system runs.
"""
import os
import time

print "Starting Stream"
count = 0
while True:
    count += 1
    print count
    os.system("python stream.py")
    os.system("python tweet_processing.py")
    os.system("python vsm.py")
    time.sleep(900)
