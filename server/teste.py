from deepforest import main
from deepforest import get_data
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
model = main.deepforest()
model.use_release()

img_path= r"D:\Arquivos\TCC\server\saves\drvores.jpg"
img_path2= get_data(r"D:\Arquivos\TCC\server\saves\drvores.jpg")
img = model.predict_image(path=img_path, return_plot=True)
img2 = model.predict_image(path=img_path2, return_plot=False)

i = 0
print (str(len(img2.head(9999))))

for n in range(len(img2)):
    i+=1

cv2.putText(img, 'Arvores: '+ str(len(img2.head(9999))), (3,4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.imshow('Output', img)
cv2.waitKey(0)