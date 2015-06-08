#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Alsu'

import sys
from main_form import MainForm
from PyQt4.QtGui import QApplication

def main():
    pass
    app = QApplication(sys.argv)
    main_window = MainForm()
    main_window.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print("Keyboard interrupt")
