from pwn import *

p = remote("vortex.labs.overthewire.org", 5842)
print p.recvline()
