import subprocess
import glob
import os
import time
import screenshot_auto_crop

#Wait for screenshot popup to disappear
time.sleep(6)

#Call crop function from screenshot_auto_crop.py
most_recent = screenshot_auto_crop.crop()

#Show in finder
subprocess.call(["open", "-R", most_recent])
