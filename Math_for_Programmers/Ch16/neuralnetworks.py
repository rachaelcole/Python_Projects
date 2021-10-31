# Artificial neural networks are mathematical functions whose structure is loosely based on the structure
# of the human brain. We can think of the activation of a neuron in a neural network as the function of 
# numerical activation values of neurons it is connected to. If a neuron connects to four others with the
# activation values a1, a2, a3, and a4, then its activation will be some mathematical function applied to
# those four values, say, f(a1, a2, a3, a4).

# The goal is to build a neural network that looks at 8x8 pixel images of digits and classifies them
# as one of ten digits from 0 to 9. The neural network classification function will be a non-linear
# vector transformation with 64 inputs and 10 outputs. The inputs are the pixel darkness values scaled
# from 0 to 1, and the ten output values represent how likely the image is to be any of ten digits. The 
# index of the largest output number is the answer.

# Due to the form of the functions connecting neurons in our neural network, there's a shortcut algorithm
# for taking the gradient, which is called backpropagation. We will use the Python library scikit-learn
# to do the gradient descent.
from math import exp
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

# Helper functions:
def sigmoid(x):
    return 1 / (1+exp(-x))

# Each entry of digits is a 2D numpy array (a matrix) giving the pixel values of one image
digits = datasets.load_digits()  

# Use imshow() to show the entries of a matrix as an image:
# plt.imshow(digits.images[0], cmap=plt.cm.gray_r)  # Fig 16.1
# for i in range(0,8):
#     for j in range(0,8):
#         plt.gca().text(i-0.15,j,int(digits.images[0][i][j]))  # Fig 16.2

# To turn this 8x8 matrix into a single 64-entry vector, we can use np.matrix.flatten():
vector = np.matrix.flatten(digits.images[0])

# Scale our data so the values are between 0 and 1:
scaled_vector = np.matrix.flatten(digits.images[0]) / 15


# BUILDING A RANDOM DIGIT CLASSIFIER:

# Measure the performance of the digit classifier
def test_digit_classify(classifier,start=0,test_count=1000):
    correct = 0
    end = start + test_count
    for img, target in zip(digits.images[start:end], digits.target[start:end]):
        v = np.matrix.flatten(img) / 15
        output = classifier(v)
        answer = list(output).index(max(output))
        if answer == target:
            correct += 1
    return (correct/test_count)

# Take the average of all the images of 9's in the data set and plot the resulting image:
def average_img(i):
    imgs = [img for img,target in zip(digits.images[1000:], digits.target[1000:]) if target==i]
    return sum(imgs) / len(imgs)

# plt.imshow(average_img(9), cmap=plt.cm.gray_r)  # Fig 16.3

# Classifier that finds the average image of each kind of digit and comparing a target image with all of
# the averages, and returns a vector of the pot products of the target image with each average digit image:
avg_digits = [np.matrix.flatten(average_img(i)) for i in range(10)]
def compare_to_avg(v):
    return [np.dot(v,avg_digits[i]) for i in range(10)]
# test_digit_classify(compare_to_avg)  # >> 0.853, i.e., 85.3% accurate

# DESIGNING A NEURAL NETWORK

# MLP class that stores weights and biases, and provides an evaluate method that takes a 64-dimensional
# input vector and returns the output 10-dimensional vector
class MLP():
    def __init__(self,layer_sizes):
        self.layer_sizes = layer_sizes
        self.weights = [np.random.rand(n,m) for m,n in zip(layer_sizes[:-1], layer_sizes[1:])]
        self.biases = [np.random.rand(n) for n in layer_sizes[1:]]
    
    def feedforward(self,v):
        activations = []
        a = v
        activations.append(a)
        for w,b in zip(self.weights, self.biases):
            z = w @ a + b
            a = [sigmoid(x) for x in z]
            activations.append(a)
        return activations
    
    def evaluate(self,v):
        return np.array(self.feedforward(v)[-1])

# Initialise our neural network as an object instance of the class MLP():
nn = MLP([64,16,10])

# Testing the classification performance of an MLP
# v = np.matrix.flatten(digits.images[0]) / 15
# nn.evaluate(v)  # >> [0.99985097 0.99992824 0.99989226 0.99976628 0.99995598 0.9999725 0.99980977 0.99868787 0.99928011 0.99981143]

# Put all our data in an array:
x = np.array([np.matrix.flatten(img) for img in digits.images[:1000]]) / 15.0
y = digits.target[:1000]

mlp = MLPClassifier(hidden_layer_sizes=(16,),activation='logistic',max_iter=100,verbose=10,random_state=1,learning_rate_init=1)
mlp.fit(x,y)
mlp.predict(x)[0]

# We can write a function that uses this MLP to do one prediction, which is ~96% accurate:
def sklearn_trained_classify(v):
    return mlp.predict([v])[0]

