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
| Rotary Encoder Button | Turns off the led RGB |

# BOM
| Item | Qty | Supplier | Cost/item | Total Cost | Link |
| :--- | :---: | :--- | :---: | :---: | :--- |
| SK6812MINI-E | 10 | Aliexpress | $0.36 | $3.60 | [Link](https://www.aliexpress.us/item/3256807677321116.html?spm=a2g0o.cart.0.0.1f5c38da4NfrhP&mp=1&pdp_npi=6%40dis%21USD%21USD+3.61%21USD+3.61%21%21USD+3.61%21%21%21%4021030dcd17929017765575367e0f08%2112000042594617264%21ct%21US%218321405938%21%211%210%21&_gl=1*12w1jau*_gcl_aw*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_dc*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_au*MjEyNDg5MTc2NC4xNzkwNTM4MDQ3*_ga*NDE0NzUzODY3LjE3OTI2OTUyMjg.*_ga_VED1YSGNC7*czE3OTI5NjM5NzEkbzYkZzEkdDE3OTI5NjQ0MDUkajUzJGwwJGgw&gatewayAdapt=glo2usa) |
| Bourns Slider | 2 | AliExpress | $3.00 | $6.00 | [Link](https://www.aliexpress.us/item/3256808527031041.html?spm=a2g0o.cart.0.0.1f5c38da4NfrhP&mp=1&pdp_npi=6%40dis%21USD%21USD+2.99%21USD+2.99%21%21USD+2.99%21%21%21%4021030dcd17929017765575367e0f08%2112000046545295125%21ct%21US%218321405938%21%212%210%21&_gl=1*ppe06u*_gcl_aw*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_dc*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_au*MjEyNDg5MTc2NC4xNzkwNTM4MDQ3*_ga*NDE0NzUzODY3LjE3OTI2OTUyMjg.*_ga_VED1YSGNC7*czE3OTI5NjM5NzEkbzYkZzEkdDE3OTI5NjQ0MDkkajQ5JGwwJGgw&gatewayAdapt=glo2usa) |
| Rotary Encoder | 1 | AliExpress | $1.55 | $1.55 | [Link](https://www.aliexpress.us/item/3256807457768762.html?spm=a2g0o.cart.0.0.1f5c38da4NfrhP&mp=1&pdp_npi=6%40dis%21USD%21USD+1.55%21USD+1.55%21%21USD+1.55%21%21%21%4021030dcd17929017765575367e0f08%2112000041630839427%21ct%21US%218321405938%21%211%210%21&_gl=1*10wpaba*_gcl_aw*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_dc*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_au*MjEyNDg5MTc2NC4xNzkwNTM4MDQ3*_ga*NDE0NzUzODY3LjE3OTI2OTUyMjg.*_ga_VED1YSGNC7*czE3OTI5NjM5NzEkbzYkZzEkdDE3OTI5NjQ0MDMkajU1JGwwJGgw&gatewayAdapt=glo2usa) |
| Waveshare ESP32-S3-ZERO | 1 | AliExpress | $4.32 | $4.32 | [Link](https://www.aliexpress.us/item/3256807949476561.html?spm=a2g0o.cart.0.0.1f5c38da4NfrhP&mp=1&pdp_npi=6%40dis%21USD%21USD+4.32%21USD+4.32%21%21USD+4.32%21%21%21%4021030dcd17929017765575367e0f08%2112000051614441514%21ct%21US%218321405938%21%211%210%21&_gl=1*10wpaba*_gcl_aw*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_dc*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_au*MjEyNDg5MTc2NC4xNzkwNTM4MDQ3*_ga*NDE0NzUzODY3LjE3OTI2OTUyMjg.*_ga_VED1YSGNC7*czE3OTI5NjM5NzEkbzYkZzEkdDE3OTI5NjQ0MDMkajU1JGwwJGgw&gatewayAdapt=glo2usa) |
| Keycaps | 10 | AliExpress | $0.30 | $3.00 | [Link](https://www.aliexpress.us/item/3256809178113894.html?spm=a2g0o.cart.0.0.1f5c38da4NfrhP&mp=1&pdp_npi=6%40dis%21USD%21USD+3.03%21USD+3.03%21%21USD+3.03%21%21%21%4021030dcd17929017765575367e0f08%2112000048873877375%21ct%21US%218321405938%21%211%210%21&_gl=1*ndrp7t*_gcl_aw*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_dc*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_au*MjEyNDg5MTc2NC4xNzkwNTM4MDQ3*_ga*NDE0NzUzODY3LjE3OTI2OTUyMjg.*_ga_VED1YSGNC7*czE3OTI5NjM5NzEkbzYkZzEkdDE3OTI5NjQ1MjIkajU2JGwwJGgw&gatewayAdapt=glo2usa) |
| Switches | 10 | AliExpress | $0.20 | $2.00 | [Link](https://www.aliexpress.us/item/2251832663616399.html?spm=a2g0o.cart.0.0.1f5c38da4NfrhP&mp=1&pdp_npi=6%40dis%21USD%21USD+2.02%21USD+2.02%21%21USD+2.02%21%21%21%4021030dcd17929017765575367e0f08%2165277852476%21ct%21US%218321405938%21%211%210%21&_gl=1*6j82c4*_gcl_aw*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_dc*R0NMLjE3OTI5MDE2MzAuQ2owS0NRandydkhXQmhES0FSSXNBQm1wN2gxLVVCZjU0a2JLd012Mlkya0pxbDRXSDNaMlBoOU5SYVVBTk5SSXRMaWw1bFJrbXpXZzZJNGFBcFBLRUFMd193Y0I.*_gcl_au*MjEyNDg5MTc2NC4xNzkwNTM4MDQ3*_ga*NDE0NzUzODY3LjE3OTI2OTUyMjg.*_ga_VED1YSGNC7*czE3OTI5NjM5NzEkbzYkZzEkdDE3OTI5NjQ2MDgkajU4JGwwJGgw&gatewayAdapt=glo2usa) |
| PCB | 1 | PCBWay | $5.00 | $5.00 | [Link](https://pcbway.com) |
| Estimated total shipping | 1 | | | $8.30 | |

#Additional Images
<img width="1241" height="855" alt="Screenshot 2026-10-25 155427" src="https://github.com/user-attachments/assets/c714738a-6c12-40ce-a117-2c630e0b97e2" />
<img width="1444" height="995" alt="Screenshot 2026-10-25 155400" src="https://github.com/user-attachments/assets/7a4541f8-24ab-43e1-98c3-ce75f0cf0906" />
<img width="1762" height="1199" alt="Screenshot 2026-10-24 232341" src="https://github.com/user-attachments/assets/41105a58-f7ed-47e5-817d-f8a49c2b0d5d" />
<img width="1372" height="1195" alt="Screenshot 2026-10-24 232227" src="https://github.com/user-attachments/assets/d00a9eb4-a156-426b-9851-4e8261d6c9de" />
<img width="1419" height="964" alt="Screenshot 2026-10-25 171503" src="https://github.com/user-attachments/assets/50ad82bf-9554-42ca-8c35-4c9166a9657e" />
