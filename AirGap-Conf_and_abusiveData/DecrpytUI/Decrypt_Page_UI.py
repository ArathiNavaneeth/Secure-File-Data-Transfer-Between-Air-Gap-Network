# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Decrypt_Page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

from gtts import gTTS
import os

import numpy as np
import cv2
import textwrap

from PIL import Image
import stepic

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1360, 760)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1360, 760))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Gui_Images/BG.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 1360, 61))
        self.label_3.setStyleSheet("background-color: rgba(106, 255, 111,170);\n"
"font: 18pt \"Papyrus\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(340, 200, 591, 421))
        self.frame.setStyleSheet("background-color: rgba(85, 255, 127,170);\n"
"border-radius:30px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(150, 300, 291, 41))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 10pt \"MV Boli\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QTextEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 381, 241))
        self.lineEdit.setStyleSheet("background-color: rgba(209, 209, 209,200);\n"
"font: 15pt \"MV Boli\";\n"
"border-radius:20px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 350, 151, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(22, 173, 20);\n"
"font: 10pt \"MV Boli\";\n"
"\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.execute)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(470, 150, 151, 41))
        self.comboBox.setStyleSheet("font: 10pt \"MV Boli\";\n"
"background-color: rgb(173, 173, 173);\n"
"color: rgb(67, 111, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['RSA Algorithm','Stagnography'])
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 680, 151, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color: rgb(74, 107, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";\n"
"\n"
"border-radius:20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_3.hide()
        
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 680, 151, 41))
        self.comboBox_2.setStyleSheet("font: 10pt \"MV Boli\";\n"
"background-color: rgb(173, 173, 173);\n"
"color: rgb(67, 111, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(['Image','Text','Audio'])
        self.comboBox_2.hide()
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 150, 151, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"background-color: rgb(74, 107, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";\n"
"\n"
"border-radius:20px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.method)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 630, 151, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgba(209, 209, 209,200);\n"
"font: 8pt \"MV Boli\";\n"
"border-radius:20px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.hide()
        self.frame.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def textToImage(self,text,filename):
        img = cv2.imread('BG_White_Image.jpg')
        print(img.shape)
        
        height, width, channel = img.shape
        
        text_img = np.ones((height, width))
        print(text_img.shape)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        #text = "Lorem Ipsum dgdhswjkclyhwegflhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhvhasvcxsbvfajhskvfgsdj"
        wrapped_text = textwrap.wrap(text, width=35)
        x, y = 10, 40
        font_size = 1
        font_thickness = 2
        
        for i, line in enumerate(wrapped_text):
            textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]
        
            gap = textsize[1] + 10
        
            y = int((img.shape[0] + textsize[1]) / 2) + i * gap
            x = int((img.shape[1] - textsize[0]) / 2)
        
            cv2.putText(img, line, (x, y), font,
                        font_size, 
                        (0,0,0), 
                        font_thickness, 
                        lineType = cv2.LINE_AA)
        
        cv2.imshow("Result Image", img)
        cv2.imwrite(filename+".jpg",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    
    def execute(self):
        if self.mainButton=="Choose File":
            self.en_file = QFileDialog.getOpenFileName(None, 'Open file', '.','Text Files (*.txt)')
            print(self.en_file[0])

            self.mainButton="Decrpyt"
            self.labelText="File Selected"
        
        elif self.mainButton=="Choose Image":
            self.Im_en_file = QFileDialog.getOpenFileName(None, 'Open file', '.','Image Files (*.PNG *png)')
            print(self.Im_en_file[0])

            self.mainButton="Decode"
            self.labelText="File Selected , Click to Decode Text"
        
        elif self.mainButton=="Decode":
            Stagimage = Image.open(self.Im_en_file[0])
            text = stepic.decode(Stagimage)
            self.lineEdit.setText(text)
            self.lineEdit_2.show()
            self.comboBox_2.show()
            self.pushButton_3.show()
            
        elif self.mainButton=="Decrpyt":
            self.decrpted_c=self.decrypt_rsa()
            self.lineEdit.setText(self.decrpted_c)
            self.pushButton_3.show()
            self.lineEdit_2.show()
            self.comboBox_2.show()
            self.mainButton="Decrpyted"
            self.labelText="The Content is Decrypted"
        
        self.pushButton_2.setText(self.mainButton)
        self.label_4.setText(self.labelText)
    def save(self):
        print("pressed")
        formt=self.comboBox_2.currentText()
        if formt=="Audio":
            mytext = self.lineEdit.toPlainText()
            language = 'en'
            myobj = gTTS(text = mytext, lang=language, slow=False)
            filename=self.lineEdit_2.text()
            myobj.save("DecryptedFiles/"+filename+".mp3")
            os.system("start DecryptedFiles/"+filename+".mp3")
        
        if formt=="Image":
            mytext = self.lineEdit.toPlainText()
            filename=self.lineEdit_2.text()
            self.textToImage(mytext,"DecryptedFiles/"+filename)
            
        if formt=="Text":
            mytext = self.lineEdit.toPlainText()
            filename=self.lineEdit_2.text()
            f=open("DecryptedFiles/"+filename+".txt",'w')
            f.write(mytext)
            f.close()
        
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_2.hide()
        self.comboBox_2.hide()
        self.pushButton_3.hide()
        self.frame.hide()
    def method(self):
        self.method=self.comboBox.currentText()
        self.frame.show()
        if self.method=='RSA Algorithm':
            self.labelText="Choose Encrypted Text File"
            self.mainButton="Choose File"
        
        if self.method=='Stagnography':
            self.labelText="Choose Stagnographed Image"
            self.mainButton="Choose Image"
        self.pushButton_2.setText(self.mainButton)
        self.label_4.setText(self.labelText)
        
    def decrypt_rsa(self):
        f = open('mykey.pem','r')
        key = RSA.importKey(f.read())
        pubKey = key.publickey()
        print(key)
        file2=(open(self.en_file[0],"rb"))
        content_f=file2.read()
        #content_e=bytes(content_f[2:-1],'utf-8')
        print("check====",content_f)
        file2.close()
        decryptor = PKCS1_OAEP.new(key)
        decrypted = decryptor.decrypt(content_f)
        decrypt_str=decrypted.decode('utf-8')
        return decrypt_str 
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", " Confidential Data Encryption and Decryption Based on KNN algorithm"))
        self.label_4.setText(_translate("Form", "Fetched data"))
        self.pushButton_2.setText(_translate("Form", "Decrypt"))
        self.pushButton_3.setText(_translate("Form", "Save File"))
        self.pushButton_4.setText(_translate("Form", "Select Method"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Filename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
