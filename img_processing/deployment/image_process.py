import numpy as np
from PIL import Image
from utils import *

def process_captured_image(file_path):
    # Load labels, preprocess image, and load the model
    labels = gen_labels()
    image = Image.open(file_path)
    img = preprocess(image)
    model = model_arc()
    model.load_weights("../weights/model.h5")

    # Make prediction
    prediction = model.predict(img[np.newaxis, ...])
    
    # Get the predicted label
    predicted_label = labels[np.argmax(prediction[0], axis=-1)]

    if predicted_label in ["metal", "glass", "trash","plastics"]:
        predicted_label = "non-degrade"
    if predicted_label in ["cardboard","paper"]:
        predicted_label ="degrade"

    # Print the predicted label
    print(" - Predicted waste type: {}".format(predicted_label))

    return predicted_label

if __name__=="__main__":
    process_captured_image("./captured_image.jpg")
