# -*- coding: utf-8 -*-

import sys
import re
from math import sqrt

from PySide import QtGui

from calculator_gui import Ui_calculator
from mathsymbol import MathSymbol
from keymap import KeyMap


class ControlMainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_calculator()
        self.ui.setupUi(self)
        self.bind_buttons()

        self.expression = ''

    def keyPressEvent(self, event):
        key = event.key()
        text = ''
        if key == KeyMap.escape:
            self.reset()
        elif key == KeyMap.back:
            text = 'CE'
        elif key == KeyMap.enter:
            text = '='
        elif key in KeyMap.keymap:
            text = KeyMap.keymap[key]
        self.execute_task(text)

    def button_clicked(self):
        sender = self.sender()
        text = sender.text()
        self.execute_task(text)

    def execute_task(self, text):
        symbol = MathSymbol(text)

        if (self.expression and self.expression[-1] == '='):
            self.reset()

        if symbol.is_digit() or symbol.is_simple_operation():
            self.expression += text
        elif symbol.is_ce():
            self.expression = self.expression[:-1]
        elif symbol.is_equal():
            result = self.compute_expression()
            self.show_in_label(result)
            self.expression += '='
        elif symbol.is_sign():
            self.change_sign()
        elif symbol.is_square_root():
            result = self.compute_expression()
            result = unicode(sqrt(float(result)))
            self.show_in_label(result)
            self.expression = u'√(' + self.expression + ')='
        else:
            self.expression += text

        self.show_in_line_edit()

    def reset(self):
        self.expression = ''
        self.ui.label.setText('')
        self.ui.lineEdit.setText('')

    def compute_expression(self):
        expression = self.replace_symbols()
        try:
            result = unicode(eval(expression))
        except:
            result = '#error'
        return result

    def show_in_label(self, text):
        self.ui.label.setText(text)

    def show_in_line_edit(self):
        self.ui.lineEdit.setText(self.expression)

    def change_sign(self):
        symbols = re.findall(r'[^\d]', self.expression)
        symbols_length = len(symbols)
        if (self.expression and self.expression[:2] == '-('
            and self.expression[-1] == ')'):
            self.expression = self.expression[2:-1]
        elif self.expression.startswith('-'):
            if symbols_length == 1:
                self.expression = self.expression[1:]
            elif symbols_length > 1:
                self.expression = '-(' + self.expression + ')'
        else:
            if symbols_length == 0:
                self.expression = '-' + self.expression
            elif symbols_length > 0:
                self.expression = '-(' + self.expression + ')'

    def bind_buttons(self):
        self.ui.button_0.clicked.connect(self.button_clicked)
        self.ui.button_1.clicked.connect(self.button_clicked)
        self.ui.button_2.clicked.connect(self.button_clicked)
        self.ui.button_3.clicked.connect(self.button_clicked)
        self.ui.button_4.clicked.connect(self.button_clicked)
        self.ui.button_5.clicked.connect(self.button_clicked)
        self.ui.button_6.clicked.connect(self.button_clicked)
        self.ui.button_7.clicked.connect(self.button_clicked)
        self.ui.button_8.clicked.connect(self.button_clicked)
        self.ui.button_9.clicked.connect(self.button_clicked)
        self.ui.button_ce.clicked.connect(self.button_clicked)
        self.ui.button_divide.clicked.connect(self.button_clicked)
        self.ui.button_dot.clicked.connect(self.button_clicked)
        self.ui.button_equal.clicked.connect(self.button_clicked)
        self.ui.button_minus.clicked.connect(self.button_clicked)
        self.ui.button_multiply.clicked.connect(self.button_clicked)
        self.ui.button_plus.clicked.connect(self.button_clicked)
        self.ui.button_power.clicked.connect(self.button_clicked)
        self.ui.button_sign.clicked.connect(self.button_clicked)
        self.ui.button_sqrt.clicked.connect(self.button_clicked)

    def replace_symbols(self):
        replacements = {u'÷': u'/', u'×': u'*', u'^': u'**'}
        expression = self.expression
        for i, j in replacements.iteritems():
            expression = expression.replace(i, j)

        return expression


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    calculator = ControlMainWindow()
    calculator.show()
    sys.exit(app.exec_())
