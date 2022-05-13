"""
Given folder containing:
- train/
  img1.jpg
  img1.xml
- valid/
  img2.jpg
  img2.xml

Make folder containing:
- Annotations/
  img1.xml
  img2.xml
- ImageSets/
  - Main/
    train.txt: img1
    val.txt: img2
- JPEGImages/
  img1.jpg
  img2.jpg
"""

import os, glob, pathlib, shutil

dataset_folder = "aquarium_data"
train_folder = os.path.join(dataset_folder, "train")
valid_folder = os.path.join(dataset_folder, "valid")
test_folder = os.path.join(dataset_folder, "test")

dest_dir = "dataset-test"
anno_dir = os.path.join(dest_dir, "Annotations")
imageset_dir = os.path.join(dest_dir, "ImageSets", "Main")
jpeg_dir = os.path.join(dest_dir, "JPEGImages")
try:
  os.mkdir(dest_dir)
  os.mkdir(anno_dir)
  os.makedirs(imageset_dir)
  os.mkdir(jpeg_dir)
except OSError:
  #exit(f"Directory '{dest_dir}' already exists, delete it before running this!")
  shutil.rmtree(dest_dir)
  os.mkdir(dest_dir)
  os.mkdir(anno_dir)
  os.makedirs(imageset_dir)
  os.mkdir(jpeg_dir)

train_names = [] # will be saved into train.txt

for file_path in glob.glob(os.path.join(train_folder, "*.jpg")):
  filename = os.path.basename(file_path)
  name, extension = os.path.splitext(filename)
  train_names.append(name)
  xml_filename = name + ".xml"
  xml_path = os.path.join(train_folder, xml_filename)
  print(xml_path)
  shutil.copyfile(file_path, os.path.join(jpeg_dir, filename))
  shutil.copyfile(xml_path, os.path.join(anno_dir, xml_filename))

train_content = ""
for name in train_names:
  train_content += name + "\n"
train_content = train_content[:-1]

with open(os.path.join(imageset_dir, "train.txt"), "w") as f:
  f.write(train_content)


valid_names = [] # will be saved into val.txt

for file_path in glob.glob(os.path.join(valid_folder, "*.jpg")):
  filename = os.path.basename(file_path)
  name, extension = os.path.splitext(filename)
  valid_names.append(name)
  xml_filename = name + ".xml"
  xml_path = os.path.join(valid_folder, xml_filename)
  print(xml_path)
  shutil.copyfile(file_path, os.path.join(jpeg_dir, filename))
  shutil.copyfile(xml_path, os.path.join(anno_dir, xml_filename))

valid_content = ""
for name in valid_names:
  valid_content += name + "\n"
valid_content = valid_content[:-1]

with open(os.path.join(imageset_dir, "val.txt"), "w") as f:
  f.write(valid_content)


test_names = [] # will be saved into test.txt

for file_path in glob.glob(os.path.join(test_folder, "*.jpg")):
  filename = os.path.basename(file_path)
  name, extension = os.path.splitext(filename)
  test_names.append(name)
  xml_filename = name + ".xml"
  xml_path = os.path.join(test_folder, xml_filename)
  print(xml_path)
  shutil.copyfile(file_path, os.path.join(jpeg_dir, filename))
  shutil.copyfile(xml_path, os.path.join(anno_dir, xml_filename))

test_content = ""
for name in test_names:
  test_content += name + "\n"
test_content = test_content[:-1]

with open(os.path.join(imageset_dir, "test.txt"), "w") as f:
  f.write(test_content)


trainval_content = ""
for name in valid_names + train_names:
  trainval_content += name + "\n"
trainval_content = trainval_content[:-1]

with open(os.path.join(imageset_dir, "trainval.txt"), "w") as f:
  f.write(trainval_content)







