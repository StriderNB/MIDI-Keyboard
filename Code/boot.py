import usb_midi
import storage

# Enable USB MIDI (creates 1 input and 1 output port)
usb_midi.enable()

# Optional: To keep the CIRCUITPY drive visible for editing, do nothing else.
# (If you ever want to hide the drive when plugged in normally, you would configure it here)