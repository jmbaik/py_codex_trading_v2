import sys

from PyQt5.QtWidgets import QApplication

from api.Kiwoom import *
from strategy.RSIStrategy import RSIStrategy

app = QApplication(sys.argv)

rsi_strategy = RSIStrategy()
rsi_strategy.start()


app.exec_()
