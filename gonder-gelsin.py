import sys, socket, os, time
from PyQt5 import QtCore, QtGui, QtWidgets
global adr
adr = ''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 478)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 441, 451))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.button_dosyasec = QtWidgets.QPushButton(self.tab)
        self.button_dosyasec.setGeometry(QtCore.QRect(310, 60, 93, 28))
        self.button_dosyasec.setObjectName("button_dosyasec")
        self.button_dosyasec.clicked.connect(self.button_dosyasec_islev)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 60, 281, 22))
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.label_1 = QtWidgets.QLabel(self.tab)
        self.label_1.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_1.setObjectName("label_1")

        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(20, 170, 401, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setEnabled(False)
        self.progressBar.setObjectName("progressBar")

        self.button_gonder = QtWidgets.QPushButton(self.tab)
        self.button_gonder.setGeometry(QtCore.QRect(170, 280, 93, 28))
        self.button_gonder.setObjectName("button_gonder")
        self.button_gonder.clicked.connect(self.button_gonder_islev)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 70, 161, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(15)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 351, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 351, 400))
        self.label_3.setObjectName("label_4")

        self.button_al = QtWidgets.QPushButton(self.tab_2)
        self.button_al.setGeometry(QtCore.QRect(170, 280, 93, 28))
        self.button_al.setObjectName("button_al")
        self.button_al.clicked.connect(self.button_al_islev)



        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gönder-gelsin-v1.0"))
        self.button_dosyasec.setText(_translate("MainWindow", "Dosya Seç"))
        self.label_1.setText(_translate("MainWindow", "Dosya Uzantısı :"))
        self.button_gonder.setText(_translate("MainWindow", "Gönder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dosya Gönder"))
        self.label_2.setText(_translate("MainWindow", "Server IP:"))
        self.label_3.setText(_translate("MainWindow", "Durum :"))
        self.button_al.setText(_translate("MainWindow", "Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Dosya Al"))
        self.label_4.setText(_translate("MainWindow", "İLK ÖNCE DOSYA GÖNDERME İŞLEMİNİ BAŞLATIN !"))
    def button_dosyasec_islev(self):
        dosya_konumu = QtWidgets.QFileDialog.getOpenFileName()
        self.dosya_konumu = dosya_konumu[0]
        self.lineEdit_1.setText(self.dosya_konumu)

    def button_al_islev(self):
        self.host_ip = self.lineEdit_2.text()
        self.dosyaAl(self.host_ip)

    def button_gonder_islev(self):
        if self.lineEdit_1.text() == '':
            err_message = QtWidgets.QErrorMessage()
            err_message.showMessage('Dosya giriniz !')
            err_message.exec()
        else:
            self.button_gonder.setEnabled(False)
            self.dosyaVer(self.lineEdit_1.text())



    def dosyaVer(self,path):
        host = ""
        port = 14555
        ser_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ser_soc.bind((host, port))
        ser_soc.listen()

        new_soc, adr = ser_soc.accept()

        yeni_konum_liste = self.dosya_konumu.split('/')
        self.dosya_adi = yeni_konum_liste[-1]
        yeni_konum = ''
        for i in yeni_konum_liste:
            yeni_konum += i+'\\'
        self.yeni_konum = yeni_konum[:-1]

        dosya_adi_bin = self.dosya_adi.encode()
        new_soc.send(dosya_adi_bin)

        dosya = os.stat(self.yeni_konum)
        self.progressBar.setEnabled(True)
        self.tab_2.setEnabled(False)
        sum = 0
        with open(self.yeni_konum, 'rb') as d:
            data = d.read(1024)
            while (data):
                new_soc.send(data)
                sum += 1024
                yuzdelik = (100 * sum) / (dosya.st_size)
                self.progressBar.setValue(int(yuzdelik))

                data = d.read(1024)
        self.progressBar.setValue(100)
        time.sleep(0.5)
        new_soc.close()
        self.progressBar.setValue(0)
        self.progressBar.setEnabled(False)
        self.button_gonder.setEnabled(True)
        self.tab_2.setEnabled(True)

    def dosyaAl(self, ip):
        host = ip
        port = 14555
        cli_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli_soc.connect((host, port))

        self.button_al.setEnabled(False)

        dosya_adi_bin_1 = cli_soc.recv(1024)
        dosya_adi_1 = dosya_adi_bin_1.decode('ascii')
        

        file = open('.\\alınan\\'+dosya_adi_1, 'wb')
        self.tab.setEnabled(False)
        data = cli_soc.recv(1024)
        flag = True
        while (data):
            file.write(data)
            data = cli_soc.recv(1024)
            if flag:
                self.label_3.setText('Durum:Dosya Alınıyor...')
                flag = False
        self.label_3.setText('Durum:Dosya Alındı')
        cli_soc.close()
        file.close()
        self.tab.setEnabled(True)
        self.button_al.setEnabled(True)




if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    app.exec()
