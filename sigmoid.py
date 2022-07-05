import numpy as np
from matplotlib import pyplot as plt

MAX_VALUE = 5


def sig(x):
    s = 1 / (1 + np.e**-x)
    return s


def main():

    x = np.arange(0, MAX_VALUE, 0.1)
    plt.title("Sigmoid")
    plt.xlabel("X")
    plt.ylabel("Y Sig value of X")
    y = x
    plt.plot(x, sig(y))
    plt.grid(True)
    plt.show()


if __name__ == "_main__":
    main()
