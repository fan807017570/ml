import pandas as pd
import numpy as np
from sklearn import datasets
from math import log


class CartTree():
    def __init__(self, dataSet, target):
        self.dataSet = dataSet
        self.target = target

    def CalGain(self):
        print("hello ")
        0

    def CalcEntropy(self):
        label_count = {}
        label_percent = {}
        total = len(self.target)
        for i in self.target:
            if i not in label_count.keys():
                label_count[i] = 1
            else:
                if i == 1:
                    label_count[i] += 1
                else:
                    label_count[i] += 1
        entropy = 0
        for key in label_count.keys():
            label_percent[key] = label_count[key] / total
            prob = label_percent[key]
            entropy -= prob * log(prob, 2)
        return entropy

    def createTree(self):
        print("create tree")

    def testHoursing(self):
        print("test hoursing")


def loadData():
    iris_data = datasets.load_iris()
    data = iris_data.data
    target = iris_data.target
    return data, target


data, target = loadData()

tree = CartTree(data, target)
print(tree.CalcEntropy())
# print(data)
colomn = data[:, 0]
# print(colomn)
colomn_list = []
for i in range(len(colomn)):
    tuple_label = [colomn[i], target[i]]
    colomn_list.append(tuple_label)
# print(sorted(colomn_list)[1:])
for j in range(len(colomn_list)):
    if j != 0:
        colomn_left = sorted(colomn_list)[:j]
        print("colomn_left:{}".format(colomn_left))
        colomn_right = sorted(colomn_list)[j:]
        print("colomn_right:{}".format(colomn_right))
# colomn_targets = sorted(colomn_list)[:]
# print(colomn_targets)
# colomn_array = np.array(colomn_targets)
# print(colomn_array[4:, 1])
# print(colomn_targets)
# print(colomn_targets[1:10][1:2])
# print(colomn_targets[:, 1])
# print(colomn_targets)
# print(sorted(data[:,3]))
# t = CartTree()
# t.testHoursing()
# t.loadData()
