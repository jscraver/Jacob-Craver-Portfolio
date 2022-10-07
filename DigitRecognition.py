######################################################################################################################
# Name: Joseph Brown, Jacob Craver, Jonathan Wellmeyer
# Date: 5/18/2020
# Description: The uses the picamera to take a picture of a digit which it then recognizes.
######################################################################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from PIL import Image
from picamera import PiCamera
import cairo
from time import sleep
import PIL.ImageOps


camera = PiCamera()

class Picture(object):
    def recognizeImage(self, event):
        # Takes a picture
        camera.start_preview()
        sleep(5)
        camera.stop_preview()
        camera.capture("number.jpg")
        # Opens the image
        original_im = Image.open("number.jpg")
        original = original_im.crop((160, 0, 640, 480))
        original = np.array(original)
        original = np.dot(original, [0.2989, 0.5870, 0.1140])
        original.shape = (480, 480)

        # Inverts the image color
        im = PIL.ImageOps.invert(original_im)
        im.save("number.jpg")

        # Opens the inverted image, then crops, resizes and converts it to an grayscale image array
        im = Image.open("number.jpg")
        im = im.crop((160, 0, 640, 480))
        size = (28, 28)
        im = im.resize(size, resample = Image.BILINEAR)
        im = np.array(im)
        im = np.dot(im, [0.2989, 0.5870, 0.1140])

        # list of total pixels
        lst = []

        # Puts every pixel into a list
        for i in im:
            for x in i:
                x = round(x)
                x = int(x)
                lst.append(x)

        # If the color of a pixel is dark, it makes it completely black
        for i in range(len(lst)):
            if lst[i] < 160:
                lst[i] = 0
        
        xtrain = []
        train_label = []

        # Gets the data from a csv file
        data = pd.read_csv("shortened_mnist_train.csv").as_matrix()

        clf = DecisionTreeClassifier()

        # Creates the training set for the data
        xtrain = data[0:30807, 1:]

        # Gets the labels for each row in the data
        train_label = data[0:30807, 0]

        # Uses the decision tree classifier to machine learn using the training set along with the labels
        clf.fit(xtrain, train_label)

        # Uses the desision tree classifier to predict the value of the data.
        prediction = clf.predict([lst])

        # For each possible prediction, it will display an image of the predicted number along with
        # the original picture in the GUI
        if prediction[0] == 0:
            image = Image.open("Images/Zero.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 0")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 1:
            print 1
            image = Image.open("Images/One.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 1")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 2:
            image = Image.open("Images/Two.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 2")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 3:
            image = Image.open("Images/Three.JPG")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 3")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 4:
            image = Image.open("Images/Four.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 4")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 5:
            image = Image.open("Images/Five.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 5")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 6:
            image = Image.open("Images/Six.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 6")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 7:
            image = Image.open("Images/Seven.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 7")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 8:
            image = Image.open("Images/Eight.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 8")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

        elif prediction[0] == 9:
            image = Image.open("Images/Nine.jpg")
            image = np.array(image)
            image = np.dot(image, [0.2989, 0.5870, 0.1140])
            image.shape = (480, 480)
            
            fig = plt.figure("Images")
            ax = fig.add_subplot(1,2,1)
            ax.set_title("Picture")
            plt.imshow(original, cmap = plt.cm.gray)
            plt.axis("off")

            ax = fig.add_subplot(1,2,2)
            ax.set_title("Prediction: 9")
            plt.imshow(image, cmap = plt.cm.gray)
            plt.axis("off")

            plt.show()

    # A function used to close the GUI window
    def stop(self, event):
        plt.close()


#############################################################################
# MAIN
#############################################################################

# Creates the window along with the buttons
fig = plt.figure("Images")
callback = Picture()
axpicture = plt.axes([.12, .025, .38, .1])
axstop = plt.axes([.5, .025, .38, .1])
stop = Button(axstop, "Quit")
picture = Button(axpicture, "Take Picture")
stop.on_clicked(callback.stop)
picture.on_clicked(callback.recognizeImage)

# Displays the GUI when the code is run.
plt.show()

