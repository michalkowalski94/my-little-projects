import numpy as np
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense, Conv2D, GlobalMaxPooling2D

#Standarizing and altering training input
train_datagen = image.ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
#Setting Seed
np.random.seed(95)

#Standarizing validation input
valid_datagen = image.ImageDataGenerator(rescale=1./255)

batch_size=40

#Setting data generators with flow from category
train_generator = train_datagen.flow_from_directory(
        '../input/training/training',
        batch_size=batch_size,
        class_mode='categorical')

valid_generator = valid_datagen.flow_from_directory(
        '../input/validation/validation',
        batch_size=batch_size,
        class_mode='categorical')

#Creating model

model = Sequential()

model.add(Conv2D(32, (3,3), activation = 'relu', input_shape=(None,None,3))) #Input as images in different shapes
model.add(Conv2D(64, (3,3), activation = 'relu', padding = 'same'))
model.add(Conv2D(64, (3,3), activation = 'relu', padding = 'same'))
model.add(GlobalMaxPooling2D()) #Pooling max values to 1D tensor instead of flattening
model.add(Dense(1024, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
#Categorizing on the folder basis
hist = model.fit_generator(
        train_generator,
        steps_per_epoch=1098 // batch_size,
        epochs=100,
        validation_data=valid_generator,
        validation_steps=272 // batch_size)

#Training accuracy: about 90%
#Validation accuracy: about 75%

#To do: edit and fine tune
