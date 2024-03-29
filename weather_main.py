# Form implementation generated from reading ui file 'weathermain.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_weathermain(object):
    def setupUi(self, weathermain):
        weathermain.setObjectName("weathermain")
        weathermain.resize(333, 428)
        weathermain.setMinimumSize(QtCore.QSize(333, 428))
        weathermain.setMaximumSize(QtCore.QSize(333, 428))
        self.centralwidget = QtWidgets.QWidget(parent=weathermain)
        self.centralwidget.setObjectName("centralwidget")
        self.weather_app_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.weather_app_title.setGeometry(QtCore.QRect(40, 40, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.weather_app_title.setFont(font)
        self.weather_app_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weather_app_title.setObjectName("weather_app_title")
        self.instruction_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.instruction_text.setGeometry(QtCore.QRect(70, 110, 181, 171))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.instruction_text.setFont(font)
        self.instruction_text.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.instruction_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.instruction_text.setWordWrap(True)
        self.instruction_text.setObjectName("instruction_text")
        self.city_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.city_input.setGeometry(QtCore.QRect(60, 300, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.city_input.setFont(font)
        self.city_input.setFrame(True)
        self.city_input.setObjectName("city_input")
        self.enter_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(120, 352, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setObjectName("enter_button")
        weathermain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=weathermain)
        self.statusbar.setObjectName("statusbar")
        weathermain.setStatusBar(self.statusbar)

        self.retranslateUi(weathermain)
        QtCore.QMetaObject.connectSlotsByName(weathermain)

    def retranslateUi(self, weathermain):
        _translate = QtCore.QCoreApplication.translate
        weathermain.setWindowTitle(_translate("weathermain", "Weather App"))
        self.weather_app_title.setText(_translate("weathermain", "Weather App"))
        self.instruction_text.setText(_translate("weathermain", "Enter your City."))
        self.enter_button.setText(_translate("weathermain", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    weathermain = QtWidgets.QMainWindow()
    ui = Ui_weathermain()
    ui.setupUi(weathermain)
    weathermain.show()
    sys.exit(app.exec())
