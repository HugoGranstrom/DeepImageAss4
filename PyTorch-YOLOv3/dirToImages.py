"""
Used to generate data/custom/train.txt from folder with the images
"""

import os

targetDir = "data/custom/images/"
trainOrVal = "test"
outputfile = f"data/custom/{trainOrVal}.txt"

content = ""
for filename in os.listdir(f"data/{trainOrVal}/images"):
  #print(targetDir + filename)
  content += targetDir + filename + "\n"

print(content)
with open(outputfile, "w") as f:
  f.write(content)
