import cv2
import numpy as np
import pickle


names = "Mr Stepen"
classes= "RDA"
# create a dictionary that would carry both the known_names and the known_encodings
data = {"face_encodings" : names,
        "names" : classes}

# open a binary file and write the dictionary to the binary file
with open("face_enrollment", "wb") as f:
    f.write(pickle.dumps(data))