# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 301)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 179, 200, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(8)
        font.setKerning(True)
        self.listWidget.setFont(font)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignHCenter)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setEnabled(True)
        self.image_label.setGeometry(QtCore.QRect(225, 20, 320, 240))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QtCore.QSize(320, 240))
        self.image_label.setObjectName("image_label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(560, 10, 201, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(200, 150))
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(9, 9, 200, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(348, 264, 75, 23))
        self.control_bt.setObjectName("control_bt")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(460, 270, 71, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "1. 新建项目"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "2. 新建项目"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "3. 新建项目"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.image_label.setText(_translate("Form", "TextLabel"))
        self.plainTextEdit.setPlainText(_translate("Form", "Text\n"
""))
        self.control_bt.setText(_translate("Form", "Start"))
        self.checkBox.setText(_translate("Form", "Speaker"))
