import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import ast


class LogisticRegression:

    def __init__(self):
        self.theta_1 = None  # Bias
        self.theta_2 = None  # Weights
        self.input_shape = None # Created x vector shape

    def fit(self, x, y, iteration_num=8000, learning_rate=1E-2):
        self.input_shape = x.shape[1]
        # Get samples
        training_num = x.shape[0]
        # Initialize weights and bias
        self.theta_1 = 1
        self.theta_2 = np.ones(x.shape[1])
        # Train respect to iteration num
        x_transpose = x.transpose()
        for i in range(iteration_num):
            # In order to make prediction about logistic reg. linear model is calculated
            y_linear = self.theta_1 + np.dot(x, self.theta_2)
            # Sigmoid function output is obtained for gradient descent in Logistic Regression
            y_sigmoid = self.sigmoid(y_linear)
            # Get new weight and bias
            new_theta_1 = self.theta_1 - learning_rate / training_num * np.sum(y_sigmoid - y)
            new_theta_2 = self.theta_2 - learning_rate / training_num * np.dot(x_transpose, (y_sigmoid - y))
            # Assign the new weight and bias
            self.theta_1 = new_theta_1
            self.theta_2 = new_theta_2
            if (i % 50 == 0 and i != 0) or i == iteration_num - 1:
                print("Iteration num %d" % i)

    # Prediction
    def prediction(self, x):
        try:
            if x.shape[1] != self.input_shape:
                pass

        except:
            x = self.preprocess(x)

        # Linear model
        y_linear = self.theta_1 + np.dot(x, self.theta_2)
        # Logistic Regression outputs
        y_sigmoid = list(map(self.sigmoid, y_linear))
        # If output is above 0.5 it is assumed as it belongs to 1 otherwise 0
        y_pred = list(map(lambda x: 1 if x > 0.5 else 0, y_sigmoid))
        return y_pred

    # Sigmoid function
    def sigmoid(self, y_linear):
        epsilon = 1E-6
        return 1 / (1 + np.exp(- (y_linear + epsilon)))

    # Accuracy calculation
    def accuracy(self, output_predicted, output_true):
        # Get comparison of predicted and true output
        comparison_list = [output_predicted[k] == output_true[k] for k in range(len(output_predicted))]
        # Get Percentage of correct predictions
        acc = comparison_list.count(True) / len(comparison_list)
        return acc

    def preprocess(self, _x):
        porter_stemmer = PorterStemmer()
        stop_word_list = stopwords.words("english")
        with open("data/word_dictionary", "r") as f:
            words = f.read()
            word_dict = ast.literal_eval(words)
        x = np.empty((_x.shape[0], len(word_dict)))
        for i,row in enumerate(_x):
            mail = re.sub("[^a-zA-Z]", " ", row).lower().split()
            # Get roots of all words and ignore if the word is stop word
            mail = [porter_stemmer.stem(word) for word in mail if word not in stop_word_list]
            for word in mail:
                if word in word_dict:
                    x[i, word_dict[word]] += 1

        return x
