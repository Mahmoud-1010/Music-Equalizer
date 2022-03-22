
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 884)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 391, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ExitButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ExitButton.sizePolicy().hasHeightForWidth())
        self.ExitButton.setSizePolicy(sizePolicy)
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ExitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("exit.PNG"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon)
        self.ExitButton.setIconSize(QtCore.QSize(25, 25))
        self.ExitButton.setFlat(True)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.play = QtWidgets.QPushButton(self.layoutWidget)
        self.play.setAutoFillBackground(False)
        self.play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("play.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon1)
        self.play.setIconSize(QtCore.QSize(25, 25))
        self.play.setDefault(False)
        self.play.setFlat(True)
        self.play.setObjectName("play")
        self.horizontalLayout.addWidget(self.play)
        self.pause = QtWidgets.QPushButton(self.layoutWidget)
        self.pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pause.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon2)
        self.pause.setIconSize(QtCore.QSize(25, 25))
        self.pause.setFlat(True)
        self.pause.setObjectName("pause")
        self.horizontalLayout.addWidget(self.pause)
        self.zoom_in = QtWidgets.QPushButton(self.layoutWidget)
        self.zoom_in.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("zoomin.PNG"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in.setIcon(icon3)
        self.zoom_in.setIconSize(QtCore.QSize(30, 30))
        self.zoom_in.setFlat(True)
        self.zoom_in.setObjectName("zoom_in")
        self.horizontalLayout.addWidget(self.zoom_in)
        self.zoom_out = QtWidgets.QPushButton(self.layoutWidget)
        self.zoom_out.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("zoom out.PNG"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon4)
        self.zoom_out.setIconSize(QtCore.QSize(30, 30))
        self.zoom_out.setFlat(True)
        self.zoom_out.setObjectName("zoom_out")
        self.horizontalLayout.addWidget(self.zoom_out)
        self.zoomx = QtWidgets.QPushButton(self.layoutWidget)
        self.zoomx.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoom x.PNG"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomx.setIcon(icon5)
        self.zoomx.setIconSize(QtCore.QSize(100, 100))
        self.zoomx.setFlat(True)
        self.zoomx.setObjectName("zoomx")
        self.horizontalLayout.addWidget(self.zoomx)
        self.zoomy = QtWidgets.QPushButton(self.layoutWidget)
        self.zoomy.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zoom y.PNG"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomy.setIcon(icon6)
        self.zoomy.setIconSize(QtCore.QSize(50, 50))
        self.zoomy.setFlat(True)
        self.zoomy.setObjectName("zoomy")
        self.horizontalLayout.addWidget(self.zoomy)
        self.clear_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.clear_Button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(
            "delete-button-pngrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_Button.setIcon(icon7)
        self.clear_Button.setIconSize(QtCore.QSize(25, 25))
        self.clear_Button.setFlat(True)
        self.clear_Button.setObjectName("clear_Button")
        self.horizontalLayout.addWidget(self.clear_Button)
        self.Export = QtWidgets.QPushButton(self.layoutWidget)
        self.Export.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pdf-file.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Export.setIcon(icon8)
        self.Export.setIconSize(QtCore.QSize(25, 25))
        self.Export.setFlat(True)
        self.Export.setObjectName("Export")
        self.horizontalLayout.addWidget(self.Export)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(430, 20, 177, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scroll_x = QtWidgets.QSlider(self.layoutWidget1)
        self.scroll_x.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.scroll_x.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_x.setObjectName("scroll_x")
        self.horizontalLayout_2.addWidget(self.scroll_x)
        self.scroll_y = QtWidgets.QSlider(self.layoutWidget1)
        self.scroll_y.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_y.setObjectName("scroll_y")
        self.horizontalLayout_2.addWidget(self.scroll_y)
        self.Channel_1 = PlotWidget(self.centralwidget)
        self.Channel_1.setGeometry(QtCore.QRect(40, 120, 511, 231))
        self.Channel_1.setObjectName("Channel_1")
        self.Channel_2 = PlotWidget(self.centralwidget)
        self.Channel_2.setGeometry(QtCore.QRect(40, 600, 511, 231))
        self.Channel_2.setObjectName("Channel_2")
        self.label_Channel2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Channel2.setGeometry(QtCore.QRect(40, 570, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Channel2.setFont(font)
        self.label_Channel2.setObjectName("label_Channel2")
        self.label_Channel1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Channel1.setGeometry(QtCore.QRect(40, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Channel1.setFont(font)
        self.label_Channel1.setObjectName("label_Channel1")
        self.r2 = QtWidgets.QRadioButton(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(40, 550, 16, 16))
        self.r2.setText("")
        self.r2.setObjectName("r2")
        self.r2.value = 2
        self.r1 = QtWidgets.QRadioButton(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(40, 70, 16, 21))
        self.r1.setText("")
        self.r1.setObjectName("r1")
        self.r1.value = 1
        self.slider_1 = QtWidgets.QSlider(self.centralwidget)
        self.slider_1.setGeometry(QtCore.QRect(60, 360, 22, 160))
        self.slider_1.setMaximum(10)
        self.slider_1.setPageStep(1)
        self.slider_1.setProperty("value", 1)
        self.slider_1.setOrientation(QtCore.Qt.Vertical)
        self.slider_1.setObjectName("slider_1")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 520, 41, 23))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 1.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.slider_2 = QtWidgets.QSlider(self.centralwidget)
        self.slider_2.setGeometry(QtCore.QRect(110, 360, 22, 160))
        self.slider_2.setMaximum(10)
        self.slider_2.setPageStep(1)
        self.slider_2.setProperty("value", 1)
        self.slider_2.setOrientation(QtCore.Qt.Vertical)
        self.slider_2.setObjectName("slider_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(100, 520, 41, 23))
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 1.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.slider_3 = QtWidgets.QSlider(self.centralwidget)
        self.slider_3.setGeometry(QtCore.QRect(160, 360, 22, 160))
        self.slider_3.setMaximum(10)
        self.slider_3.setPageStep(1)
        self.slider_3.setProperty("value", 1)
        self.slider_3.setOrientation(QtCore.Qt.Vertical)
        self.slider_3.setObjectName("slider_3")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(150, 520, 41, 23))
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setProperty("value", 1.0)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.slider_4 = QtWidgets.QSlider(self.centralwidget)
        self.slider_4.setGeometry(QtCore.QRect(210, 360, 22, 160))
        self.slider_4.setMaximum(10)
        self.slider_4.setPageStep(1)
        self.slider_4.setProperty("value", 1)
        self.slider_4.setOrientation(QtCore.Qt.Vertical)
        self.slider_4.setObjectName("slider_4")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(200, 520, 41, 23))
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setProperty("value", 1.0)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.slider_5 = QtWidgets.QSlider(self.centralwidget)
        self.slider_5.setGeometry(QtCore.QRect(260, 360, 22, 160))
        self.slider_5.setMaximum(10)
        self.slider_5.setPageStep(1)
        self.slider_5.setProperty("value", 1)
        self.slider_5.setOrientation(QtCore.Qt.Vertical)
        self.slider_5.setObjectName("slider_5")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(250, 520, 41, 23))
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setProperty("value", 1.0)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.slider_6 = QtWidgets.QSlider(self.centralwidget)
        self.slider_6.setGeometry(QtCore.QRect(310, 360, 22, 160))
        self.slider_6.setMaximum(10)
        self.slider_6.setPageStep(1)
        self.slider_6.setProperty("value", 1)
        self.slider_6.setOrientation(QtCore.Qt.Vertical)
        self.slider_6.setObjectName("slider_6")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(300, 520, 41, 23))
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.setProperty("value", 1.0)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.slider_7 = QtWidgets.QSlider(self.centralwidget)
        self.slider_7.setGeometry(QtCore.QRect(360, 360, 22, 160))
        self.slider_7.setMaximum(10)
        self.slider_7.setPageStep(1)
        self.slider_7.setProperty("value", 1)
        self.slider_7.setOrientation(QtCore.Qt.Vertical)
        self.slider_7.setObjectName("slider_7")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(350, 520, 41, 23))
        self.lcdNumber_7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_7.setProperty("value", 1.0)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.slider_8 = QtWidgets.QSlider(self.centralwidget)
        self.slider_8.setGeometry(QtCore.QRect(410, 360, 22, 160))
        self.slider_8.setMaximum(10)
        self.slider_8.setPageStep(1)
        self.slider_8.setProperty("value", 1)
        self.slider_8.setOrientation(QtCore.Qt.Vertical)
        self.slider_8.setObjectName("slider_8")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(400, 520, 41, 23))
        self.lcdNumber_8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_8.setProperty("value", 1.0)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.slider_9 = QtWidgets.QSlider(self.centralwidget)
        self.slider_9.setGeometry(QtCore.QRect(450, 360, 22, 160))
        self.slider_9.setMaximum(10)
        self.slider_9.setPageStep(1)
        self.slider_9.setProperty("value", 1)
        self.slider_9.setOrientation(QtCore.Qt.Vertical)
        self.slider_9.setObjectName("slider_9")
        self.slider_10 = QtWidgets.QSlider(self.centralwidget)
        self.slider_10.setGeometry(QtCore.QRect(490, 360, 21, 160))
        self.slider_10.setMaximum(10)
        self.slider_10.setPageStep(1)
        self.slider_10.setProperty("value", 1)
        self.slider_10.setOrientation(QtCore.Qt.Vertical)
        self.slider_10.setObjectName("slider_10")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setGeometry(QtCore.QRect(440, 520, 41, 23))
        self.lcdNumber_9.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_9.setProperty("value", 1.0)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_10.setGeometry(QtCore.QRect(490, 520, 41, 23))
        self.lcdNumber_10.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_10.setProperty("value", 1.0)
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.label_Spectrogram_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Spectrogram_1.setGeometry(QtCore.QRect(570, 90, 217, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Spectrogram_1.setFont(font)
        self.label_Spectrogram_1.setObjectName("label_Spectrogram_1")
        self.Spectrogram_1 = pg.GraphicsLayoutWidget(self.centralwidget)
        self.Spectrogram_1.setGeometry(QtCore.QRect(570, 120, 511, 321))
        self.Spectrogram_1.setObjectName("Spectrogram_1")
        self.r4 = QtWidgets.QRadioButton(self.centralwidget)
        self.r4.setGeometry(QtCore.QRect(570, 450, 16, 16))
        self.r4.setText("")
        self.r4.setObjectName("r4")
        self.r4.value = 4
        self.label_Spectrogram_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Spectrogram_2.setGeometry(QtCore.QRect(570, 473, 216, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Spectrogram_2.setFont(font)
        self.label_Spectrogram_2.setObjectName("label_Spectrogram_2")
        self.Spectrogram_2 = pg.GraphicsLayoutWidget(self.centralwidget)
        self.Spectrogram_2.setGeometry(QtCore.QRect(570, 510, 511, 321))
        self.Spectrogram_2.setObjectName("Spectrogram_2")
        self.r3 = QtWidgets.QRadioButton(self.centralwidget)
        self.r3.setGeometry(QtCore.QRect(570, 70, 16, 16))
        self.r3.setText("")
        self.r3.setObjectName("r3")
        self.r3.value = 3
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Play_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Play_Signal_1.setObjectName("Play_Signal_1")
        self.Pause_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Pause_Signal_1.setObjectName("Pause_Signal_1")
        self.Clear_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Clear_Signal_1.setObjectName("Clear_Signal_1")
        self.Play_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Play_Signal_2.setObjectName("Play_Signal_2")
        self.Pause_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Pause_Signal_2.setObjectName("Pause_Signal_2")
        self.Clear_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Clear_Signal_2.setObjectName("Clear_Signal_2")
        self.Play_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Play_Signal_3.setObjectName("Play_Signal_3")
        self.Pause_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Pause_Signal_3.setObjectName("Pause_Signal_3")
        self.Clear_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Clear_Signal_3.setObjectName("Clear_Signal_3")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionOpen_3 = QtWidgets.QAction(MainWindow)
        self.actionOpen_3.setObjectName("actionOpen_3")
        self.OpenChannel_1 = QtWidgets.QAction(MainWindow)
        self.OpenChannel_1.setObjectName("OpenChannel_1")
        self.OpenChannel_2 = QtWidgets.QAction(MainWindow)
        self.OpenChannel_2.setObjectName("OpenChannel_2")
        self.OpenChannel_3 = QtWidgets.QAction(MainWindow)
        self.OpenChannel_3.setObjectName("OpenChannel_3")
        self.zoom_x_Signal_1 = QtWidgets.QAction(MainWindow)
        self.zoom_x_Signal_1.setObjectName("zoom_x_Signal_1")
        self.zoom_x_Signal_2 = QtWidgets.QAction(MainWindow)
        self.zoom_x_Signal_2.setObjectName("zoom_x_Signal_2")
        self.zoom_x_Signal_3 = QtWidgets.QAction(MainWindow)
        self.zoom_x_Signal_3.setObjectName("zoom_x_Signal_3")
        self.zoom_y_Signal_1 = QtWidgets.QAction(MainWindow)
        self.zoom_y_Signal_1.setObjectName("zoom_y_Signal_1")
        self.zoom_y_Signal_2 = QtWidgets.QAction(MainWindow)
        self.zoom_y_Signal_2.setObjectName("zoom_y_Signal_2")
        self.zoom_y_Signal_3 = QtWidgets.QAction(MainWindow)
        self.zoom_y_Signal_3.setObjectName("zoom_y_Signal_3")
        self.Export_Signal_1 = QtWidgets.QAction(MainWindow)
        self.Export_Signal_1.setObjectName("Export_Signal_1")
        self.Export_Signal_2 = QtWidgets.QAction(MainWindow)
        self.Export_Signal_2.setObjectName("Export_Signal_2")
        self.Export_Signal_3 = QtWidgets.QAction(MainWindow)
        self.Export_Signal_3.setObjectName("Export_Signal_3")
        self.original_Spectrogram = QtWidgets.QAction(MainWindow)
        self.original_Spectrogram.setObjectName("original_Spectrogram")
        self.Signal_2_Spectrogram = QtWidgets.QAction(MainWindow)
        self.Signal_2_Spectrogram.setObjectName("Signal_2_Spectrogram")
        self.Signal_3_Spectrogram = QtWidgets.QAction(MainWindow)
        self.Signal_3_Spectrogram.setObjectName("Signal_3_Spectrogram")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionZoom_X = QtWidgets.QAction(MainWindow)
        self.actionZoom_X.setObjectName("actionZoom_X")
        self.actionZoom_Y = QtWidgets.QAction(MainWindow)
        self.actionZoom_Y.setObjectName("actionZoom_Y")
        self.actionopen_file = QtWidgets.QAction(MainWindow)
        self.actionopen_file.setObjectName("actionopen_file")
        self.actionnew_window = QtWidgets.QAction(MainWindow)
        self.actionnew_window.setObjectName("actionnew_window")
        self.menuFile.addAction(self.actionopen_file)
        self.menuFile.addAction(self.actionnew_window)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionZoom_X)
        self.menuView.addAction(self.actionZoom_Y)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.slider_1.valueChanged['int'].connect(self.lcdNumber.display)
        self.slider_2.valueChanged['int'].connect(self.lcdNumber_2.display)
        self.slider_3.valueChanged['int'].connect(self.lcdNumber_3.display)
        self.slider_4.valueChanged['int'].connect(self.lcdNumber_4.display)
        self.slider_5.valueChanged['int'].connect(self.lcdNumber_5.display)
        self.slider_6.valueChanged['int'].connect(self.lcdNumber_6.display)
        self.slider_7.valueChanged['int'].connect(self.lcdNumber_7.display)
        self.slider_8.valueChanged['int'].connect(self.lcdNumber_8.display)
        self.slider_9.valueChanged['int'].connect(self.lcdNumber_9.display)
        self.slider_10.valueChanged['int'].connect(self.lcdNumber_10.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ExitButton.setToolTip(_translate("MainWindow", "exit"))
        self.ExitButton.setShortcut(_translate("MainWindow", "Esc"))
        self.play.setToolTip(_translate("MainWindow", "play"))
        self.play.setShortcut(_translate("MainWindow", "P"))
        self.pause.setToolTip(_translate("MainWindow", "pause"))
        self.pause.setShortcut(_translate("MainWindow", "S"))
        self.zoom_in.setToolTip(_translate("MainWindow", "zoom in "))
        self.zoom_in.setShortcut(_translate("MainWindow", "+"))
        self.zoom_out.setToolTip(_translate("MainWindow", "zoom out"))
        self.zoom_out.setShortcut(_translate("MainWindow", "-"))
        self.zoomx.setToolTip(_translate("MainWindow", "zoom x"))
        self.zoomx.setShortcut(_translate("MainWindow", "X"))
        self.zoomy.setToolTip(_translate("MainWindow", "zoom y"))
        self.zoomy.setShortcut(_translate("MainWindow", "Y"))
        self.clear_Button.setToolTip(_translate("MainWindow", "clear"))
        self.clear_Button.setShortcut(_translate("MainWindow", "Backspace"))
        self.Export.setToolTip(_translate("MainWindow", "export as pdf"))
        self.Export.setShortcut(_translate("MainWindow", "E"))
        self.scroll_x.setToolTip(_translate("MainWindow", "scroll x"))
        self.scroll_y.setToolTip(_translate("MainWindow", "scroll y"))
        self.label_Channel2.setText(
            _translate("MainWindow", "Modified Signal"))
        self.label_Channel1.setText(
            _translate("MainWindow", "Original Signal"))
        self.r2.setShortcut(_translate("MainWindow", "2"))
        self.r1.setShortcut(_translate("MainWindow", "1"))
        self.label_Spectrogram_1.setText(
            _translate("MainWindow", "Original Spectrogram"))
        self.r4.setShortcut(_translate("MainWindow", "1"))
        self.label_Spectrogram_2.setText(
            _translate("MainWindow", "Modified Spectogram"))
        self.r3.setShortcut(_translate("MainWindow", "1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.Play_Signal_1.setText(_translate("MainWindow", "Play"))
        self.Pause_Signal_1.setText(_translate("MainWindow", "Pause"))
        self.Clear_Signal_1.setText(_translate("MainWindow", "Clear"))
        self.Play_Signal_2.setText(_translate("MainWindow", "Play"))
        self.Pause_Signal_2.setText(_translate("MainWindow", "Pause"))
        self.Clear_Signal_2.setText(_translate("MainWindow", "Clear"))
        self.Play_Signal_3.setText(_translate("MainWindow", "Play"))
        self.Pause_Signal_3.setText(_translate("MainWindow", "Pause"))
        self.Clear_Signal_3.setText(_translate("MainWindow", "Clear"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionOpen_3.setText(_translate("MainWindow", "Open"))
        self.OpenChannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.OpenChannel_1.setShortcut(_translate("MainWindow", "O, 1"))
        self.OpenChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.OpenChannel_2.setShortcut(_translate("MainWindow", "O, 2"))
        self.OpenChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.OpenChannel_3.setShortcut(_translate("MainWindow", "O, 3"))
        self.zoom_x_Signal_1.setText(_translate("MainWindow", "Signal 1"))
        self.zoom_x_Signal_2.setText(_translate("MainWindow", "Signal 2"))
        self.zoom_x_Signal_3.setText(_translate("MainWindow", "Signal 3"))
        self.zoom_y_Signal_1.setText(_translate("MainWindow", "Signal 1"))
        self.zoom_y_Signal_2.setText(_translate("MainWindow", "Signal 2"))
        self.zoom_y_Signal_3.setText(_translate("MainWindow", "Signal 3"))
        self.Export_Signal_1.setText(
            _translate("MainWindow", "Export Signal 1"))
        self.Export_Signal_2.setText(
            _translate("MainWindow", "Export Signal 2"))
        self.Export_Signal_3.setText(
            _translate("MainWindow", "Export Signal 3"))
        self.original_Spectrogram.setText(
            _translate("MainWindow", "Signal 1 Spectrogram"))
        self.original_Spectrogram.setShortcut(_translate("MainWindow", "G, 1"))
        self.Signal_2_Spectrogram.setText(
            _translate("MainWindow", "Signal 2 Spectrogram"))
        self.Signal_2_Spectrogram.setShortcut(_translate("MainWindow", "G, 2"))
        self.Signal_3_Spectrogram.setText(
            _translate("MainWindow", "Signal 3 Spectrogram"))
        self.Signal_3_Spectrogram.setShortcut(_translate("MainWindow", "G, 3"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_X.setText(_translate("MainWindow", "Zoom X"))
        self.actionZoom_Y.setText(_translate("MainWindow", "Zoom Y"))
        self.actionopen_file.setText(_translate("MainWindow", "open file"))
        self.actionnew_window.setText(_translate("MainWindow", "new window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())