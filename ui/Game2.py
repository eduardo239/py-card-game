import random
from card import CARD, NULL
from style import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 663)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 65))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_new_game = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_new_game.setMinimumSize(QtCore.QSize(0, 28))
        self.btn_new_game.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_new_game.setObjectName("btn_new_game")
        self.horizontalLayout_3.addWidget(self.btn_new_game)
        self.btn_stats = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_stats.setMinimumSize(QtCore.QSize(0, 28))
        self.btn_stats.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stats.setObjectName("btn_stats")
        self.horizontalLayout_3.addWidget(self.btn_stats)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_exit = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 28))
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout_3.addWidget(self.btn_exit)
        self.gridLayout_2.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 65))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_p1_score = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_p1_score.setFont(font)
        self.lbl_p1_score.setObjectName("lbl_p1_score")
        self.horizontalLayout.addWidget(self.lbl_p1_score)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbl_p2_score = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_p2_score.setFont(font)
        self.lbl_p2_score.setObjectName("lbl_p2_score")
        self.horizontalLayout.addWidget(self.lbl_p2_score)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_fight_status_p1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lbl_fight_status_p1.setFont(font)
        self.lbl_fight_status_p1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_fight_status_p1.setObjectName("lbl_fight_status_p1")
        self.verticalLayout.addWidget(self.lbl_fight_status_p1)
        self.lbl_fight_status_p2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setItalic(False)
        self.lbl_fight_status_p2.setFont(font)
        self.lbl_fight_status_p2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_fight_status_p2.setObjectName("lbl_fight_status_p2")
        self.verticalLayout.addWidget(self.lbl_fight_status_p2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 222))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lbl_p1_vantagem = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_p1_vantagem.setFont(font)
        self.lbl_p1_vantagem.setObjectName("lbl_p1_vantagem")
        self.horizontalLayout_4.addWidget(self.lbl_p1_vantagem)
        self.card_p1 = QtWidgets.QPushButton(self.groupBox_7)
        self.card_p1.setMaximumSize(QtCore.QSize(150, 200))
        self.card_p1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_p1.setStyleSheet("border: none;\n"
"")
        self.card_p1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/cards/bird-99.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_p1.setIcon(icon)
        self.card_p1.setIconSize(QtCore.QSize(150, 250))
        self.card_p1.setObjectName("card_p1")
        self.horizontalLayout_4.addWidget(self.card_p1)
        self.lbl_versus = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Light")
        font.setPointSize(28)
        self.lbl_versus.setFont(font)
        self.lbl_versus.setObjectName("lbl_versus")
        self.horizontalLayout_4.addWidget(self.lbl_versus)
        self.card_p2 = QtWidgets.QPushButton(self.groupBox_7)
        self.card_p2.setMaximumSize(QtCore.QSize(150, 200))
        self.card_p2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_p2.setStyleSheet("border: none;\n"
"")
        self.card_p2.setText("")
        self.card_p2.setIcon(icon)
        self.card_p2.setIconSize(QtCore.QSize(150, 250))
        self.card_p2.setObjectName("card_p2")
        self.horizontalLayout_4.addWidget(self.card_p2)
        self.lbl_p2_vantagem = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_p2_vantagem.setFont(font)
        self.lbl_p2_vantagem.setObjectName("lbl_p2_vantagem")
        self.horizontalLayout_4.addWidget(self.lbl_p2_vantagem)
        spacerItem4 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.card_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.card_4.setMaximumSize(QtCore.QSize(150, 200))
        self.card_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_4.setStyleSheet("border: none;\n"
"")
        self.card_4.setText("")
        self.card_4.setIcon(icon)
        self.card_4.setIconSize(QtCore.QSize(150, 250))
        self.card_4.setObjectName("card_4")
        self.gridLayout.addWidget(self.card_4, 0, 4, 1, 1)
        self.card_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.card_2.setMaximumSize(QtCore.QSize(150, 200))
        self.card_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_2.setStyleSheet("border: none;\n"
"")
        self.card_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/cards/water_01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_2.setIcon(icon1)
        self.card_2.setIconSize(QtCore.QSize(150, 250))
        self.card_2.setObjectName("card_2")
        self.gridLayout.addWidget(self.card_2, 0, 2, 1, 1)
        self.card_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.card_5.setMaximumSize(QtCore.QSize(150, 200))
        self.card_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_5.setStyleSheet("border: none;\n"
"")
        self.card_5.setText("")
        self.card_5.setIcon(icon)
        self.card_5.setIconSize(QtCore.QSize(150, 250))
        self.card_5.setObjectName("card_5")
        self.gridLayout.addWidget(self.card_5, 0, 5, 1, 1)
        self.card_1 = QtWidgets.QPushButton(self.groupBox_4)
        self.card_1.setMaximumSize(QtCore.QSize(150, 200))
        self.card_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_1.setStyleSheet("border: none;\n"
"")
        self.card_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/cards/natu_01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_1.setIcon(icon2)
        self.card_1.setIconSize(QtCore.QSize(150, 250))
        self.card_1.setObjectName("card_1")
        self.gridLayout.addWidget(self.card_1, 0, 1, 1, 1)
        self.card_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.card_3.setMaximumSize(QtCore.QSize(150, 200))
        self.card_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_3.setStyleSheet("border: none;\n"
"")
        self.card_3.setText("")
        self.card_3.setIcon(icon)
        self.card_3.setIconSize(QtCore.QSize(150, 250))
        self.card_3.setObjectName("card_3")
        self.gridLayout.addWidget(self.card_3, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 6, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Players = QtWidgets.QMenu(self.menubar)
        self.menu_Players.setObjectName("menu_Players")
        self.menu_Stats = QtWidgets.QMenu(self.menubar)
        self.menu_Stats.setObjectName("menu_Stats")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Names = QtWidgets.QAction(MainWindow)
        self.action_Names.setObjectName("action_Names")
        self.action_Rank = QtWidgets.QAction(MainWindow)
        self.action_Rank.setObjectName("action_Rank")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_Exit)
        self.menu_Players.addAction(self.action_Names)
        self.menu_Stats.addAction(self.action_Rank)
        self.menu_About.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Players.menuAction())
        self.menubar.addAction(self.menu_Stats.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        """style"""
        self.lbl_p1_vantagem.setStyleSheet(lbl_vantagem)
        self.lbl_p2_vantagem.setStyleSheet(lbl_vantagem)

        """init"""
        self.start()

        """buttons"""
        self.btn_new_game.clicked.connect(self.start)
        self.btn_exit.clicked.connect(lambda: MainWindow.close())

        self.card_p1.clicked.connect(self.remove)

        self.card_1.clicked.connect(lambda: self.pick(self.deck_p1[0]))
        self.card_2.clicked.connect(lambda: self.pick(self.deck_p1[1]))
        self.card_3.clicked.connect(lambda: self.pick(self.deck_p1[2]))
        self.card_4.clicked.connect(lambda: self.pick(self.deck_p1[3]))
        self.card_5.clicked.connect(lambda: self.pick(self.deck_p1[4]))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_new_game.setText(_translate("MainWindow", "New Game"))
        self.btn_stats.setText(_translate("MainWindow", "Stats"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.lbl_p1_score.setText(_translate("MainWindow", "Player 1:###"))
        self.lbl_p2_score.setText(_translate("MainWindow", "Player 2: ###"))
        self.lbl_fight_status_p1.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_fight_status_p2.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_p1_vantagem.setText(_translate("MainWindow", "vantagem"))
        self.lbl_versus.setText(_translate("MainWindow", "VERSUS"))
        self.lbl_p2_vantagem.setText(_translate("MainWindow", "vantagem"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Players.setTitle(_translate("MainWindow", "&Players"))
        self.menu_Stats.setTitle(_translate("MainWindow", "&Stats"))
        self.menu_About.setTitle(_translate("MainWindow", "&Help"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Names.setText(_translate("MainWindow", "&Names"))
        self.action_Rank.setText(_translate("MainWindow", "&Rank"))
        self.action_About.setText(_translate("MainWindow", "&About"))

    """start"""

    def start(self):
        self.del_deck()
        self.deck_p1 = self.get_deck()
        self.deck_p2 = self.get_deck()

        # self.get_deck()
        self.set_deck(self.deck_p2)
        self.set_deck(self.deck_p1)

    """generate deck"""

    def get_deck(self):
        a = []
        for i in range(1, 6):
            d = random.choice(CARD)
            a.append(d)
        return a

    """set cards on game"""

    def set_deck(self, deck):
        i = QtGui.QIcon()
        i.addPixmap(QtGui.QPixmap(NULL[0]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_p1.setIcon(i)

        i2 = QtGui.QIcon()
        i2.addPixmap(QtGui.QPixmap(NULL[0]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_p2.setIcon(i2)

        # player 1

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(deck[0]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_1.setIcon(icon1)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(deck[1]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_2.setIcon(icon2)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(deck[2]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_3.setIcon(icon3)

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(deck[3]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_4.setIcon(icon4)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(deck[4]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_5.setIcon(icon5)

    """pick the card"""

    def pick(self, card):

        print(card)

        p1_atk = card['attack']
        p1_def = card['defense']
        p1_elm = card['element']

        self.lbl_fight_status_p1.setText(
            f'''attack: {p1_atk} + defense: {p1_def} + element: {p1_elm}'''
        )

        i = QtGui.QIcon()
        i.addPixmap(QtGui.QPixmap(card['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_p1.setIcon(i)

        self.lbl_p1_vantagem.setText(card['element'])

    def del_deck(self):
        self.deck_p1 = []
        self.deck_p2 = []

    def remove(self):
        i = QtGui.QIcon()
        i.addPixmap(QtGui.QPixmap(NULL[0]['image']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_p1.setIcon(i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())