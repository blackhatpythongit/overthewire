from pwn import *

r = remote("vortex.labs.overthewire.org", 5842)
ns = [r.recvn(4) for _ in range(4)]
ans = sum(u32(n) for n in ns)
r.send(p32(ans&0xffffffff))
print r.recvall()
