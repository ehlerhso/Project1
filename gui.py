# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GradesWindow(object):
    def setupUi(self, GradesWindow):
        GradesWindow.setObjectName("GradesWindow")
        GradesWindow.resize(359, 253)
        self.StudentLabel = QtWidgets.QLabel(parent=GradesWindow)
        self.StudentLabel.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.StudentLabel.setFont(font)
        self.StudentLabel.setObjectName("StudentLabel")
        self.ScoreLabel1 = QtWidgets.QLabel(parent=GradesWindow)
        self.ScoreLabel1.setGeometry(QtCore.QRect(10, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ScoreLabel1.setFont(font)
        self.ScoreLabel1.setObjectName("ScoreLabel1")
        self.StudentEntry = QtWidgets.QLineEdit(parent=GradesWindow)
        self.StudentEntry.setGeometry(QtCore.QRect(150, 10, 191, 31))
        self.StudentEntry.setObjectName("StudentEntry")
        self.AttemptsEntry = QtWidgets.QLineEdit(parent=GradesWindow)
        self.AttemptsEntry.setGeometry(QtCore.QRect(150, 50, 51, 31))
        self.AttemptsEntry.setObjectName("AttemptsEntry")
        self.Submit = QtWidgets.QPushButton(parent=GradesWindow)
        self.Submit.setGeometry(QtCore.QRect(220, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Submit.setFont(font)
        self.Submit.setObjectName("Submit")
        self.label = QtWidgets.QLabel(parent=GradesWindow)
        self.label.setGeometry(QtCore.QRect(220, 90, 131, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.NumberAttemptsLabel = QtWidgets.QLabel(parent=GradesWindow)
        self.NumberAttemptsLabel.setGeometry(QtCore.QRect(10, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumberAttemptsLabel.setFont(font)
        self.NumberAttemptsLabel.setObjectName("NumberAttemptsLabel")
        self.ScoreEntry1 = QtWidgets.QLineEdit(parent=GradesWindow)
        self.ScoreEntry1.setGeometry(QtCore.QRect(150, 90, 51, 31))
        self.ScoreEntry1.setObjectName("ScoreEntry1")

        self.retranslateUi(GradesWindow)
        QtCore.QMetaObject.connectSlotsByName(GradesWindow)

    def retranslateUi(self, GradesWindow):
        _translate = QtCore.QCoreApplication.translate
        GradesWindow.setWindowTitle(_translate("GradesWindow", "Student Grades"))
        self.StudentLabel.setText(_translate("GradesWindow", "Student name"))
        self.ScoreLabel1.setText(_translate("GradesWindow", "Score 1:"))
        self.Submit.setText(_translate("GradesWindow", "Submit"))
        self.label.setText(_translate("GradesWindow", "Please fill all values"))
        self.NumberAttemptsLabel.setText(_translate("GradesWindow", "No. of attempts"))
