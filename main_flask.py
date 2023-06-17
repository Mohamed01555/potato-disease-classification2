from flask import Flask, request
from flask_cors import CORS
from keras.models import load_model
from PIL import Image
from io import BytesIO
import numpy as np

app = Flask(__name__)
CORS(app)

model = load_model("backend/potatoes.h5", compile=False)

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# def read_file_as_image(data) -> np.ndarray:
#     image = Image.open(BytesIO(data))
    
#     image = image.resize((256,256))
#     # print(np.array(image).shape)
    
#     return np.array(image)[:,:,:3]

@app.route("/predict", methods=['POST'])
def predict():
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(request.files['file'])
    image = np.array(image.resize((256,256)))[:,:,:3]
    
    img_batch = np.expand_dims(image, 0)
    
    predictions = model.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }
if __name__ =='__main__':
	#app.debug = True
	app.run(host='localhost', port=8000)