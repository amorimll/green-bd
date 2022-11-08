from ast import Str
from tkinter import Image
from flask import Flask, request
from flask import jsonify
from flask import request
import requests
from deepforest import main
from deepforest import get_data
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt
from google.cloud import storage

model = main.deepforest()
model.use_release()


UPLOAD_FOLDER = 'saves'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/teste", methods=["GET"])
# def authe():
    # """Uploads a file to the bucket."""
    # # The ID of your GCS bucket
    # bucket_name = "gs://green-app-de1e3.appspot.com"
    # # The path to your file to upload
    # source_file_name = "./saves/drvores.jpg" 
    # # The ID of your GCS object
    # destination_blob_name = "Teste"

    # storage_client = storage.Client(project="green-app-de1e3")
    # bucket = storage_client.bucket(bucket_name)
    # blob = bucket.blob(destination_blob_name)

    # blob.upload_from_filename(source_file_name)

    # print(
    #     f"File {source_file_name} uploaded to {destination_blob_name}."
    # )
    # return "Ok"

@app.route("/postImagem", methods=["POST"])
def post_articles():
    # lat 33.526681
    # lon -87.964842,18
    key = "AmgMwslLVEnaaAIzvJ_DckOn8PXbZOytAshy3dFAMmwQN6ex_DoujM6EQSpGFF0s"
    lat = request.form['latitude']
    lon = request.form['longitude']


    urlApi = "https://dev.virtualearth.net/REST/v1/Imagery/Map/AerialWithLabels?pp=" + lat + "," + lon + ";&mapSize=1920,1080&zoomLevel=19&key=" + key
    img_data = requests.get(urlApi).content
    fileSave = r"D:\Arquivos\TCC\client\pics\baseImage.jpg"
    with open(fileSave, 'wb') as handler:
        handler.write(img_data)
    img_path = get_data(fileSave)
    img = model.predict_image(path=img_path, return_plot=False)
    print(len(img.head(9999)))
    
    print("FORM: " + str(request.form))
    print("DATA: " + str(request.data))
    print("FILES: " + str(request.files))
    return str(len(img.head(9999)))

if __name__== "__main__":
    app.run(host="192.168.1.93", port=5000, debug=True)