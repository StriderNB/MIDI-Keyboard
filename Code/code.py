import board
import analogio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.midi import Midi
from kmk.extensions.RGB import RGB
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# --- ENCODER CONFIG ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ( (board.TX, board.RX, 4),)

# --- MIDI CONFIG ---
midi_ext = Midi()
keyboard.extensions.append(midi_ext)

# --- SLIDER CONFIG ---
slider_1_pin = analogio.AnalogIn(board.IO11)
slider_2_pin = analogio.AnalogIn(board.IO12)
previous_s1 = 0
previous_s2 = 0

# --- HARDWARE PIN CONFIG ---
keyboard.row_pins = (board.IO1, board.IO2, board.IO3, board.IO4, board.IO5, board.IO6, board.IO8, board.IO9, board.IO10, board.IO13)
keyboard.col_pins = ()
keyboard.diode_orientation = DiodeOrientation.COLS_SHARE_DIODE

# --- SK6812 NEOPIXEL LED CONFIG ---
rgb_ext = RGB(
    pixel_pin=board.IO7, # Pin connected to the SK6812 NeoPixel LEDs
    num_pixels=3,        # Number of SK6812 NeoPixel LEDs connected to the pin
    val_default=100,       # Default brightness for the SK6812 NeoPixel LEDs
    rgb_order=(0, 2, 1),   # RGB color order for the SK6812 NeoPixel LEDs
)
keyboard.extensions.append(rgb_ext)

# --- KEYMAP ---
keyboard.keymap = [
    [
        KC.MIDI('C4', velocity 127), # Touch_2
        KC.MIDI('D4', velocity 127), # Touch_3
        KC.MIDI('E4', velocity 127), # Touch_1
        KC.MIDI('F4', velocity 127), # Touch_6
        KC.MIDI('G4', velocity 127), # Touch_5
        KC.MIDI('A4', velocity 127), # Touch_4
        KC.MIDI_Octave_UP,           # Switch_3
        KC.MIDI_OCTAVE_DOWN,         # Switch_2
        KC.MIDI_SUSTAIN,             # Switch_1
        KC.RGB_OFF,                  # Switch_4  
    ]
]

# --- ENCODER ACTIONS ---
# Keeps CC 1 (Modulation) for both directions (127 = Increase/Up, 0 = Decrease/Down)
encoder_handler.map = [
    (
        (KC.MIDI_CC(1, 127), KC.MIDI_CC(7, 0))
    )
]

# --- MAIN LOOP ---
# Initialize a manual loop
keyboard.before_matrix_scan()

while True:
    # Allow KMK to process events
    keyboard.main_loop()

    # Read slider values mapped to MIDI CC range (0-127)
    current_s1 = int(slider_1_pin.value / 65535 * 127)
    current_s2 = int(slider_2_pin.value / 65535 * 127)

    # Send MIDI CC messages if slider values have changed significantly
    if abs(current_s1 - previous_s1) > 1:
        midi_ext.midi.send(Midi.CC(control=74, value=current_s1))
        previous_s1 = current_s1

    if abs(current_s2 - previous_s2) > 1:
        midi_ext.midi.send(Midi.CC(control=91, value=current_s2))
        previous_s2 = current_s2

    time.sleep(0.01)  # Small delay to prevent busy-waiting