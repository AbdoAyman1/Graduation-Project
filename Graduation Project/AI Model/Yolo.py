from PIL import Image
import os
from keras.models import load_model
import numpy as np
import random
import matplotlib.pyplot as plt
from ultralytics import YOLO

os.chdir(r'D:\Graduation project\New folder (2)\Traffic_Sign_Recognition\Traffic_Sign_Recognition')
model = load_model("TSR.h5")
imageDimesions = (64, 64 , 3)
# Classes of trafic signs
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

model = YOLO("yolov8n.pt")

# result = model.predict(source=0,show=True,conf=0.4,save=True)

def test_on_img(img):
    data = []
    image = Image.open(img)
    # Convert to grayscale
    image = image.convert('L')
    image = image.resize((imageDimesions[0], imageDimesions[1]))
    data.append(np.array(image))
    X_test = np.array(data)
    # Reshape for model input
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)
    Y_pred = model.predict(X_test)
    classes_x = np.argmax(Y_pred, axis=1)
    return image, classes_x

plot,prediction = test_on_img(r'D:\Graduation project\New folder (2)\Traffic_Sign_Recognition\Traffic_Sign_Recognition\Test\00010.png')
s = [str(i) for i in prediction] 
a = int("".join(s)) 
print("Predicted traffic sign is: ", classes[a])
plt.imshow(plot)
plt.show()

# def get_random_test_image(test_folder):
#     test_images = [f for f in os.listdir(test_folder) if f.endswith('.png')]
#     random_image = random.choice(test_images)
#     return os.path.join(test_folder, random_image)

# def test_on_random_img(model, test_folder):
#     random_img_path = get_random_test_image(test_folder)
#     plot, prediction = test_on_img(random_img_path)
    
#     s = [str(i) for i in prediction] 
#     a = int("".join(s)) 
#     print("Predicted traffic sign is: ", classes[a])
    
#     plt.imshow(plot)
#     plt.show()

# # Example usage:
# test_folder_path = r'C:\Users\abdoa\OneDrive\Desktop\proj\Test'
# test_on_random_img(model, test_folder_path)