import cv2
import time
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

config = tf.ConfigProto(
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
    # device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
set_session(session)

img_width = 128
img_height = 128

cap = cv2.VideoCapture(1)
print('capturing')
test_datagen = ImageDataGenerator(rescale=1. / 255)

val_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=False)

model = load_model('model_keras4.h5')
print('model loaded')

# i = 0
# while(i<50):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     i+=1
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     time.sleep(0.1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    try:
        cv2.imshow('frame', frame)
    except Exception as e:
        print(str(e))

    frame = cv2.resize(frame, (img_width, img_height),
                       interpolation=cv2.INTER_CUBIC)
    frame = frame / 255
    try:
        preds = model.predict(np.expand_dims(frame, axis=0))[0][0]
    except Exception as e:
        print(str(e))

    if(preds > 0.85):
        print('Car Spotted')
    else:
        print('no car')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.5)

cap.release()
cv2.destroyAllWindows()
