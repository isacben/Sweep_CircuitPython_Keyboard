import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner


# GPIO to key mapping - each line is a new row.
_KEY_CFG = [
    board.D7, board.A0, board.A1, board.A2, board.A3,
    board.SCK, board.MISO, board.MOSI, board.D10, board.TX,
    board.D2, board.D3, board.D4, board.D5, board.D6,
    board.D8, board.D9,
]

# Keyboard implementation class
class KMKKeyboard(_KMKKeyboard):
    data_pin=board.RX
    coord_mapping = [
     0,  1,  2,  3,  4,  21, 20, 19, 18, 17,
     5,  6,  7,  8,  9,  26, 25, 24, 23, 22,
    10, 11, 12, 13, 14,  31, 30, 29, 28, 27,
                15, 16,  33, 32,
    ]

    def __init__(self):
        self.matrix = KeysScanner(_KEY_CFG)
