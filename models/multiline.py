import cv2
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.python.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam



def initialize_model(transferlearned_weights):
    vg12 = Sequential()

    pretrained_model = tf.keras.applications.VGG16(
        input_shape=(224,224,3),
        include_top=False,
        weights="imagenet",
        input_tensor=None,
        pooling="avg",
        classes=2
    )

    for layer in pretrained_model.layers:
            layer.trainable=False

    vg12.add(pretrained_model)
    vg12.add(Flatten())
    vg12.add(Dense(512, activation='relu'))
    vg12.add(Dense(2, activation='softmax'))
    vg12.load_weights(transferlearned_weights)
    return vg12


def process_image(image_path):
    image=cv2.imread(image_path)
    img_height,img_width=224,224
    image_resized= cv2.resize(image, (img_height,img_width))
    image=np.expand_dims(image_resized,axis=0)
    model = initialize_model(r"E:\Study materials\IIT\4th year\FYP\Codes\sinhala_handwriting_error_detection-main\weigths\multi_line_model_epochs_10.h5")
    pred=model.predict(image)
    probability =float(str(round(max(pred[0]),3)))
   
    class_names = ['issue', 'normal']
    output_class=class_names[np.argmax(pred)]
    return {"class":output_class , "probability":probability}
