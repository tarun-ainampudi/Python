import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.filters import roberts

def edge_detection(path):
    a = cv2.imread(path)
    a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    f = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
    g = roberts(f)
    g = (g / g.max() * 255).astype(np.uint8)
    return g

for i in range(1,6):
    g=edge_detection(f"output{i}.png")
    cv2.imwrite(f"output{i}.png", g)
    img = Image.open(f"output{i}.png").convert("RGBA")
    img.save(f"output{i}.png")