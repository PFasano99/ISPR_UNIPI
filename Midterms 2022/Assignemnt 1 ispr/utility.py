import os
import random
import shutil
import numpy as np

from numpy import source
import scipy.io.wavfile as wavfile
from scipy import signal
from random import shuffle

def devideFiles(source, destination):     
    """

    This simple method devides the files in a folder moving randomly 1 on 5 files in an other folder.
    Can be used to create sample of data that must not be used in training or validation ( Refares to Machine Learing purpose)   
    """   
    src = source
    dest = destination
    files = os.listdir(source)
    no_of_files = len(files) // 5

    for file_name in random.sample(files, no_of_files):
        shutil.move(os.path.join(source, file_name), dest)

# devideFiles(source='./violinWav',destination='./testSet')
# devideFiles(source='./benjoWav',destination='./testSet')
# devideFiles(source='./trumpetWav',destination='./testSet')
# devideFiles(source='./celloWav',destination='./testSet')
def loadAllWavInLists(path = './', trim = True, trimTime = 2, label = True, trimLabel = '_'):
    spectrograms = []
    labels = []
    arrayNames = os.listdir(path)
    maxShape = (0,0)
    # read all files        
    for fi in arrayNames:
        Fs, aud = wavfile.read(path+fi)
        if trim:
            first = aud[:int(Fs*trimTime)] 
        #plot the spectrum for the file fi
        frequencies, times, spectrogram = signal.spectrogram(first, Fs)
        if(maxShape<spectrogram.shape):
            maxShape = spectrogram.shape
        np.pad(spectrogram, (129, 393), 'constant', constant_values=(0,0))
        print(spectrogram.shape)
        #spectrogram  = np.stack(spectrogram, axis=0)  
        print(spectrogram.shape)
        spectrograms.append(spectrogram)
        print(len(spectrograms))
        #add a label to the spectrogram
        if label:
            fi = fi.split("_")[0]
        labels.append(fi)     
    return labels, spectrograms

def printSpecValues(lab, spec):
    i = 0
    for l in lab:
        print(l, "\n",spec[i])
        i+=1

#lab, spec = loadAllWav(path = './benjoWav/')
#printSpecValues(lab, spec)

#this function is used to shuffle two related lists 
def shuffleLists(list1, list2, seed = 42):
    assert(len(list1)==len(list2)), "Lists are not of the same size"
    random.seed(seed)
    list1_shuf = []
    list2_shuf = []
    index_shuf = list(range(len(list1)))
    shuffle(index_shuf)
    for i in index_shuf:
        list1_shuf.append(list1[i])
        list2_shuf.append(list2[i])
    return list1_shuf, list2_shuf

#print(shuffleLists([1,2,3,4,5,6,7,8,9],[5,6,7,8,9,1,2,4,5]))

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


def loadAllWavInNpArray(path = './', trim = True, trimTime = 2, label = True, trimLabel = '_'):
    
    spectrograms = np.zeros(shape=(1,120))
    arrayNames = os.listdir(path)
    
    #shape cal
    Fs, aud = wavfile.read(path+arrayNames[0])
    if trim:
        first = aud[:int(Fs*trimTime)] 
        #plot the spectrum for the file fi
    frequencies, times, spectrogram = signal.spectrogram(first, Fs)
    print (len(spectrogram))
    
    
    # read all files    
    index = 0    
    for fi in arrayNames:
        Fs, aud = wavfile.read(path+fi)
        if trim:
            first = aud[:int(Fs*trimTime)] 
        #plot the spectrum for the file fi
        frequencies, times, spectrogram = signal.spectrogram(first, Fs)
        len(spectrogram)
        spectrograms[index] = spectrogram
        #add a label to the spectrogram
        if label:
            fi = fi.split("_")[0]
        labels[index] = fi     
        index+=1
    return labels, spectrograms


