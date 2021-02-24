import os
import sys
from PIL import Image

def JPGtoPNGConverter(source, dest):
  """
  Extract all the files from the source folder.
  Check whether dest folder exists otherwise create new.
  Check all source files are in .jpg format
  If yes, convert into PNG format
  If not, show that file in the output
  """
  files = os.listdir(f"./{source}")
  if not os.path.exists(f"./{dest}"):os.makedirs(f"./{dest}")

  for file in files:
    if os.path.splitext(file)[-1] == ".jpg":
      img = Image.open(f"./{source}/{file}")
      clean_text = os.path.splitext(file)[0]
      img.save(f"./{dest}/{clean_text}.png","png")
    else:
      print(f"Your filename: {file} is not in .JPG format !!")
  return "All files converted successfully :) "

# Converting files from JPG to PNG
print(JPGtoPNGConverter(source = "ImageProcessing", dest = 'New_image'))

