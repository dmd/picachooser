# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'melodicompTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1750, 846)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(200, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-30, 0, 1771, 781))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pane1_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pane1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pane1_label.setObjectName("pane1_label")
        self.verticalLayout.addWidget(self.pane1_label)
        self.image_graphicsView_1 = GraphicsLayoutWidget(self.horizontalLayoutWidget)
        self.image_graphicsView_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_graphicsView_1.sizePolicy().hasHeightForWidth())
        self.image_graphicsView_1.setSizePolicy(sizePolicy)
        self.image_graphicsView_1.setMinimumSize(QtCore.QSize(100, 100))
        self.image_graphicsView_1.setMaximumSize(QtCore.QSize(1000, 1200))
        self.image_graphicsView_1.setSizeIncrement(QtCore.QSize(1, 1))
        self.image_graphicsView_1.setObjectName("image_graphicsView_1")
        self.verticalLayout.addWidget(self.image_graphicsView_1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pane2_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pane2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pane2_label.setObjectName("pane2_label")
        self.verticalLayout_2.addWidget(self.pane2_label)
        self.image_graphicsView_2 = GraphicsLayoutWidget(self.horizontalLayoutWidget)
        self.image_graphicsView_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_graphicsView_2.sizePolicy().hasHeightForWidth())
        self.image_graphicsView_2.setSizePolicy(sizePolicy)
        self.image_graphicsView_2.setMinimumSize(QtCore.QSize(100, 100))
        self.image_graphicsView_2.setMaximumSize(QtCore.QSize(1000, 1200))
        self.image_graphicsView_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.image_graphicsView_2.setObjectName("image_graphicsView_2")
        self.verticalLayout_2.addWidget(self.image_graphicsView_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1750, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pane1_label.setText(
            _translate("MainWindow", "Component XX of XX: XX.X% explained var., XX.X% total var.")
        )
        self.pane2_label.setText(
            _translate("MainWindow", "Component XX of XX: XX.X% explained var., XX.X% total var.")
        )


from pyqtgraph import GraphicsLayoutWidget
