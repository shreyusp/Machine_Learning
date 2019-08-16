from keras.models import model_from_json
json_file=open('model5epoch.json')

jsonfile=json_file.read()
json_file.close()

model=model_from_json(json_file)
model.load_weights('model5epoch.h5)

import numpy as np
from keras.preprocessing import image
testImage=image.load_img('dataset/sample1.jpg',target_size=(64,64))
testImage=image.img_to_array(testImage)