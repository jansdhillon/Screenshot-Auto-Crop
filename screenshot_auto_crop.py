from PIL import Image
import glob
import os
# get desktop path


def crop():
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    path = desktop + "/*.png"
    # use glob to get the most recent file
    filelist = glob.glob(path)
    most_recent = max(filelist, key=os.path.getmtime)
    # Open the image
    img = Image.open(most_recent)
    # Crop the image to the approximate size of the desired region of my Mac screen.
    # Plans to make this more dynamic and implement other monitors in the future.
    img = img.crop((0, 80, 3024, 1850))
    # Save the image
    img.save(most_recent)
    return most_recent
