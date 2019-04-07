"""
Generate serialized form of a ML trained model

__author__ = Marc Durocher

"""
import dill
import sys
import random
from sklearn import linear_model

import m2cgen as m2c


def serialize(model, filename):
    """
    Serializes the model passed in parameter
    :param filename: file name to produce
    :param model: model to serialize
    :return: void
    """

    with open(filename, "wb") as file:
        dill.dump(model, file)


def train_and_return_model():
    """

    :return: model
    """

    def f(x0):
        """
        Linear function to generate points as data input to train the model
        :param x0:
        :return:
        """
        res = x0 * 250 + 3
        return res

    values = []

    # now using f we are going to create 300 values.
    for i in range(0, 300):
        x = random.uniform(1, 1000)
        y = f(x)
        values.append((x, y))

    rg = linear_model.LinearRegression()
    # split the values into two series instead a list of tuples
    x, y = zip(*values)

    # split the values in train and data.
    train_data_x = list(map(lambda x0: [x0], list(x)))
    train_data_y = list(y)

    # feed the linear regression with the train data to obtain a model.
    rg.fit(train_data_x, train_data_y)

    return rg


def main():
    filename = './ml_model.bin'
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    model = train_and_return_model()
    serialize(model, filename)


if __name__ == "__main__":
    main()
