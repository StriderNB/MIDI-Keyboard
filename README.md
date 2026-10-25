# MIDI-Keyboard
Week 3 project of Half Life event hosted by Hack Club.
<img width="2001" height="1185" alt="Screenshot 2026-10-24 232310" src="https://github.com/user-attachments/assets/73ed7ae2-9e37-440f-b4a9-71063c2b77de" />
# Features
A Midi Keyboard in the shape of a star!

3 Switches with shine through rgb SK6812MINI-E Neopixels

2 Slide potentiometers

A clickable 360 degree rotary encoder

Controlled and powered by a Waveshare ESP32-S3-Zero

# Setup
1. Install CircuitPython on the ESP32-S3 ZERO
2. Install KMK and adafruit and neopixel libraries
3. Save the boot.py file in the root of the CIRCUITPY drive
4. Save the code.py file onto the drive
5. Open any DAW and select the Midi device

# Controls
| Button | Function |
| :--- | :---: |
| Touch 1-6 | Plays a note |
| Switch 1 | Turns on sustain |
| Switch 2 | Turns the touch buttons down an octave |
| Switch 3 | Turns the touch buttons up an octave |
| Slider 1 | Filter cutoff |
| Slider 2 | Reverb | 
| Rotary Encoder | Turns volume up or down |
| Rotary Encoder Button | Turns off the led rbg |

# BOM
| Item | Qty | Supplier | Cost/item | Total Cost | Link |
| :--- | :---: | :--- | :---: | :---: | :--- |
| SK6812MINI-E | 10 | Aliexpress | $0.36 | $3.60 | [Link](https://aliexpress.us) |
| Bourns Slider | 2 | AliExpress | $3.00 | $6.00 | [Link](https://aliexpress.us) |
| Rotary Encoder | 1 | AliExpress | $1.55 | $1.55 | [Link](https://aliexpress.us) |
| Waveshare ESP32-S3-ZERO | 1 | AliExpress | $4.32 | $4.32 | [Link](https://aliexpress.us) |

#Additional Images
<img width="1241" height="855" alt="Screenshot 2026-10-25 155427" src="https://github.com/user-attachments/assets/c714738a-6c12-40ce-a117-2c630e0b97e2" />
<img width="1444" height="995" alt="Screenshot 2026-10-25 155400" src="https://github.com/user-attachments/assets/7a4541f8-24ab-43e1-98c3-ce75f0cf0906" />
<img width="1762" height="1199" alt="Screenshot 2026-10-24 232341" src="https://github.com/user-attachments/assets/41105a58-f7ed-47e5-817d-f8a49c2b0d5d" />
<img width="1372" height="1195" alt="Screenshot 2026-10-24 232227" src="https://github.com/user-attachments/assets/d00a9eb4-a156-426b-9851-4e8261d6c9de" />
