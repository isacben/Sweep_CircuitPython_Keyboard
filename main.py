from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

split = Split(
    split_type=SplitType.UART,
    split_side=SplitSide.LEFT,
    split_target_left=True,
    target_left=True, use_pio=True
    )

layers = Layers()

keyboard.modules = [layers, split]

_______ = KC.TRNS
XXXXXXX = KC.NO
SAPP = KC.LCMD(KC.TAB)                    # Switch application
NTAB = KC.LCTL(KC.TAB)                    # Browser next tab
PTAB = KC.LCTL(KC.LSFT(KC.TAB))           # Browser previous tab

SEARCH = KC.LCMD(KC.F)                    # Control + F
SPOTL = KC.LCMD(KC.SPC)                   # Spotlight search
CTL_K = KC.LCMD(KC.K)                     # Insert link
UNDO = KC.LCMD(KC.Z)                      # Undo
REDO = KC.LCMD(KC.LSFT(KC.Z))             # Redo
CUT = KC.LCMD(KC.X)                       # Cut
COPY = KC.LCMD(KC.C)                      # Copy
PASTE = KC.LCMD(KC.V)                     # Paste
SAVE = KC.LCMD(KC.S)                      # Control + S
SEALL = KC.LCMD(KC.A)                     # Select all
CMD_T = KC.LCMD(KC.T)                     # New browser tab
CMD_W = KC.LCMD(KC.W)                     # Close browser tab
CMD_Q = KC.LCMD(KC.Q)                     # Close application
CMD_L = KC.LCMD(KC.L)                     # Chrome search bar
L_COMM = KC.LCMD(KC.SLSH)                 # Toggle line comment
B_COMM = KC.LALT(KC.LSFT(KC.A))           # Toggle block comment

ACNT = KC.LALT(KC.E)                      # Accent character
TILD = KC.LALT(KC.N)                      # ˜ character for the ñ
OQUES = KC.LALT(KC.QUES)                  # Open question mark (¿)
OEXCL = KC.LALT(KC.N1)                    # Open exclamation mark (¡)

#Slack
CODE = KC.LCMD(KC.LSFT(KC.C))             # Slack code line
CODEB = KC.LCMD(KC.LALT(KC.LSFT(KC.C)))   # Slack code block

LAYER_1 = KC.LT(1, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=250)
LAYER_2 = KC.LT(2, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=250)
LAYER_3 = KC.LT(3, KC.T, prefer_hold=False, tap_interrupted=False, tap_time=250)

# fmt: off
keyboard.keymap = [
    [   # COLEMAK
        KC.Q,     KC.W,     KC.F,     KC.P,     KC.G,          KC.J,     KC.L,     KC.U,     KC.Y,     KC.EXLM,
        KC.A,     KC.R,     KC.S,     LAYER_3,  KC.D,          KC.H,     KC.N,     KC.E,     KC.I,     KC.O,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,          KC.K,     KC.M,     KC.COMM,  KC.DOT,   KC.QUES,
                                      KC.LSFT,  LAYER_1,       LAYER_2,  KC.SPC,
    ],
    [   # LAYER_1
        KC.ESC,   XXXXXXX,  SEALL,    SAVE,     KC.SLSH,       KC.BSLS,  KC.N1,    KC.N2,    KC.N3,    KC.PMNS,
        KC.LSFT,  KC.LCTL,  KC.LALT,  KC.LCMD,  KC.TAB,        KC.DQUO,  KC.N4,    KC.N5,    KC.N6,    KC.EQL,
        REDO,     CUT,      COPY,     PASTE,    UNDO,          KC.QUOT,  KC.N7,    KC.N8,    KC.N9,    KC.UNDS,
                                      _______,  LAYER_1,       LAYER_2,  KC.N0,
    ],
    [   # LAYER_2
        KC.LPRN,  KC.RPRN,  KC.LCBR,  KC.RCBR,  CODEB,         TILD,     PTAB,     KC.UP,    NTAB,     SPOTL,
        KC.LSFT,  KC.LCTL,  KC.LALT,  KC.LCMD,  CODE,          ACNT,     KC.LEFT,  KC.DOWN,  KC.RGHT,  CMD_L,
        OEXCL,    OQUES,    KC.LBRC,  KC.RBRC,  KC.GRV,        KC.SCLN,  KC.COLN,  SEARCH,   CTL_K,    KC.AT,
                                      _______,  LAYER_1   ,    LAYER_2,  _______,
    ],
    [   # LAYER_3
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,       KC.F12,  KC.VOLD,  KC.VOLU,  KC.MUTE,   XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  LAYER_3,  XXXXXXX,       KC.PPLS,  KC.HASH,  KC.ASTR,  KC.AMPR,  KC.PIPE,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,       CMD_T,    L_COMM,   B_COMM,   XXXXXXX,  CMD_W,
                                      _______,  LAYER_1,       LAYER_2,  CMD_Q,
    ]
]
# fmt: on

if __name__ == '__main__':
    keyboard.go()

#So on each layer, put the switch to the third layer where the other keys is. So lets say you have a split with 2 space bars, and you want to go to layer 3 (adjust), you could set the left space to MO(1), the right to MO(2). Then on those layers, make the other key MO(3). Then no matter which order you hit them, you'll end up on MO(3