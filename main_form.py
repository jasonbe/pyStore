#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Alsu'

from PyQt4 import QtGui, uic, QtCore
from pymongo import MongoClient, ASCENDING, DESCENDING


class MainForm(QtGui.QMainWindow):
    def __init__(self):
        self._client = MongoClient()
        self._db = self._client.store_base
        self._motherboards = self._db.motherboard
        QtGui.QWidget.__init__(self)
        uic.loadUi('mainwindow.ui', self)
        self._load_min_max()
        self.connect(self.btnCount, QtCore.SIGNAL("clicked()"), self._count_all)

    def _load_min_max(self):
        minimum = self._motherboards.find().sort([("price", ASCENDING)]).limit(1)[0]['price']
        maximum = self._motherboards.find().sort([("price", DESCENDING)]).limit(1)[0]['price']
        self.ledtMinPrice.setText(str(minimum))
        self.ledtMaxPrice.setText(str(maximum))

    def _count_all(self):
        motherboards = self._mothercount()
        self.textBrowser.setText(str(motherboards))

    def _mothercount(self):
        producer = self.cmbxProducer.currentText()
        formfactor = self.cmbxFormFactor.currentText()
        proc = 'Intel' if self.rbtnIntelMB.isChecked() else 'AMD'

        answer = self._motherboards.find({"producer": "ASRock"})
        count = 0
        for i in answer:
            count += i['price']
        print(count)
        return count

    def _proccount(self):
        pass

    def _ramcount(self):
        pass


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.showMaximized()
    sys.exit(app.exec_())
