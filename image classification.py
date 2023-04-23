# -*- coding: utf-8 -*-
"""Image_Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vzWSqEn-Dg-5zE9b5YqEbg1U8qURnfGY

Here we will taking cifar10 dataset and traing our labels to correctly recoganize the images
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# dataset is already present in keras so we will just call the load function and divide our data set into 2 tuples of trainiong and testing

(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()

# we will scale down the pixels or you say normalise the data as the values of pixel is between 0 to 255 so we will do it as 0 and 1 for our convinent

training_images, testing_images = training_images/255, testing_images/255

# we will defne a class with all the 10 types of imagesd names

class_names = ['Plane', 'Car', 'Bird','Cat','Deer', 'Dog','Frog', 'Horse', 'Ship', 'Truck']
#we will be able to classify all these things
#it is important here tio maintain an order in which the things are there in the dataset otherwise wrong output will be generated

# we will be viewing 16 of thye images so for this purpose we will be using 4X4 matric

for i in range(16):
  plt.subplot(4,4,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(training_images[i], cmap = plt.cm.binary)
  plt.xlabel(class_names[training_labels[i][0]])
plt.show()

# as we can see that the images  are not of good quality so we need to train our neural network precisiolyu

# we will reduce the number of images
training_images = training_images[:20000]
training_labels = training_labels[:20000]
testing_images = testing_images[:5000]
testing_labels = testing_labels[:5000]

# builing neural network

#de3fining a simple sequential model
model = models.Sequential()
#defining the input layer
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))
#adding a maxpooling layer to simply and keep only essential info
model.add(layers.MaxPooling2D((2,2)))
#adding another layer
model.add(layers.Conv2D(64, (3,3), activation='relu'))
#adding another maxpoooling layer
model.add(layers.MaxPooling2D((2,2)))
#Adding last convolutional layer
model.add(layers.Conv2D(64, (3,3), activation='relu'))
#Adding a flatten layer to make input of one dimension
model.add(layers.Flatten())
#adding 2 dense layers one for proseeing and last one for output layer
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
#softmax scales all the result so they all add up to one like in percentasge so sum of all becomes one

# now we will compile the model and define our optimizer, loss function and accuracy measure
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# we will fit our model on training images
model.fit(training_images, training_labels, epochs=20, validation_data=(testing_images, testing_labels))

# adjust the number of espochs as per the accuracy
# is we can see an observable increasing accuracy then increase the number of epochs

loss, accuracy = model.evaluate(testing_images, testing_labels)
print(f"loss: {loss}")
print(f"accuracy: {accuracy}")
#this will print the loss and accuracy of our testingf model

# we can save the model and simply call it next timew when we will need it instead of always running all the codes
model.save('image_classification.model')
# we can wrte img = models.load_model('model_name')
#to simply load the model directly
