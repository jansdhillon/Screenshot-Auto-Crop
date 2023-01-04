from PIL import Image, ImageEnhance, ImageFilter
import glob
import os

if __name__ == '__main__':
    # Path to the folder containing the screenshots
    path = '/Users/imigh/Desktop/*.png'
    filelist = glob.glob(path)
    most_recent = max(filelist, key=os.path.getmtime)
    print(most_recent)
    img = Image.open(most_recent)
    # Crop the image
    img = img.crop((0, 60, 3024, 1850))
    # Save the image
    img.save(most_recent)
    
