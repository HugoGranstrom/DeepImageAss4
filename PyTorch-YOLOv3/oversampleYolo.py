import os

traintxt = "data/custom/train.txt"

classToMultiply = {
  0: 1, #fish
  1: 2,#jellyfish
  2: 2,#penguin
  3: 4,#puffin
  4: 3,#shark
  5: 10,#starfish
  6: 5#stingray
}

with open(traintxt, 'r') as f:
  original = f.read()

print(len(original))

new_content = original + "\n"

for line in original.splitlines():
  filename = os.path.basename(line)
  name, extension = os.path.splitext(filename)
  txt_filename = name + ".txt"
  with open(os.path.join("data/custom/labels", txt_filename)) as f:
    classes = []
    for bbox in f.read().splitlines():
      class_idx, x, y, w, h = bbox.split(" ")
      classes.append(int(class_idx))
    mul = max([classToMultiply[x] for x in classes], default=1)
  new_content += (mul-1) * (line + '\n')
  #print(mul, classes)

print(len(new_content))

with open(traintxt, 'w') as f:
  f.write(new_content)