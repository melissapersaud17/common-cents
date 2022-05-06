import numpy as np
from flask import Flask, request
from flask_cors import CORS
from keras.models import load_model
from PIL import Image, ImageOps

# Creates Flask app instance, and allows any CORS request
app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload():
    # Load the model
    model = load_model('keras_model.h5', compile=False)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(request.files['file'])
    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    prediction = prediction[0].tolist()

    max_value = max(prediction)

    prediction_index = prediction.index(max_value)

    result = None
    if prediction_index == 0:
        result = '$1 Bill'
    elif prediction_index == 1:
        result = '$5 Bill'
    elif prediction_index == 2:
        result = '$10 Bill'
    elif prediction_index == 3:
        result = '$20 Bill'
    elif prediction_index == 4:
        result = '$50 Bill'
    elif prediction_index == 5:
        result = '$100 Bill'

    return {"message": result}
