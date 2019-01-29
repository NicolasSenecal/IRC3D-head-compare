# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 447)
        MainWindow.setMinimumSize(QtCore.QSize(800, 350))
        self.MainWindows = QtWidgets.QWidget(MainWindow)
        self.MainWindows.setObjectName("MainWindows")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWindows)
        self.gridLayout.setObjectName("gridLayout")
        self.gridViewerLayout = QtWidgets.QGridLayout()
        self.gridViewerLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridViewerLayout.setSpacing(0)
        self.gridViewerLayout.setObjectName("gridViewerLayout")
        self.frame = QtWidgets.QFrame(self.MainWindows)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VideoWidget = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.VideoWidget.sizePolicy().hasHeightForWidth())
        self.VideoWidget.setSizePolicy(sizePolicy)
        self.VideoWidget.setBaseSize(QtCore.QSize(0, 0))
        self.VideoWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.VideoWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.VideoWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.VideoWidget.setBackgroundBrush(brush)
        self.VideoWidget.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.VideoWidget.setCacheMode(QtWidgets.QGraphicsView.CacheNone)
        self.VideoWidget.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.VideoWidget.setObjectName("VideoWidget")
        self.horizontalLayout.addWidget(self.VideoWidget)
        self.GLWidget = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.GLWidget.sizePolicy().hasHeightForWidth())
        self.GLWidget.setSizePolicy(sizePolicy)
        self.GLWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GLWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.GLWidget.setBackgroundBrush(brush)
        self.GLWidget.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.GLWidget.setObjectName("GLWidget")
        self.horizontalLayout.addWidget(self.GLWidget)
        self.gridViewerLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridViewerLayout, 0, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(5, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.videoProcessTable = QtWidgets.QTableWidget(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoProcessTable.sizePolicy().hasHeightForWidth())
        self.videoProcessTable.setSizePolicy(sizePolicy)
        self.videoProcessTable.setMaximumSize(QtCore.QSize(16777215, 10))
        self.videoProcessTable.setLineWidth(0)
        self.videoProcessTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.videoProcessTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.videoProcessTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.videoProcessTable.setAutoScroll(False)
        self.videoProcessTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.videoProcessTable.setTabKeyNavigation(False)
        self.videoProcessTable.setProperty("showDropIndicator", False)
        self.videoProcessTable.setDragDropOverwriteMode(False)
        self.videoProcessTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.videoProcessTable.setTextElideMode(QtCore.Qt.ElideNone)
        self.videoProcessTable.setShowGrid(False)
        self.videoProcessTable.setGridStyle(QtCore.Qt.SolidLine)
        self.videoProcessTable.setRowCount(1)
        self.videoProcessTable.setColumnCount(1)
        self.videoProcessTable.setObjectName("videoProcessTable")
        self.videoProcessTable.horizontalHeader().setVisible(False)
        self.videoProcessTable.horizontalHeader().setCascadingSectionResizes(False)
        self.videoProcessTable.horizontalHeader().setDefaultSectionSize(0)
        self.videoProcessTable.horizontalHeader().setHighlightSections(False)
        self.videoProcessTable.horizontalHeader().setMinimumSectionSize(0)
        self.videoProcessTable.horizontalHeader().setSortIndicatorShown(False)
        self.videoProcessTable.horizontalHeader().setStretchLastSection(False)
        self.videoProcessTable.verticalHeader().setVisible(False)
        self.videoProcessTable.verticalHeader().setDefaultSectionSize(10)
        self.videoProcessTable.verticalHeader().setMinimumSectionSize(10)
        self.horizontalLayout_2.addWidget(self.videoProcessTable)
        spacerItem1 = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.videoSlider = QtWidgets.QSlider(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoSlider.sizePolicy().hasHeightForWidth())
        self.videoSlider.setSizePolicy(sizePolicy)
        self.videoSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.videoSlider.setMaximum(1)
        self.videoSlider.setOrientation(QtCore.Qt.Horizontal)
        self.videoSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.videoSlider.setTickInterval(1)
        self.videoSlider.setObjectName("videoSlider")
        self.verticalLayout_3.addWidget(self.videoSlider)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.topButtons = QtWidgets.QHBoxLayout()
        self.topButtons.setSpacing(6)
        self.topButtons.setObjectName("topButtons")
        self.last10Frame_PB = QtWidgets.QPushButton(self.MainWindows)
        self.last10Frame_PB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/last-10frame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.last10Frame_PB.setIcon(icon)
        self.last10Frame_PB.setIconSize(QtCore.QSize(16, 16))
        self.last10Frame_PB.setObjectName("last10Frame_PB")
        self.topButtons.addWidget(self.last10Frame_PB)
        self.lastFrame_PB = QtWidgets.QPushButton(self.MainWindows)
        self.lastFrame_PB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/last-frame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastFrame_PB.setIcon(icon1)
        self.lastFrame_PB.setIconSize(QtCore.QSize(16, 16))
        self.lastFrame_PB.setObjectName("lastFrame_PB")
        self.topButtons.addWidget(self.lastFrame_PB)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.topButtons.addItem(spacerItem2)
        self.read_PB = QtWidgets.QPushButton(self.MainWindows)
        self.read_PB.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.read_PB.setIcon(icon2)
        self.read_PB.setObjectName("read_PB")
        self.topButtons.addWidget(self.read_PB)
        self.headPosition_PB = QtWidgets.QPushButton(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headPosition_PB.sizePolicy().hasHeightForWidth())
        self.headPosition_PB.setSizePolicy(sizePolicy)
        self.headPosition_PB.setObjectName("headPosition_PB")
        self.topButtons.addWidget(self.headPosition_PB)
        self.pause_PB = QtWidgets.QPushButton(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_PB.sizePolicy().hasHeightForWidth())
        self.pause_PB.setSizePolicy(sizePolicy)
        self.pause_PB.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_PB.setIcon(icon3)
        self.pause_PB.setObjectName("pause_PB")
        self.topButtons.addWidget(self.pause_PB)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.topButtons.addItem(spacerItem3)
        self.nextFrame_PB = QtWidgets.QPushButton(self.MainWindows)
        self.nextFrame_PB.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/next-frame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextFrame_PB.setIcon(icon4)
        self.nextFrame_PB.setObjectName("nextFrame_PB")
        self.topButtons.addWidget(self.nextFrame_PB)
        self.next10Frame_PB = QtWidgets.QPushButton(self.MainWindows)
        self.next10Frame_PB.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/next-10frame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next10Frame_PB.setIcon(icon5)
        self.next10Frame_PB.setObjectName("next10Frame_PB")
        self.topButtons.addWidget(self.next10Frame_PB)
        self.gridLayout.addLayout(self.topButtons, 2, 0, 1, 1)
        self.bottomButtons = QtWidgets.QHBoxLayout()
        self.bottomButtons.setObjectName("bottomButtons")
        self.square_BT = QtWidgets.QPushButton(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.square_BT.sizePolicy().hasHeightForWidth())
        self.square_BT.setSizePolicy(sizePolicy)
        self.square_BT.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.square_BT.setIcon(icon6)
        self.square_BT.setObjectName("square_BT")
        self.bottomButtons.addWidget(self.square_BT)
        self.coordinates_PB = QtWidgets.QPushButton(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coordinates_PB.sizePolicy().hasHeightForWidth())
        self.coordinates_PB.setSizePolicy(sizePolicy)
        self.coordinates_PB.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/coordinates.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.coordinates_PB.setIcon(icon7)
        self.coordinates_PB.setObjectName("coordinates_PB")
        self.bottomButtons.addWidget(self.coordinates_PB)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.bottomButtons.addItem(spacerItem4)
        self.processAllVideo_PB = QtWidgets.QPushButton(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processAllVideo_PB.sizePolicy().hasHeightForWidth())
        self.processAllVideo_PB.setSizePolicy(sizePolicy)
        self.processAllVideo_PB.setObjectName("processAllVideo_PB")
        self.bottomButtons.addWidget(self.processAllVideo_PB)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.bottomButtons.addItem(spacerItem5)
        self.confidenceLayout = QtWidgets.QHBoxLayout()
        self.confidenceLayout.setObjectName("confidenceLayout")
        self.confidenceTitle = QtWidgets.QLabel(self.MainWindows)
        self.confidenceTitle.setObjectName("confidenceTitle")
        self.confidenceLayout.addWidget(self.confidenceTitle)
        self.confidenceSlider = QtWidgets.QSlider(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confidenceSlider.sizePolicy().hasHeightForWidth())
        self.confidenceSlider.setSizePolicy(sizePolicy)
        self.confidenceSlider.setMaximum(200)
        self.confidenceSlider.setSingleStep(5)
        self.confidenceSlider.setPageStep(5)
        self.confidenceSlider.setProperty("value", 75)
        self.confidenceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.confidenceSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.confidenceSlider.setTickInterval(1)
        self.confidenceSlider.setObjectName("confidenceSlider")
        self.confidenceLayout.addWidget(self.confidenceSlider)
        self.confidenceInfo = QtWidgets.QLabel(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confidenceInfo.sizePolicy().hasHeightForWidth())
        self.confidenceInfo.setSizePolicy(sizePolicy)
        self.confidenceInfo.setObjectName("confidenceInfo")
        self.confidenceLayout.addWidget(self.confidenceInfo)
        self.bottomButtons.addLayout(self.confidenceLayout)
        self.gridLayout.addLayout(self.bottomButtons, 3, 0, 1, 1)
        self.Info = QtWidgets.QHBoxLayout()
        self.Info.setSpacing(0)
        self.Info.setObjectName("Info")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameInfo = QtWidgets.QLabel(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameInfo.sizePolicy().hasHeightForWidth())
        self.frameInfo.setSizePolicy(sizePolicy)
        self.frameInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.frameInfo.setObjectName("frameInfo")
        self.verticalLayout_2.addWidget(self.frameInfo)
        self.facesInfo = QtWidgets.QLabel(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.facesInfo.sizePolicy().hasHeightForWidth())
        self.facesInfo.setSizePolicy(sizePolicy)
        self.facesInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.facesInfo.setObjectName("facesInfo")
        self.verticalLayout_2.addWidget(self.facesInfo)
        self.Info.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.videoInfo = QtWidgets.QLabel(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoInfo.sizePolicy().hasHeightForWidth())
        self.videoInfo.setSizePolicy(sizePolicy)
        self.videoInfo.setTextFormat(QtCore.Qt.AutoText)
        self.videoInfo.setScaledContents(False)
        self.videoInfo.setWordWrap(True)
        self.videoInfo.setOpenExternalLinks(False)
        self.videoInfo.setObjectName("videoInfo")
        self.verticalLayout.addWidget(self.videoInfo)
        self.modelInfo = QtWidgets.QLabel(self.MainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelInfo.sizePolicy().hasHeightForWidth())
        self.modelInfo.setSizePolicy(sizePolicy)
        self.modelInfo.setTextFormat(QtCore.Qt.AutoText)
        self.modelInfo.setScaledContents(False)
        self.modelInfo.setWordWrap(True)
        self.modelInfo.setOpenExternalLinks(False)
        self.modelInfo.setObjectName("modelInfo")
        self.verticalLayout.addWidget(self.modelInfo)
        self.Info.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.Info, 2, 1, 2, 1)
        self.topGLUtils = QtWidgets.QHBoxLayout()
        self.topGLUtils.setObjectName("topGLUtils")
        self.fovyTitle = QtWidgets.QLabel(self.MainWindows)
        self.fovyTitle.setObjectName("fovyTitle")
        self.topGLUtils.addWidget(self.fovyTitle)
        self.fovySlider = QtWidgets.QSlider(self.MainWindows)
        self.fovySlider.setMinimum(0)
        self.fovySlider.setMaximum(180)
        self.fovySlider.setProperty("value", 20)
        self.fovySlider.setOrientation(QtCore.Qt.Horizontal)
        self.fovySlider.setTickInterval(1)
        self.fovySlider.setObjectName("fovySlider")
        self.topGLUtils.addWidget(self.fovySlider)
        self.fovyInfo = QtWidgets.QLabel(self.MainWindows)
        self.fovyInfo.setObjectName("fovyInfo")
        self.topGLUtils.addWidget(self.fovyInfo)
        self.gridLayout.addLayout(self.topGLUtils, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.MainWindows)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_video = QtWidgets.QAction(MainWindow)
        self.actionOpen_video.setObjectName("actionOpen_video")
        self.actionOpen_model = QtWidgets.QAction(MainWindow)
        self.actionOpen_model.setObjectName("actionOpen_model")
        self.menuFile.addAction(self.actionOpen_video)
        self.menuFile.addAction(self.actionOpen_model)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.videoProcessTable.setSortingEnabled(False)
        self.headPosition_PB.setText(_translate("MainWindow", "Get head position"))
        self.processAllVideo_PB.setText(_translate("MainWindow", "Process all video"))
        self.confidenceTitle.setText(_translate("MainWindow", "Confidence"))
        self.confidenceInfo.setText(_translate("MainWindow", "0.75"))
        self.frameInfo.setText(_translate("MainWindow", "Frame: ..."))
        self.facesInfo.setText(_translate("MainWindow", "Frame not process"))
        self.videoInfo.setText(_translate("MainWindow", "Video: ..."))
        self.modelInfo.setText(_translate("MainWindow", "Model: ..."))
        self.fovyTitle.setText(_translate("MainWindow", "Field of view"))
        self.fovyInfo.setText(_translate("MainWindow", "0.20"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_video.setText(_translate("MainWindow", "Open video..."))
        self.actionOpen_model.setText(_translate("MainWindow", "Open model..."))

from ui import icons_rc
