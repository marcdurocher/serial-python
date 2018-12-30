"""
Generate bin function from any function

__author__ = Marc Durocher

"""
import dill
import sys
import random
from sklearn import linear_model


def serialize(fn, filename):
    """
    Serialise la fonction <fn> passee en parametre
    :param filename: nom du fichier a produire
    :param fn: fonction a serialiser
    :return: neant
    """

    with open(filename, "wb") as file:
        dill.dump(fn, file)


def train_and_return_predictive_function():
    """

    :return:
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
    # check that the coeffients are the expected ones.
    m = rg.coef_[0]
    b = rg.intercept_
    fp = rg.predict

    print(' y = {0} * x + {1}'.format(m, b))
    print(' type:rg', type(rg))
    print(' type:fp', type(fp))

    def nfp(x0):
        '''
        The prediction function returns a numpy.ndarray
        We have to cast into list an then take the first item
        :param x0:
        :return:
        '''
        r = rg.predict([[x0]]).tolist()[0]
        # print('type(r) %s' % (type(r),))

        return r
    return nfp


def main():
    filename = './function.bin'
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    fn = train_and_return_predictive_function()
    serialize(fn, filename)


if __name__ == "__main__":
    main()
