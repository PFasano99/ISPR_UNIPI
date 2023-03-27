# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile
from scipy import signal
import os


paths = ['./wavToPlot/']
i = 0
for path in paths:
    arrayNames = os.listdir(path)
    for fi in arrayNames:
        Fs, aud = wavfile.read(path+fi)

        # plt.subplot(211)

        plt.title('Spectrogram of a wav file with ' + fi.split(".")[0] +' note') 
        plt.xlabel('Time')
        plt.ylabel('Frequency')

        # # select left channel only
        # #aud = aud[:,0]
        # # trim the first 2 second
        first = aud[:int(Fs*2)] 

        frequencies, times, spectrogram = signal.spectrogram(first, Fs)
        plt.pcolormesh(times, frequencies, 10*np.log10(spectrogram), shading='gouraud')
        #plt.imshow(spectrogram)
        # #plt.plot(spectrogram)

        # plt.subplot(212)

        
        #plt.xlabel('Time')
        #plt.ylabel('Frequency')
        # powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
        plt.savefig(fi.split(".")[0]+'.png')
        i+=1
        print(i,path+fi)
        # print("here \n")
        # print(signal.spectrogram(first, Fs))
        # print("here 2\n")
        # print(plt.specgram(first, Fs=Fs))
#plt.show()