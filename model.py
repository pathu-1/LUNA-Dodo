import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array

sar_classification_model = load_model("sar_model.h5")


sar_classes = ["2S1", "BRDM_2", "BTR_60", "D7", "SLICY", "T62", "ZIL_131", "ZSU_24_3"]
def sar_class_prediction(sar_image_path):
    sar_image_ = load_img(sar_image_path, target_size=(224, 224))

    sar_image_ = img_to_array(sar_image_)
    sar_image_ = tf.expand_dims(sar_image_, axis=0)/255.

    output_ = tf.argmax(sar_classification_model(sar_image_), axis=1)
    return sar_classes[int(output_.numpy())]






