import random
import glob

from PyQt5 import QtCore, QtGui, QtWidgets
from cards import *
from style import *
from termcolor import cprint

from ui import Options

print_error = lambda x: cprint(x, 'red', attrs=['bold'])
print_grey_on_yellow2 = lambda x: cprint(x, 'grey', 'on_yellow', end=' ')
print_grey_on_yellow = lambda x: cprint(x, 'grey', 'on_yellow')
print_yellow_on_grey2 = lambda x: cprint(x, 'yellow', 'on_grey', end=' ')
print_yellow_on_grey = lambda x: cprint(x, 'yellow', 'on_grey')
print_cyan = lambda x: cprint(x, 'cyan', attrs=['bold'])
print_warning2 = lambda x: cprint(x, 'yellow', end=' ')
print_warning = lambda x: cprint(x, 'yellow')
print_info2 = lambda x: cprint(x, 'blue', end=' ')
print_info = lambda x: cprint(x, 'blue')
print_green2 = lambda x: cprint(x, 'green', end=' ')
print_green = lambda x: cprint(x, 'green')
print_win = lambda x: cprint(x, 'yellow')


class Ui_MainWindow(object):
    def __init__(self):
        self.dck_p1_old__ = []
        self.dck_p2_old__ = []

        self.p1_number_card = {}
        self.p2_number_card = {}

        self.my_attack = 'Attack:'
        self.my_defense = 'Defense:'
        self.my_element = 'Element:'

        self.en_attack = ''
        self.en_defense = ''
        self.en_element = ''

        self.total_p1__ = 0
        self.total_p2__ = 0

        self.p1_score = 0
        self.p2_score = 0

        self.played_cards = 5

        # cards from folder
        self.all_cards = []

        self.deck_p1_list = []
        self.deck_p2_list = []

        self.p1_deck = {}
        self.p2_deck = {}

        self.p1_picked_card = {}
        self.p2_picked_card = {}

        self.p1_total = 0
        self.p2_total = 0

        self.p1_random_cards = []
        self.p2_random_cards = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.inp_score_p1 = QtWidgets.QLineEdit(self.groupBox)
        self.inp_score_p1.setObjectName("inp_score_p1")
        self.verticalLayout_2.addWidget(self.inp_score_p1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.inp_score_p2 = QtWidgets.QLineEdit(self.groupBox)
        self.inp_score_p2.setObjectName("inp_score_p2")
        self.verticalLayout_2.addWidget(self.inp_score_p2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.inp_name_p1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_name_p1.setObjectName("inp_name_p1")
        self.verticalLayout_3.addWidget(self.inp_name_p1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.inp_name_p2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.inp_name_p2.setObjectName("inp_name_p2")
        self.verticalLayout_3.addWidget(self.inp_name_p2)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_new_game = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_new_game.setObjectName("btn_new_game")
        self.verticalLayout_5.addWidget(self.btn_new_game)
        self.btn_options = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_options.setObjectName("btn_options")
        self.verticalLayout_5.addWidget(self.btn_options)
        self.btn_exit = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_5.addWidget(self.btn_exit)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.img_enemy_cards = QtWidgets.QLabel(self.frame_2)
        self.img_enemy_cards.setText("")
        self.img_enemy_cards.setPixmap(QtGui.QPixmap("./assets/enemy_card5.png"))
        self.img_enemy_cards.setAlignment(QtCore.Qt.AlignCenter)
        self.img_enemy_cards.setObjectName("img_enemy_cards")
        self.verticalLayout_4.addWidget(self.img_enemy_cards)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lbl_op_attack = QtWidgets.QPushButton(self.groupBox_4)
        self.lbl_op_attack.setObjectName("lbl_enemy_attack")
        self.horizontalLayout_3.addWidget(self.lbl_op_attack)
        self.lbl_en_defense = QtWidgets.QPushButton(self.groupBox_4)
        self.lbl_en_defense.setObjectName("lbl_enemy_defense")
        self.horizontalLayout_3.addWidget(self.lbl_en_defense)
        self.lbl_en_element = QtWidgets.QPushButton(self.groupBox_4)
        self.lbl_en_element.setObjectName("lbl_enemy_element")
        self.horizontalLayout_3.addWidget(self.lbl_en_element)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./assets/rect.png"))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lbl_score = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lbl_score.setFont(font)
        self.lbl_score.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_score.setObjectName("lbl_score")
        self.horizontalLayout_2.addWidget(self.lbl_score)
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("./assets/rect.png"))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.lbl_my_attack = QtWidgets.QPushButton(self.groupBox_5)
        self.lbl_my_attack.setObjectName("lbl_my_attack")
        self.horizontalLayout_4.addWidget(self.lbl_my_attack)

        self.lbl_my_defense = QtWidgets.QPushButton(self.groupBox_5)
        self.lbl_my_defense.setObjectName("lbl_my_defense")
        self.horizontalLayout_4.addWidget(self.lbl_my_defense)

        self.lbl_my_element = QtWidgets.QPushButton(self.groupBox_5)
        self.lbl_my_element.setObjectName("lbl_my_element")
        self.horizontalLayout_4.addWidget(self.lbl_my_element)

        self.lbl_my_result = QtWidgets.QPushButton(self.groupBox_5)
        self.lbl_my_result.setObjectName("lbl_my_result")
        self.horizontalLayout_4.addWidget(self.lbl_my_result)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.card_1 = QtWidgets.QPushButton(self.groupBox_7)
        self.card_1.setStyleSheet("border: 0;")
        self.card_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_1.setIcon(icon)
        self.card_1.setIconSize(QtCore.QSize(120, 160))
        self.card_1.setObjectName("card_1")
        self.horizontalLayout_5.addWidget(self.card_1)
        self.card_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.card_2.setStyleSheet("border: 0;")
        self.card_2.setText("")
        self.card_2.setIcon(icon)
        self.card_2.setIconSize(QtCore.QSize(120, 160))
        self.card_2.setObjectName("card_2")
        self.horizontalLayout_5.addWidget(self.card_2)
        self.card_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.card_3.setStyleSheet("border: 0;")
        self.card_3.setText("")
        self.card_3.setIcon(icon)
        self.card_3.setIconSize(QtCore.QSize(120, 160))
        self.card_3.setObjectName("card_3")
        self.horizontalLayout_5.addWidget(self.card_3)
        self.card_4 = QtWidgets.QPushButton(self.groupBox_7)
        self.card_4.setStyleSheet("border: 0;")
        self.card_4.setText("")
        self.card_4.setIcon(icon)
        self.card_4.setIconSize(QtCore.QSize(120, 160))
        self.card_4.setObjectName("card_4")
        self.horizontalLayout_5.addWidget(self.card_4)
        self.card_5 = QtWidgets.QPushButton(self.groupBox_7)
        self.card_5.setStyleSheet("border: 0;")
        self.card_5.setText("")
        self.card_5.setIcon(icon)
        self.card_5.setIconSize(QtCore.QSize(120, 160))
        self.card_5.setObjectName("card_5")
        self.horizontalLayout_5.addWidget(self.card_5)
        self.verticalLayout_4.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(265, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.groupBox_8)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New_Game = QtWidgets.QAction(MainWindow)
        self.action_New_Game.setObjectName("action_New_Game")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_File.addAction(self.action_New_Game)
        self.menu_File.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.label_2.setBuddy(self.inp_score_p1)
        self.label_3.setBuddy(self.inp_score_p2)
        self.label_6.setBuddy(self.inp_name_p1)
        self.label_5.setBuddy(self.inp_name_p2)

        """ style """
        MainWindow.setStyleSheet(main_window)

        self.img_enemy_cards.setStyleSheet(img_cards)

        self.pushButton.setStyleSheet(btn_secondary_big)

        self.lbl_score.setStyleSheet(lbl_big)

        self.inp_score_p1.setStyleSheet(inp_disabled)
        self.inp_score_p2.setStyleSheet(inp_disabled)

        self.inp_name_p1.setStyleSheet(inp_enable)
        self.inp_name_p2.setStyleSheet(inp_enable)

        self.lbl_op_attack.setStyleSheet(lbl_pink + min_width)
        self.lbl_en_defense.setStyleSheet(lbl_pink + min_width)
        self.lbl_en_element.setStyleSheet(lbl_pink + min_width)

        self.lbl_my_attack.setStyleSheet(lbl_pink + min_width)
        self.lbl_my_defense.setStyleSheet(lbl_pink + min_width)
        self.lbl_my_element.setStyleSheet(lbl_pink + min_width)
        self.lbl_my_result.setStyleSheet(lbl_pink + min_width)

        self.btn_new_game.setStyleSheet(btn_secondary)
        self.btn_options.setStyleSheet(btn_secondary)
        self.btn_exit.setStyleSheet(btn_secondary)

        self.groupBox_4.setStyleSheet(group_box)
        self.groupBox_5.setStyleSheet(group_box)
        self.groupBox_6.setStyleSheet(group_box)
        self.groupBox_7.setStyleSheet(group_box)
        self.groupBox_8.setStyleSheet(group_box)

        """ menu """
        self.btn_new_game.clicked.connect(self.new_game)
        self.action_New_Game.triggered.connect(self.new_game)
        self.btn_options.clicked.connect(self.w_options)
        self.btn_exit.clicked.connect(lambda: MainWindow.close())

        """ begin """
        # set players names
        self.inp_name_p1.setText('Joana')
        self.inp_name_p2.setText('Gill')
        self.generate_deck()

        """ buttons """
        self.card_1.clicked.connect(lambda: self.pick(1))
        self.card_2.clicked.connect(lambda: self.pick(2))
        self.card_3.clicked.connect(lambda: self.pick(3))
        self.card_4.clicked.connect(lambda: self.pick(4))
        self.card_5.clicked.connect(lambda: self.pick(5))

        """ inputs, labels default """
        self.inp_score_p1.setReadOnly(True)
        self.inp_score_p2.setReadOnly(True)
        self.inp_score_p1.setText('0')
        self.inp_score_p2.setText('0')
        self.lbl_score.setText('0 x 0')

        """ call match method """
        self.pushButton.clicked.connect(self.match)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inp_score_p1, self.inp_score_p2)
        MainWindow.setTabOrder(self.inp_score_p2, self.inp_name_p1)
        MainWindow.setTabOrder(self.inp_name_p1, self.inp_name_p2)
        MainWindow.setTabOrder(self.inp_name_p2, self.btn_new_game)
        MainWindow.setTabOrder(self.btn_new_game, self.btn_options)
        MainWindow.setTabOrder(self.btn_options, self.btn_exit)
        MainWindow.setTabOrder(self.btn_exit, self.lbl_op_attack)
        MainWindow.setTabOrder(self.lbl_op_attack, self.lbl_en_defense)
        MainWindow.setTabOrder(self.lbl_en_defense, self.lbl_en_element)
        MainWindow.setTabOrder(self.lbl_en_element, self.lbl_my_attack)
        MainWindow.setTabOrder(self.lbl_my_attack, self.lbl_my_defense)
        MainWindow.setTabOrder(self.lbl_my_defense, self.lbl_my_element)
        MainWindow.setTabOrder(self.lbl_my_element, self.card_1)
        MainWindow.setTabOrder(self.card_1, self.card_2)
        MainWindow.setTabOrder(self.card_2, self.card_3)
        MainWindow.setTabOrder(self.card_3, self.card_4)
        MainWindow.setTabOrder(self.card_4, self.card_5)
        MainWindow.setTabOrder(self.card_5, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Score"))
        self.label_2.setText(_translate("MainWindow", self.inp_name_p1.text()))
        self.label_3.setText(_translate("MainWindow", self.inp_name_p2.text()))
        self.groupBox_2.setTitle(_translate("MainWindow", "Players"))
        self.label_4.setText(_translate("MainWindow", "Players Name"))
        self.label_6.setText(_translate("MainWindow", "Player 1"))
        self.label_5.setText(_translate("MainWindow", "Player 2"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Menu"))
        self.btn_new_game.setText(_translate("MainWindow", "New Game"))
        self.btn_options.setText(_translate("MainWindow", "Options"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.lbl_op_attack.setText(_translate("MainWindow", "Attack: ???"))
        self.lbl_en_defense.setText(_translate("MainWindow", "Defense: ???"))
        self.lbl_en_element.setText(_translate("MainWindow", "Element: ???"))
        self.lbl_score.setText(_translate("MainWindow", "0 x 0"))
        self.lbl_my_attack.setText(_translate("MainWindow", self.my_attack))
        self.lbl_my_defense.setText(_translate("MainWindow", self.my_defense))
        self.lbl_my_element.setText(_translate("MainWindow", self.my_element))
        self.lbl_my_result.setText(_translate("MainWindow", f'Result: {str(self.p1_total)}'))
        self.pushButton.setText(_translate("MainWindow", "PLAY"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.action_New_Game.setText(_translate("MainWindow", "&New Game"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))

    def new_game(self):
        self.reset()
        self.generate_deck()

    # def set_pick(self, p1):
    #     a = p1['attack']
    #     d = p1['defense']
    #     e = p1['element']
    #     self.lbl_my_attack.setText(a)
    #     self.lbl_my_defense.setText(d)
    #     self.lbl_my_element.setText(e)

    def pick(self, pick):
        if self.p1_score == 3 or self.p2_score == 3:
            self.reset()

        self.lbl_op_attack.setText("Attack:")
        self.lbl_en_defense.setText("Defense:")
        self.lbl_en_element.setText("Element:")

        # self.p1_number_card = self.dck_p1_old__[pick - 1]
        # self.p2_number_card = self.dck_p2_old__[pick - 1]

        # p1_atk = self.card_p1['attack']
        # p1_def = self.card_p1['defense']
        # p1_elm = self.card_p1['element']
        #
        # p2_atk = self.card_p2['attack']
        # p2_def = self.card_p2['defense']
        # p2_elm = self.card_p2['element']

        # self.my_attack = p1_atk
        # self.my_defense = p1_def
        # self.my_element = p1_elm
        #
        # self.en_attack = p2_atk
        # self.en_defense = p2_def
        # self.en_element = p2_elm

        # self.lbl_my_attack.setText(str(f'Attack: {self.my_attack}'))
        # self.lbl_my_defense.setText(str(f'Defense: {self.my_defense}'))
        # self.lbl_my_element.setText(str(f'Element: {self.my_element}'))

        # self.total_p1 = int(p1_atk) - int(p2_def)
        # self.total_p2 = int(p2_atk) - int(p1_def)

        # self.lbl_my_result.setText(str(f'Result: {self.total_p1}'))

        # new with images p1
        self.lbl_my_attack.setText(str(f'Attack: {self.p1_deck[f"card{pick}"]["attack"]}'))
        self.lbl_my_defense.setText(str(f'Defense: {self.p1_deck[f"card{pick}"]["defense"]}'))
        self.lbl_my_element.setText(str(f'Element: {self.p1_deck[f"card{pick}"]["element"]}'))

        # sum of stats p1
        self.p1_picked_card = self.p1_deck[f"card{pick}"]
        p1_atk = int(self.p1_picked_card['attack'])
        p1_def = int(self.p1_picked_card['defense'])
        p1_elm = self.p1_picked_card['element']
        '''todo:::element'''
        total_stats_p1 = p1_atk + p1_def
        self.p1_total = total_stats_p1
        self.lbl_my_result.setText(str(f'Result: {total_stats_p1}'))

        # sum of stats p2 fake pick
        self.p2_picked_card = self.p2_deck[f'card{pick}']
        p2_atk = int(self.p2_picked_card['attack'])
        p2_def = int(self.p2_picked_card['defense'])
        p2_elm = self.p2_picked_card['element']
        total_stats_p2 = p2_atk + p2_def
        self.p2_total = total_stats_p2

    def generate_deck(self):
        # from old app ///
        # remover ///
        # self.dck_p1_old__ = random.sample(CARD, 5)
        # self.dck_p2_old__ = random.sample(CARD, 5)

        # new APP

        # get all images from folder
        self.get_all_images()

        # 5 random cards for players
        self.p1_random_cards = random.sample(self.all_cards, 5)
        self.p2_random_cards = random.sample(self.all_cards, 5)

        # generate list for each card with stats and pathname
        for i in range(len(self.p1_random_cards)):
            self.deck_p1_list.append(self.p1_random_cards[i])
            self.deck_p1_list.append(self.p1_random_cards[i].split('_'))

        for k in range(len(self.p2_random_cards)):
            self.deck_p2_list.append(self.p2_random_cards[k])
            self.deck_p2_list.append(self.p2_random_cards[k].split('_'))

        self.convert_filename_to_dict(self.deck_p1_list, self.deck_p2_list)

    def match(self):
        # reset score style
        self.lbl_score.setStyleSheet(lbl_big)

        # if user click on the play button before pick one card
        self.lbl_score.setText('')
        if not bool(self.p1_picked_card):
            return self.lbl_score.setText('Pick one card.')

        # subtract card from enemy deck
        self.played_cards -= 1
        i = self.played_cards
        self.img_enemy_cards.setPixmap(QtGui.QPixmap(f"./assets/enemy_card{i}.png"))

        # get score from players
        a = self.p1_total
        b = self.p2_total

        # set score in the labels
        # self.lbl_enemy_attack.setText(str(f'Attack: {self.en_attack}'))
        # self.lbl_enemy_defense.setText(str(f'Defense: {self.en_defense}'))
        # self.lbl_enemy_element.setText(str(f'Element: {self.en_element}'))

        # __set enemy stats
        self.lbl_op_attack.setText(str(f'Attack: {self.p2_picked_card["attack"]}'))
        self.lbl_en_defense.setText(str(f'Defense: {self.p2_picked_card["defense"]}'))
        self.lbl_en_element.setText(str(f'Element: {self.p2_picked_card ["element"]}'))

        # set + 1 for the winners
        if a > b:
            self.p1_score += 1
            self.lbl_score.setText(f'{a} x {b}')
            self.winner()
        elif b > a:
            self.p2_score += 1
            self.lbl_score.setText(f'{a} x {b}')
            self.winner()
        else:
            self.p1_score += 1
            self.p2_score += 1
            self.lbl_score.setText(f'{a} x {b}')
            self.winner()

        # update scoreboard
        self.inp_score_p1.setText(str(self.p1_score))
        self.inp_score_p2.setText(str(self.p2_score))

    def winner(self):
        if self.p1_score == 3 and self.p2_score == 3:
            self.lbl_score.setStyleSheet(lbl_big_winner)
            self.lbl_score.setText(f'Draw')
        elif self.p2_score == 3:
            self.lbl_score.setStyleSheet(lbl_big_winner)
            self.lbl_score.setText(f'{self.inp_name_p2.text()} won')
        elif self.p1_score == 3:
            self.lbl_score.setStyleSheet(lbl_big_winner)
            self.lbl_score.setText(f'{self.inp_name_p1.text()} won')
        else:
            pass

    def get_all_images(self):
        self.all_cards = glob.glob('./assets/cards/*.png')

    def set_cards_on_deck(self):
        # update card image on deck
        i1 = QtGui.QIcon()
        i1.addPixmap(QtGui.QPixmap(self.p1_deck[f'card1']['filename']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_1.setIcon(i1)

        i2 = QtGui.QIcon()
        i2.addPixmap(QtGui.QPixmap(self.p1_deck[f'card2']['filename']), QtGui.QIcon.Normal,
                     QtGui.QIcon.Off)
        self.card_2.setIcon(i2)

        i3 = QtGui.QIcon()
        i3.addPixmap(QtGui.QPixmap(self.p1_deck[f'card3']['filename']), QtGui.QIcon.Normal,
                     QtGui.QIcon.Off)
        self.card_3.setIcon(i3)

        i4 = QtGui.QIcon()
        i4.addPixmap(QtGui.QPixmap(self.p1_deck[f'card4']['filename']), QtGui.QIcon.Normal,
                     QtGui.QIcon.Off)
        self.card_4.setIcon(i4)

        i5 = QtGui.QIcon()
        i5.addPixmap(QtGui.QPixmap(self.p1_deck[f'card5']['filename']), QtGui.QIcon.Normal,
                     QtGui.QIcon.Off)
        self.card_5.setIcon(i5)

    def convert_filename_to_dict(self, p1_cards, p2_cards):
        dict_deck_p1 = {
            'card1': {
                'attack': p1_cards[1][1],
                'defense': p1_cards[1][2],
                'element': p1_cards[1][3].split('.')[0],
                'filename': p1_cards[0]
            },
            'card2': {
                'attack': p1_cards[3][1],
                'defense': p1_cards[3][2],
                'element': p1_cards[3][3].split('.')[0],
                'filename': p1_cards[2]
            },
            'card3': {
                'attack': p2_cards[5][1],
                'defense': p1_cards[5][2],
                'element': p1_cards[5][3].split('.')[0],
                'filename': p1_cards[4]
            },
            'card4': {
                'attack': p1_cards[7][1],
                'defense': p1_cards[7][2],
                'element': p1_cards[7][3].split('.')[0],
                'filename': p1_cards[6]
            },
            'card5': {
                'attack': p1_cards[9][1],
                'defense': p1_cards[9][2],
                'element': p1_cards[9][3].split('.')[0],
                'filename': p1_cards[8]
            },
        }
        self.p1_deck = dict_deck_p1
        #
        dict_deck_p2 = {
            'card1': {
                'attack': p2_cards[1][1],
                'defense': p2_cards[1][2],
                'element': p2_cards[1][3].split('.')[0],
                'filename': p2_cards[0]
            },
            'card2': {
                'attack': p2_cards[3][1],
                'defense': p2_cards[3][2],
                'element': p2_cards[3][3].split('.')[0],
                'filename': p2_cards[2]
            },
            'card3': {
                'attack': p2_cards[5][1],
                'defense': p2_cards[5][2],
                'element': p2_cards[5][3].split('.')[0],
                'filename': p2_cards[4]
            },
            'card4': {
                'attack': p2_cards[7][1],
                'defense': p2_cards[7][2],
                'element': p2_cards[7][3].split('.')[0],
                'filename': p2_cards[6]
            },
            'card5': {
                'attack': p2_cards[9][1],
                'defense': p2_cards[9][2],
                'element': p2_cards[9][3].split('.')[0],
                'filename': p2_cards[8]
            },
        }
        self.p2_deck = dict_deck_p2
        self.set_cards_on_deck()

    def reset(self):
        self.p1_score = 0
        self.p2_score = 0
        self.inp_score_p1.setText('0')
        self.inp_score_p2.setText('0')
        self.lbl_score.setText('0 x 0')

        self.played_cards = 5
        self.img_enemy_cards.setPixmap(QtGui.QPixmap(f"./assets/enemy_card5.png"))

    def w_options(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Options.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
