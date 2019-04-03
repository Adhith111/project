import sys
import pyaudio
import math
import urllib.request
import datetime
from pydub import AudioSegment
import urllib.error
import re
import sys
import time
import wave
import urllib
import urllib.request
import os
import pipes
import subprocess
from tqdm import tqdm
from multiprocessing import pool
import shlex
import speech_recognition as sr
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
import pymysql
TOTAL_DURATION=0
LANG_CODE='eng-US'
GOOGLE_SPEECH_URL='https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter=2&lang=%s&maxresults=6' % (LANG_CODE)
db=pymysql.connect("localhost","root","123","file")
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print("Database version: %s :",data)
start_time = datetime.datetime(100,1,1,0,0,0) #the video is now at 5 minute mark
#00:07:20

max_time = datetime.datetime(100,1,1,0,8,0) #max duration of the video is 8 minutes

block_num = 13
class FilePicker(QtWidgets.QWidget,):
    """
    An example file picker application
    """

    
    def __init__(self):
        # create GUI
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('select video to generate subtitle')
        # Set the window dimensions
        self.resize(300,75)
        # vertical layout for widgets
        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)

        # Create a label which displays the path to our chosen file
        self.lbl = QtWidgets.QLabel('No file selected')
        self.vbox.addWidget(self.lbl)
        btn = QtWidgets.QPushButton('select video', self)
        
        self.vbox.addWidget(btn)
        
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 110, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STIXVariants")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 270, 171, 51))
        font = QtGui.QFont()
        font.setFamily("STIXVariants")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 190, 171, 51))
        font = QtGui.QFont()
        font.setFamily("STIXVariants")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(510, 120, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(510, 200, 118, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(510, 280, 118, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label.setText("Audio extraction")
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.progressBar)
        self.label_2.setText("Speech recognition")
        self.vbox.addWidget(self.label_2)
        self.vbox.addWidget(self.progressBar_2)
        self.label_3.setText("Subtitle generation")
        self.vbox.addWidget(self.label_3)
        self.pushButton.setText("Generate subtitles")
        self.vbox.addWidget(self.progressBar_3)
        self.vbox.addWidget(self.pushButton)
        
        
        # Create a push button labelled 'choose' and add it to our layout
        
        
        # Connect the clicked signal to the get_fname handler
        btn.clicked.connect(self.get_fname)
        self.pushButton.clicked.connect(self.video_to_audio)

    def video_to_audio(self):

        name=self.lbl.text()
        print(name)
        print("%s"%name)
        print("ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn audio.wav"%name)
        command = ("ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn audio.wav"%name)

        subprocess.call(command, shell=True)
        

        #self.speechrecognition()
        self.timestamping()
    
    def stt_google_wav(self,audio_fname):
    
        print ("Sending ", audio_fname)
        #Convert to flac first
        filename = audio_fname
        """del_flac = False
        if 'flac' not in filename:
            del_flac = True
            print ("Converting to flac")
            print (FLAC_CONV + filename)
            os.system(FLAC_CONV + ' ' + filename)
            filename = filename.split('.')[0] + '.flac'"""

        f = open(filename, 'rb')
        flac_cont = f.read()
        f.close()
        print("speech recognition starting.....")
        r=sr.Recognizer()
        audio='audio.wav'
        with sr.AudioFile(audio) as source:
            print("Started")
            audio=r.record(source)
            print("Done")
        try:
            res=r.recognize_google(audio,language='eng-US')
            print("hai")
            print (res)
            print("hai")
        except Exception as e:
            print(e)
        return res
    def convert_to_mins(self,sec):
    
        secs = sec%60
        mins = sec/60
        hours = mins/60
        mins = mins%60

        if hours<10:
            hours = str(0)+str(hours)
        if mins<10:
            mins = str(0)+str(mins)
        if secs<10:
            secs = str(0)+str(secs)

        return str(hours)+":"+str(mins)+":"+str(secs)
    def coalesce_silences(self,silence):
        pos_to_delete = []
        for i in range(len(silence)-1):
            if(silence[i]==silence[i+1]):
                pos_to_delete.append(i)
    
    #reverse list
        pos_to_delete = pos_to_delete[::-1]
    
        for i in pos_to_delete:
            silence.pop(i)
        return silence
    def get_speech_timestamp_in_seconds(self,silence):
        speech_mins = []
        speech_sec = []
        temp1 = ""
        temp2 = ""
        for i in range(len(silence)-1):
            temp1 = str(self.convert_to_mins(silence[i])) + " --> " + str(self.convert_to_mins(silence[i+1]))
            temp2 = str(silence[i]) + " --> " + str(silence[i+1])
            speech_mins.append(temp1)
            speech_sec.append(temp2)
        return speech_mins,speech_sec
    def write_srt_file(self,speech_mins,speech_sec):
        f = open('sub.srt', 'a')
        l=0
        for i in range(len(speech_mins)):
            string = self.split_audio_file(speech_sec[i])
            print (string)
            print(str(i+1))
            if not string:
                write_chunk = "{} \n  {} \n\n".format(int(i+1),str(speech_mins[i]))
            elif string:
                g=str(speech_mins[i])
                print(g)
                d=l
                l+=i+5
            
                write_chunk = "{} \n  {} \n  {} \n\n".format(int(i+1),g,str(string[d:l]))
            f.write(write_chunk)
        f.close()
    def timestamping(self):
        print ("Calculating time stamps based on silence intervals\n")
        w = wave.open('audio.wav','r')
        frame = True
        start = 0
        THRESHOLD = 90
        MAJORITY = 0.6
        CHUNK = int(math.floor(w.getframerate()/3))
        num_of_chunks = 0
        silence = []
        fi = 1
        count = 1
        while frame:
            frame = w.readframes(CHUNK)
            flag = True
            count = 0
            for i in range(len(frame)):
                if (frame[i])<THRESHOLD:
                    count+=1
            num_of_chunks+=1
        #print count, w.getframerate()
            if (float(count)/w.getframerate()) > MAJORITY:
                silence.append((w.tell()-CHUNK)/w.getframerate())
        TOTAL_DURATION = float(num_of_chunks)/3
        silence.append(int(TOTAL_DURATION))
        silence = self.coalesce_silences(silence)
        speech_mins,speech_sec = self.get_speech_timestamp_in_seconds(silence)
        print (speech_mins, speech_sec)

        self.write_srt_file(speech_mins,speech_sec)
    def split_audio_file(self,time):
        time = time.split()
        if float(time[0])<1:
            startTime = str(time[0])
            duration = str(float(time[2]) - float(time[0]) + 1)
        elif(float(time[2])>=float(TOTAL_DURATION-1)):
            startTime = str(float(time[0])-1)
            duration = str(float(time[2]) - float(time[0]))
        else:
            startTime = str(float(time[0])-1)
            duration = str(float(time[2]) - float(time[0]) + 1)
        command = "ffmpeg -ss " + startTime + " -t " + duration + " -i audio.wav -vn -ac 1 -ar 16000 -acodec flac convert.flac"
        os.system(command)
        string =  self.stt_google_wav('convert.flac')
        command = "rm convert.flac"
        os.system(command)
        return string



       

    
    def get_fname(self):
        """
        Handler called when 'choose file' is clicked
        """
        # When you call getOpenFileName, a file picker dialog is created
        # and if the user selects a file, it's path is returned, and if not
        # (ie, the user cancels the operation) None is returned

        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file')[0]
        
        if fname:
            self.lbl.setText(fname)
            query="""INSERT INTO file(path) VALUES (%s)"""
            cursor.execute(query,fname)
            db.commit()
            db.close()
            print (fname)
            

        else:
            self.lbl.setText('No file selected')
        print (fname)
        
        

# If the program is run directly or passed as an argument to the python
# interpreter then create a FilePicker instance and show it
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = FilePicker()
    gui.resize(800,600)
    gui.show()
    app.exec_()

