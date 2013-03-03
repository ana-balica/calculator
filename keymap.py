from PySide import QtCore


class KeyMap():
    escape = QtCore.Qt.Key.Key_Escape
    back = QtCore.Qt.Key.Key_Backspace
    enter = QtCore.Qt.Key.Key_Return

    keymap = {
        QtCore.Qt.Key.Key_0: '0',
        QtCore.Qt.Key.Key_1: '1',
        QtCore.Qt.Key.Key_2: '2',
        QtCore.Qt.Key.Key_3: '3',
        QtCore.Qt.Key.Key_4: '4',
        QtCore.Qt.Key.Key_5: '5',
        QtCore.Qt.Key.Key_6: '6',
        QtCore.Qt.Key.Key_7: '7',
        QtCore.Qt.Key.Key_8: '8',
        QtCore.Qt.Key.Key_9: '9',
        QtCore.Qt.Key.Key_Space: ' ',
        QtCore.Qt.Key.Key_Equal: '=',
        QtCore.Qt.Key.Key_Plus: '+',
        QtCore.Qt.Key.Key_Minus: '-',
        QtCore.Qt.Key.Key_Asterisk: '*',
        QtCore.Qt.Key.Key_Slash: '/',
        QtCore.Qt.Key.Key_Period: '.',
        QtCore.Qt.Key.Key_Comma: '.',
        QtCore.Qt.Key.Key_ParenLeft: '(',
        QtCore.Qt.Key.Key_ParenRight: ')'
    }
