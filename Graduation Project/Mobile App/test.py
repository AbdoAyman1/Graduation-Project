
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import os
from keras.models import load_model


app = Flask(__name__)
CORS(app)
# Load your machine learning model here
# Example: model = load_model('your_model.h5')
model_path = os.path.abspath('lib/training1/TSR.h5')
model = load_model(model_path)
# Classes of traffic signs
classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)', 
            2:'Speed limit (50km/h)', 
            3:'Speed limit (60km/h)', 
            4:'Speed limit (70km/h)', 
            5:'Speed limit (80km/h)', 
            6:'End of speed limit (80km/h)', 
            7:'Speed limit (100km/h)', 
            8:'Speed limit (120km/h)', 
            9:'No passing', 
            10:'No passing veh over 3.5 tons', 
            11:'Right-of-way at intersection', 
            12:'Priority road', 
            13:'Yield', 
            14:'Stop', 
            15:'No vehicles', 
            16:'Veh > 3.5 tons prohibited', 
            17:'No entry', 
            18:'General caution', 
            19:'Dangerous curve left', 
            20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing veh > 3.5 tons' }

def test_on_img(img):
    data = []
    image = Image.open(img)
    image = image.resize((30, 30))
    data.append(np.array(image))
    X_test = np.array(data)
    Y_pred = model.predict(X_test)
    classes_x = np.argmax(Y_pred, axis=1)
    return image, classes_x

@app.route('/predict_traffic_sign', methods=['POST'])
def predict_traffic_sign():
    try:
        # Get the image file from the request
        img = request.files['image']

        # Process the image and get predictions
        plot, prediction = test_on_img(img)
        s = [str(i) for i in prediction]
        a = int("".join(s))
        predicted_class = classes[a]  # Ensure you have 'classes' defined somewhere

        # Return the predicted class
        response_data = {'predicted_class': predicted_class}

        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

    