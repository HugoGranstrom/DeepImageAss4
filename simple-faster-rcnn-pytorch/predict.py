import torch
from model import FasterRCNNVGG16, VGG16RoIHead
from trainer import FasterRCNNTrainer

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os, glob
from utils.vis_tool import vis_bbox

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



faster_rcnn = FasterRCNNVGG16()
faster_rcnn.head = VGG16RoIHead(
            n_class=7 + 1,
            roi_size=7,
            spatial_scale=(1. / faster_rcnn.feat_stride),
            classifier=faster_rcnn.head.classifier
        ).to(device)
trainer = FasterRCNNTrainer(faster_rcnn, visualize=False).to(device)
trainer.load("checkpoints/best_37.pth")

net = trainer.faster_rcnn
net.eval()


jpeg_path = "dataset-test/JPEGImages/"
img_path = "dataset-test/JPEGImages/IMG_2354_jpeg_jpg.rf.396e872c7fb0a95e911806986995ee7a.jpg"

img_paths = []
filenames = []
with open("dataset-test/ImageSets/main/test.txt") as f:
  for line in f.read().splitlines():
    img_paths.append(os.path.join(jpeg_path, line + ".jpg"))
    filenames.append(line + ".jpg")

images = []
sizes = []
for path in img_paths:
  im = Image.open(path)
  size = np.array(im.size)
  im = np.moveaxis(np.asarray(im), -1, 0).astype('float32')
  images.append(im)
  sizes.append(size)

matplotlib.use('TkAgg')

with torch.no_grad():
  net.eval()
  _bboxes, _labels, _scores = net.predict(images, sizes, visualize=True)
  print(_bboxes)
  print(_labels)
  print(_scores)
  for i in range(len(images)):
    fig = plt.figure()
    ax = plt.axes()
    vis_bbox(images[i], _bboxes[i], label=_labels[i], score=_scores[i], ax=ax)
    plt.savefig(os.path.join("output/", filenames[i]))
