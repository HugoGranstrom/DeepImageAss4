import os
from bs4 import BeautifulSoup

traintxt = "dataset-test/ImageSets/Main/train.txt"
trainvaltxt = "dataset-test/ImageSets/Main/trainval.txt"

classToMultiply = {
  0: 1, #fish
  1: 2,#jellyfish
  2: 2,#penguin
  3: 4,#puffin
  4: 3,#shark
  5: 10,#starfish
  6: 5#stingray
}

stringToClass = {
  'fish': 0,
  'jellyfish': 1,
  'penguin': 2,
  'puffin': 3,
  'shark': 4,
  'starfish': 5,
  'stingray': 6
}

with open(traintxt, 'r') as f:
  original = f.read()

print(original.count('\n'))

new_content = original + "\n"

for line in original.splitlines():
  name = line
  txt_filename = name + ".xml"
  with open(os.path.join("dataset-test/Annotations", txt_filename)) as f:
    classes = []
    Bs_data = BeautifulSoup(f.read(), "xml")
    bboxes = Bs_data.find_all('name')
    #print(bboxes)
    for bbox in bboxes:
      class_idx = stringToClass[bbox.contents[0]]
      classes.append(int(class_idx))
    mul = max([classToMultiply[x] for x in classes], default=1)
  new_content += (mul-1) * (name + '\n')
  #print(mul, classes)

print(new_content, new_content.count('\n'))

with open(traintxt, 'w') as f:
  f.write(new_content)

with open(trainvaltxt, 'w') as f:
  f.write(new_content)

