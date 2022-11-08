import requests
import os

fileSave = r"D:\Arquivos\TCC\server\saves\base_image.png"

img_data = requests.get("https://dev.virtualearth.net/REST/v1/Imagery/Map/AerialWithLabels?pp=33.537716,-88.032289,19;&mapSize=1920,1080&zoomLevel=19&key=AmgMwslLVEnaaAIzvJ_DckOn8PXbZOytAshy3dFAMmwQN6ex_DoujM6EQSpGFF0s").content
with open(fileSave, 'wb') as handler:
    handler.write(img_data)