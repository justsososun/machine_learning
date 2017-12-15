# -*-coding:utf-8-*-
__author__ = 'sun'
# 20171203
import numpy as np
import operator


def creatDataSet():
    group = np.array([[1, 1.1], [1, 1], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def printf(func):
    """
    :param func:
    :return:
    """

    g, l = func()
    print g
    print l


if __name__ == '__main__':
    printf(creatDataSet)

