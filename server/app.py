from flask import Flask
from flask import jsonify
from flask import request
from deepforest import main
from deepforest import get_data
import cv2
import os
import matplotlib.pyplot as plt
model = main.deepforest()
model.use_release()

img_path= get_data(r"D:\Arquivos\TCC\client\pics\florestas.png")
img = model.predict_image(path=img_path, return_plot=False)

# cv2.imshow('Output', img)
# cv2.waitKey(0)

app = Flask(__name__)

@app.route("/teste", methods=["GET"])
def get_articles():
    return str(len(img.head(9999)))

@app.route("/", methods=["POST"])
def post_articles():
    if request.method == "POST":
        return 'Teste'

if __name__== "__main__":
    app.run(host="192.168.1.93", port=5000, debug=True)