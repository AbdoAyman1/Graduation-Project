import tensorflow as tf
from keras import layers, models
from keras.optimizers import Adam
from keras.losses import SparseCategoricalCrossentropy
import numpy as np
from sklearn.model_selection import train_test_split
import os
import cv2
import matplotlib.pyplot as plt
import random
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical


path = r"D:\Graduation project\New folder (2)\Traffic_Sign_Recognition\Traffic_Sign_Recognition\Train"
labelFile = r'D:\Graduation project\New folder (2)\Traffic_Sign_Recognition\Traffic_Sign_Recognition\labels.csv'
batch_size_val = 64
epochs_val = 7
imageDimesions = (32, 32, 3)
testRatio = 0.2
validationRatio = 0.2

count = 0
images = []
classNo = []
myList = os.listdir(path)
print("Total Classes Detected:", len(myList))
noOfClasses = len(myList)
print("Importing Classes.....")
for x in range(0, len(myList)):
    myPicList = os.listdir(path+"/"+str(count))
    for y in myPicList:
        curImg = cv2.imread(path+"/"+str(count)+"/"+y)
        # Resize the image to a consistent size (32x32)
        curImg = cv2.resize(curImg, (imageDimesions[0], imageDimesions[1]))
        images.append(curImg)
        classNo.append(count)
    print(count, end=" ")
    count += 1
print(" ")

images = np.array(images)
classNo = np.array(classNo)

X_train, X_test, y_train, y_test = train_test_split(images, classNo, test_size=testRatio)
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validationRatio)

# X_train = ARRAY OF IMAGES TO TRAIN
# y_train = CORRESPONDING CLASS ID

print("Data Shapes")
print("Train",end = "");print(X_train.shape,y_train.shape)
print("Validation",end = "");print(X_validation.shape,y_validation.shape)
print("Test",end = "");print(X_test.shape,y_test.shape)
assert(X_train.shape[0]==y_train.shape[0]), "The number of images in not equal to the number of lables in training set"
assert(X_validation.shape[0]==y_validation.shape[0]), "The number of images in not equal to the number of lables in validation set"
assert(X_test.shape[0]==y_test.shape[0]), "The number of images in not equal to the number of lables in test set"
assert(X_train.shape[1:]==(imageDimesions))," The dimesions of the Training images are wrong "
assert(X_validation.shape[1:]==(imageDimesions))," The dimesionas of the Validation images are wrong "
assert(X_test.shape[1:]==(imageDimesions))," The dimesionas of the Test images are wrong"

data=pd.read_csv(labelFile)
print("data shape ",data.shape,type(data))

num_of_samples = []
cols = 5
num_classes = noOfClasses
fig, axs = plt.subplots(nrows=num_classes, ncols=cols, figsize=(5, 300))
fig.tight_layout()
for i in range(cols):
    for j,row in data.iterrows():
        x_selected = X_train[y_train == j]
        axs[j][i].imshow(x_selected[random.randint(0, len(x_selected)- 1), :, :], cmap=plt.get_cmap("gray"))
        axs[j][i].axis("off")
        if i == 2:
            axs[j][i].set_title(str(j)+ "-"+row["Name"])
            num_of_samples.append(len(x_selected))
print(num_of_samples)
plt.figure(figsize=(12, 4))
plt.bar(range(0, num_classes), num_of_samples)
plt.title("Distribution of the training dataset")
plt.xlabel("Class number")
plt.ylabel("Number of images")
plt.show()

def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img =cv2.equalizeHist(img)
    return img
def preprocessing(img):
    img = grayscale(img)     # CONVERT TO GRAYSCALE
    img = equalize(img)      # STANDARDIZE THE LIGHTING IN AN IMAGE
    img = img/255            # TO NORMALIZE VALUES BETWEEN 0 AND 1 INSTEAD OF 0 TO 255
    return img
 
X_train=np.array(list(map(preprocessing,X_train)))  # TO IRETATE AND PREPROCESS ALL IMAGES
X_validation=np.array(list(map(preprocessing,X_validation)))
X_test=np.array(list(map(preprocessing,X_test)))
# cv2.imshow("GrayScale Images",X_train[random.randint(0,len(X_train)-1)]) # TO CHECK IF THE TRAINING IS DONE PROPERLY

X_train=X_train.reshape(X_train.shape[0],X_train.shape[1],X_train.shape[2],1)
X_validation=X_validation.reshape(X_validation.shape[0],X_validation.shape[1],X_validation.shape[2],1)
X_test=X_test.reshape(X_test.shape[0],X_test.shape[1],X_test.shape[2],1)

dataGen= ImageDataGenerator(width_shift_range=0.05,   # 0.1 = 10%     IF MORE THAN 1 E.G 10 THEN IT REFFERS TO NO. OF  PIXELS EG 10 PIXELS
                            height_shift_range=0.05,
                            zoom_range=0.1,  # 0.2 MEANS CAN GO FROM 0.8 TO 1.2
                            shear_range=0.1,  # MAGNITUDE OF SHEAR ANGLE
                            rotation_range=10)  # DEGREES
dataGen.fit(X_train)
batches= dataGen.flow(X_train,y_train,batch_size=20)  # REQUESTING DATA GENRATOR TO GENERATE IMAGES  BATCH SIZE = NO. OF IMAGES CREAED EACH TIME ITS CALLED
X_batch,y_batch = next(batches)
 
# TO SHOW AGMENTED IMAGE SAMPLES
fig,axs=plt.subplots(1,15,figsize=(20,5))
fig.tight_layout()
 
for i in range(15):
    axs[i].imshow(X_batch[i].reshape(imageDimesions[0],imageDimesions[1]))
    axs[i].axis('off')
plt.show()
 
 
y_train = to_categorical(y_train,noOfClasses)
y_validation = to_categorical(y_validation,noOfClasses)
y_test = to_categorical(y_test,noOfClasses)

# Resize images to 224x224 and normalize pixel values to [0, 1]
images = [tf.image.resize(img, (32, 32)).numpy() / 255.0 for img in images]

# Convert to numpy arrays
images = np.array(images)
labels = np.array(classNo)

# Split data into training, validation, and test sets
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)
train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.2, random_state=42)

def create_vit_model(imageDimesions, num_classes, num_patches=16, embedding_dim=80, num_layers=6, num_heads=6):
    # Input layer
    inputs = layers.Input(shape=imageDimesions)

    # Patch Embedding layer
    patch_size = imageDimesions[0] // num_patches
    patch_emb = layers.Conv2D(embedding_dim, kernel_size=patch_size, strides=patch_size)(inputs)
    patch_emb = layers.Reshape((num_patches * num_patches, embedding_dim))(patch_emb)

    # Transformer Encoder layers
    x = patch_emb
    for _ in range(num_layers):
        x = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embedding_dim)(x, x)
        x = layers.LayerNormalization(epsilon=1e-6)(x)
        x = layers.Dense(4 * embedding_dim, activation='relu')(x)
        x = layers.Dense(embedding_dim)(x)
        x = layers.LayerNormalization(epsilon=1e-6)(x)

    # Classification head
    x = layers.GlobalAveragePooling1D()(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    # Create model
    model = models.Model(inputs, outputs)
    return model

# Define the model
num_classes = len(np.unique(labels))
vit_model = create_vit_model(imageDimesions, num_classes)

# Define optimizer and loss function
optimizer = Adam(learning_rate=0.0001)
loss_function = SparseCategoricalCrossentropy()


vit_model.compile(optimizer=optimizer, loss=loss_function, metrics=['accuracy'])

# Train the model
vit_model.fit(train_images, train_labels, epochs=epochs_val, validation_data=(val_images, val_labels))  # Increase epochs to 10

# Evaluate the model on the test set
test_loss, test_accuracy = vit_model.evaluate(test_images, test_labels)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")
vit_model.save("vit.h5")

