import numpy as np 
import cv2 
import os 
from keras.models import load_model 
from ultralytics import YOLO
import drivers
from time import sleep

# Initialize the LCD (16x2 characters)
display = drivers.Lcd()

os.chdir(r'/home/abdo/Desktop') 
frameWidth = 1280 
frameHeight = 720 
threshold = 0.5   
font = cv2.FONT_HERSHEY_SIMPLEX 
 
cap = cv2.VideoCapture(0) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight) 
 
# Load the traffic sign classification model 
try: 
    tsmodel = load_model("TSR4.h5") 
    print("Model loaded successfully.") 
except Exception as e: 
    print(f"Error loading model: {e}") 
 
def preprocessing(img): 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    img = cv2.equalizeHist(img) 
    img = img / 255.0 
    print("Preprocessing successful.") 
    return img 
 
def getClassName(classNo): 
    class_names = ['Speed Limit 20 km/h', 'Speed Limit 30 km/h', 'Speed Limit 50 km/h', 'Speed Limit 60 km/h',  
                   'Speed Limit 70 km/h', 'Speed Limit 80 km/h', 'End of Speed Limit 80 km/h', 'Speed Limit 100 km/h',  
                   'Speed Limit 120 km/h', 'No passing', 'No passing for vehicles over 3.5 metric tons',  
                   'Right-of-way at the next intersection', 'Priority road', 'Yield', 'Stop', 'No vehicles',  
                   'Vehicles over 3.5 metric tons prohibited', 'No entry', 'General caution',  
                   'Dangerous curve to the left', 'Dangerous curve to the right', 'Double curve', 'Bumpy road',  
                   'Slippery road', 'Road narrows on the right', 'Road work', 'Traffic signals', 'Pedestrians',  
                   'Children crossing', 'Bicycles crossing', 'Beware of ice/snow', 'Wild animals crossing',  
                   'End of all speed and passing limits', 'Turn right ahead', 'Turn left ahead', 'Ahead only',  
                   'Go straight or right', 'Go straight or left', 'Keep right', 'Keep left', 'Roundabout mandatory',  
                   'End of no passing', 'End of no passing by vehicles over 3.5 metric tons'] 
    return class_names[classNo] if 0 <= classNo < len(class_names) else "Unknown" 
 
model = YOLO("yolov5s.pt") 
 
while True: 
    success, imgOriginal = cap.read() 
    if not success: 
        print("Failed to capture image.") 
        break 
    img_traffic_sign = cv2.resize(imgOriginal, (96, 96)) 
    img_traffic_sign = preprocessing(img_traffic_sign) 
    img_traffic_sign = img_traffic_sign.reshape(1, 96, 96, 1) 
     
    # Perform prediction using the traffic sign classification model 
    predictions_traffic_sign = tsmodel.predict(img_traffic_sign) 
    print(f"Predictions: {predictions_traffic_sign}") 
    classIndex_traffic_sign = np.argmax(predictions_traffic_sign) 
    probabilityValue_traffic_sign = predictions_traffic_sign[0, classIndex_traffic_sign] 
    print(f"Class: {classIndex_traffic_sign}, Probability: {probabilityValue_traffic_sign}") 
     
    # Display traffic sign classification results if probability is above threshold 
    if probabilityValue_traffic_sign > threshold: 
        classIndex_traffic_sign = int(classIndex_traffic_sign)  # Convert classIndex to integer 
        cv2.putText(imgOriginal, f"{classIndex_traffic_sign} {getClassName(classIndex_traffic_sign)}", 
                    (20, 40), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA) 
        cv2.putText(imgOriginal, f"{round(probabilityValue_traffic_sign * 100, 2)}%", (20, 60), font, 
                    0.75, (0, 0, 255), 2, cv2.LINE_AA) 
        
        # Update LCD display for various traffic signs
        if classIndex_traffic_sign == 14:  # Stop sign has index 14
            display.lcd_display_string("STOP", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()
        
        elif classIndex_traffic_sign == 7:  # Speed Limit 100 km/h sign has index 7
            display.lcd_display_string("Speed Limit 100", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()

        elif classIndex_traffic_sign == 33:  # Turn Right Ahead sign has index 33
            display.lcd_display_string("Turn Right Ahead", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()
        
        elif classIndex_traffic_sign == 34:  # Turn Left Ahead sign has index 34
            display.lcd_display_string("Turn Left Ahead", 1)  # Display on line 1
            sleep(2)
            display.lcd_clear()
        
    try: 
        results = model.predict(source=imgOriginal, show=True, stream=True) 
        print("YOLO prediction successful.") 
    except Exception as e: 
        print(f"YOLO prediction error: {e}") 
        
    # Exit condition 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        print("Exiting.") 
        break 
 
# Clean up 
cap.release() 
cv2.destroyAllWindows()
