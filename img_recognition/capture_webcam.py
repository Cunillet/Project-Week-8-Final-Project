import numpy as np
import cv2
import time
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.losses import SparseCategoricalCrossentropy


# general vars
img_shape = (150, 150)
animal_names = {
    'butterfly': 0,
    'cat': 1,
    'chicken': 2,
    'cow': 3,
    'human': 4,
    'elephant': 5,
    'horse': 6,
    'sheep': 7,
    'spider': 8,
    'squirrel': 9,
    '0': 'butterfly',
    '1': 'cat',
    '2': 'chicken',
    '3': 'cow',
    '4': 'human',
    '5': 'elephant',
    '6': 'horse',
    '7': 'sheep',
    '8': 'spider',
    '9': 'squirrel'
}

# recover model
model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(img_shape[0], img_shape[1], 3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(128, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(10, activation='sigmoid')
])
model.compile(optimizer='adam',
              loss=SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
model.load_weights('img_recognition/data/checkpoints/animals_model_3')

# start capturing img
cap = cv2.VideoCapture(0)
animal_captured = ''
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resize img
    img_resized = cv2.resize(frame, img_shape, interpolation=cv2.INTER_AREA)

    # change frmo 1..255 to 0..1
    img_resized = img_resized / 255

    # predict
    predicted = model.predict_classes(np.asarray([img_resized]))[0]

    animal_predicted = animal_names[str(predicted)]
    # check if the animal has changed
    if animal_captured != animal_predicted:
        animal_captured = animal_predicted
        print(animal_captured)
    cv2.putText(frame, animal_captured, (100,150), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255),2)
    cv2.imshow('my webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # esc to quit

    #time.sleep(0.5)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()