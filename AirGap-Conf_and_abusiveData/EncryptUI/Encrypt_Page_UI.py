# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Encrypt_Page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


import speech_recognition as sr

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

from PIL import Image
import stepic

import os
#from FileSend import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1360, 760)
        self.mainButton=""
        df = pd.read_excel('KnnDataset.xlsx', sheet_name='Sheet1')

        #print("Column headings:")
        #print(df.columns)
        self.words=list(df['Words'])
        self.mode=list(df['Decrypt Mode'])
        self.level=list(df['Confidentiality'])
        le = preprocessing.LabelEncoder()
        # Converting string labels into numbers.
        self.words_encoded=le.fit_transform(self.words)
        self.mode_encoded=le.fit_transform(self.mode)
        self.label=le.fit_transform(self.level)
        self.check=list(self.label)
        print("Words_E:",self.words_encoded)
        print("Mode_E:",self.mode_encoded)
        print("Level_E:",self.label)
        
        self.features=list(zip(self.words_encoded,self.mode_encoded))
        
        f = open('mykey.pem','r')
        self.key = RSA.importKey(f.read())
        self.pubKey = self.key.publickey()

        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone(device_index=1)
        
        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1360, 760))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Gui_Images/BG.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 110, 1360, 61))
        self.label_3.setStyleSheet("background-color: rgba(106, 255, 111,170);\n"
"font: 18pt \"Papyrus\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(350, 270, 591, 421))
        self.frame.setStyleSheet("background-color: rgba(85, 255, 127,170);\n"
"border-radius:30px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.hide()
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(115, 60, 375, 41))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 10pt \"MV Boli\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 360, 151, 41))
        self.pushButton.setStyleSheet("color: rgb(255, 123, 163);\n"
"font: 10pt \"MV Boli\";\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.funtions)
        self.lineEdit = QtWidgets.QTextEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(110, 100, 381, 241))
        self.lineEdit.setStyleSheet("background-color: rgba(209, 209, 209,200);\n"
"font: 15pt \"MV Boli\";\n"
"border-radius:20px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 10, 151, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(22, 173, 20);\n"
"font: 10pt \"MV Boli\";\n"
"\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.selectfile)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(490, 200, 151, 41))
        self.comboBox.setStyleSheet("font: 10pt \"MV Boli\";\n"
"background-color: rgb(173, 173, 173);\n"
"color: rgb(67, 111, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Write Text","Text File","Audio","Image","Stagnography"])
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 200, 151, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color: rgb(74, 107, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";\n"
"\n"
"border-radius:20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.selectMode)
        #self.pushButton_2.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def ocr_core(self,filename):
        """
        This function will handle the core OCR processing of images.
        """
        text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
        return text
    
    def recognize_speech_from_mic(self,recognizer, microphone):
        self.label_4.setText("Say Something..")
        """Transcribe speech from recorded from `microphone`.
        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                   successful
        "error":   `None` if no error occured, otherwise a string containing
                   an error message if the API could not be reached or
                   speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                   otherwise a string containing the transcribed text
        """
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")
    
        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
    
        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
            print("Say something:")
            
            audio = recognizer.listen(source)
    
        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #   update the response object accordingly
        try:
            #pass
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable/unresponsive"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
        self.label_4.setText("Check Confidentiality")
        return response
    
    def selectMode(self):
        self.mode=self.comboBox.currentText()
        self.pushButton_2.hide()
        print(self.mode)
        self.selected=0
        self.lineEdit.clear()
        if self.mode=="Write Text":
            self.mainButton="Analyse"
            self.labelText="Type Text You Want to Send"
        if self.mode=="Text File":
            self.pushButton_2.show()
            self.mainButton="Fetch Text"
            self.labelText="Select Text Document"
        if self.mode=="Audio":
            self.labelText="Click on Speak"
            self.mainButton="Speak Now"
        if self.mode=="Image":
            self.pushButton_2.show()
            self.labelText="Select the Image"
            self.mainButton="Convert"
        if self.mode=="Stagnography":
            self.pushButton_2.show()
            self.labelText="Select the Image"
            self.mainButton="Hide Text"
        self.pushButton.setText(self.mainButton)    
        self.label_4.setText(self.labelText)
        self.frame.show()
    
    def calc_confidance(self,text):
        model = KNeighborsClassifier(n_neighbors=3)
        # Train the model using the training sets
        model.fit(self.features,self.label)
        sampleSent=text
        sampleWords=sampleSent.split()
        wordlen=0
        total_conf=0
        abusive=False
        for word in sampleWords:
            if len(word)<3:
                continue
            if word in self.words:
                wordlen+=1
                i=self.words.index(word)
                print(i)
                predicted = model.predict([[self.words_encoded[i],1]])
                index=self.check.index(predicted[0])
                print(self.level[index])
                print("Confidential Word:"+word+"---"+str(self.level[index]))
                if self.level[index]=='A':
                	abusive=True
                	

                if(self.level[index]=='C'):
                    total_conf+=1
            else:
                wordlen+=1
                print("Normal Word:"+word)
        print(total_conf)
        print(wordlen)
        self.perc=(total_conf/wordlen)*100
        return self.perc,abusive
    
    def rsa_encrypt(self,text):
        msg = bytes(text, 'utf-8')
        #msg = b'basic explanation class'
        encryptor = PKCS1_OAEP.new(self.pubKey)
        self.encrypted = encryptor.encrypt(msg)
        print(self.encrypted)
        encrypted_str=binascii.hexlify(self.encrypted)
        self.lineEdit.clear()
        self.lineEdit.setText(str(encrypted_str))
    
    def sendmail(self,sub,message,filenames):
        fromaddr = 'securedatatransfer8@gmail.com'#"raspberryp087@gmail.com"     #https://www.google.com/settings/security/lesssecureapps
        toaddr = "arathinavaneeth1602@gmail.com"
        self.label_4.setText("Sending Mail")       
        # instance of MIMEMultipart 
        msg = MIMEMultipart() 
        # storing the senders email address   
        msg['From'] = "Confidential Data"
          
        # storing the receivers email address  
        msg['To'] = toaddr 
          
        # storing the subject  
        msg['Subject'] = sub
        
        # string to store the body of the mail 
        body = message
          
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 
          
        # open the file to be sent  
        
        for filename in filenames:
            attachment = open(filename, "rb") 
              
            # instance of MIMEBase and named as p 
            p = MIMEBase('application', 'octet-stream') 
              
            # To change the payload into encoded form 
            p.set_payload((attachment).read()) 
              
            # encode into base64 
            encoders.encode_base64(p) 
                 
            # attach the instance 'p' to instance 'msg'
        
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p) 
          
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
          
        # start TLS for security 
        s.starttls() 
          
        # Authentication 
        s.login(fromaddr,"qwerty@1602")#"Raspberry@123" 
          
        # Converts the Multipart msg into a string 
        text = msg.as_string() 
          
        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 
          
        # terminating the session 
        s.quit()
        self.label_4.setText("Mail Sent")
        self.labelText="Mail Sent"
        self.mainButton="Clear"

       
    def funtions(self):
        if self.mode=="Text File" and self.mainButton=="Fetch Text":
            file=(open(self.textfile[0],"r"))
            self.content=file.read()
            #print(self.content)
            self.lineEdit.setText(self.content)
            self.labelText="Check Confidentiality"
            self.mainButton="Analyse"
        elif self.mainButton=="Analyse":
            self.contnt=self.lineEdit.toPlainText()
            self.conf,self.absv=self.calc_confidance(self.contnt)
            print(self.conf)
            self.labelText="Confidentiality:"+str(round(self.conf,2))+" %"
            if self.absv==True:
            	QMessageBox.information(None,"Abusive Word Detected","Avoid Using Abusive Content")

            elif(self.conf>30):
                self.labelText=self.labelText+", Encrypt Data"
                self.mainButton="Encrypt-Send"
            else:
                self.labelText=self.labelText+",Can Send File"
                self.mainButton="Send File"
                file3 = open("FileToSend/Send.txt","w") 
                # \n is placed to indicate EOL (End of Line) 
                file3.write(self.contnt) 
                file3.close() #to change file access modes
            
        elif self.mainButton=="Encrypt-Send":
            self.rsa_encrypt(self.contnt)
            file1 = open("FileToSend/Send.txt","wb") 
            # \n is placed to indicate EOL (End of Line) 
            file1.write(self.encrypted) 
            file1.close() #to change file access modes
            self.label_4.setText("File Sent")
            self.labelText="File Sent"
            self.mainButton="Clear"
            #self.sendmail("Encrypted Info","Seems like a confidential Data,In order to Decrpyt Use the Decrytion App",["FileToSend/Encrypted"+str(round(self.conf,2))+".txt"])
        
        elif self.mainButton=="Send File":
            self.label_4.setText("File Sent")
            self.labelText="File Sent"
            self.mainButton="Clear"
            filename=os.path.join(os.getcwd(),"FileSend.py")
            print(os.getcwd(),filename)
            os.system("python "+filename)
            
            
            #self.sendmail("Normal Info"," Readable Format",['FileToSend/NormalData.txt'])
        
        elif self.mainButton=="Speak Now":
            self.labelText="Say Something.."
            self.label_4.setText(self.labelText)
            response = self.recognize_speech_from_mic(self.recognizer, self.mic)
            if response['success']==False:
                self.labelText="Something Wrong, Try Again"
            else:
                self.lineEdit.setText(response['transcription'])
                self.mainButton='Analyse'
                self.labelText="Check Confidentiality.."
        elif self.mainButton=="Convert":
            self.lineEdit.setText(self.ocr_core(self.imgfile[0]))
            self.mainButton='Analyse'
            self.labelText="Check Confidentiality.."
        
        elif self.mainButton=="Hide Text":
            im = Image.open(self.stagfile[0])
            data=self.lineEdit.toPlainText()
            self.s_filename="StagImage.png"
            if (len(data) == 0):
                raise ValueError('Data is empty')
            bin_data = bytes(data, 'utf8')
            im1 = stepic.encode(im, bin_data)
            im1.save(self.s_filename, 'PNG')
            self.labelText="Data Encoded"
            self.lineEdit.clear()
            self.mainButton="Send Image"

        elif self.mainButton=="Send Image":
            self.sendmail("Stagnographed Image"," Hidden Text , Use Application to decrypt",[self.s_filename])
        
        elif self.mainButton=="Clear":
            self.selected=0
            self.lineEdit.clear()
            self.labelText=''
            self.mainButton=''
            self.frame.hide()
        
        self.label_4.setText(self.labelText)
        self.pushButton.setText(self.mainButton)
        
    def selectfile(self):
        print(self.mode)
        if self.mode=="Text File" and self.selected==0:
            self.textfile = QFileDialog.getOpenFileName(None, 'Open file', '.','Text Files (*.txt)')
            print(self.textfile[0])
            self.labelText="Selected Text Document"
            self.label_4.setText(self.labelText)
        
        if self.mode=="Image" and self.selected==0:
            self.imgfile = QFileDialog.getOpenFileName(None, 'Open file', '.','Images (*.jpg *.png)')
            print(self.imgfile[0])
            self.labelText="Image Selected"
            self.label_4.setText(self.labelText)
            
        if self.mode=="Stagnography" and self.selected==0:
            self.stagfile = QFileDialog.getOpenFileName(None, 'Open file', '.','Images (*.jpg *.png)')
            print(self.stagfile[0])
            self.labelText="Image Selected , Write Content.."
            self.label_4.setText(self.labelText)
        
            
        
        
            
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Encrypt Data"))
        self.label_3.setText(_translate("Form", " Confidential Data Encryption and Decryption Based on KNN algorithm"))
        self.label_4.setText(_translate("Form", "Fetched data"))
        self.pushButton.setText(_translate("Form", "Analyse"))
        self.pushButton_2.setText(_translate("Form", "Select File"))
        self.pushButton_3.setText(_translate("Form", "Select Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

