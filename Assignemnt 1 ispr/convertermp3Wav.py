from os import path
from pydub import AudioSegment
import os


# import required modules
import subprocess

arrayNames = os.listdir("./violin")
# for all files in directory        
for fi in arrayNames:       
    print(fi)                                                           
    src = "violin/" + fi 
    newName = fi.split(".")[0]
    dst = "./violinWav/" + newName + ".wav"
   # print("\n")
   # print(src)
   # print("as: " + newName + ".wav")
   # print("\n")


# convert mp3 file to wav file
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")