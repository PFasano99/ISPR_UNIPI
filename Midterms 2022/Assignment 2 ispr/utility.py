import os 
import random
import cv2 
import numpy as np


from random import shuffle

def loadFiles(path = "./"):
    files = os.listdir(path)
    labels = []
    data = []

    for file in files:
        pic = cv2.imread(path+file)
        if file.find("_GT") != -1:
            #print("label ", file)
            labels.append(pic)
        else:
            data.append(pic)
    
    return data, labels

#this function is used to shuffle two related lists 
def shuffleLists(list1, list2, seed = 42):
    assert(len(list1)==len(list2)), ("Lists are not of the same size",  len(list1), len(list2)) 
    random.seed(seed)
    list1_shuf = []
    list2_shuf = []
    index_shuf = list(range(len(list1)))
    shuffle(index_shuf)
    for i in index_shuf:
        list1_shuf.append(list1[i])
        list2_shuf.append(list2[i])
    return list1_shuf, list2_shuf

def splitDataset(allLabels, alldata, percentageOfVal = 30):
    testSet= [] 
    testLabels = []
    validationSet= []
    validationLabels = []

    valLen = (len(alldata)*percentageOfVal)/100
    per = 0
    while per <= valLen:
        validationLabels.append(allLabels[per])
        validationSet.append(alldata[per])
        per+=1
    
    while per < len(alldata):
        testLabels.append(allLabels[per])
        testSet.append(alldata[per])
        per+=1 
    
    return testLabels, testSet, validationLabels, validationSet
