import cv2
import numpy
from tensorflow.keras.models import load_model




def classify_image(image_path):
    image_classification_model = load_model("./image_classification_model.keras")
    label_classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

    image = cv2.imread(image_path)
    image = cv2.resize(image, (32, 32))
    image = image / 255.0
    image = numpy.expand_dims(image, axis=0)
    predict = image_classification_model.predict(image)
    print(predict)
    predicted_class_index = numpy.argmax(predict)
    print(predicted_class_index)
    print(label_classes[predicted_class_index])
    return label_classes[predicted_class_index]

