from pwn import *

<<<<<<< HEAD
r = remote("vortex.labs.overthewire.org", 5842)
ns = [r.recvn(4) for _ in range(4)]
ans = sum(u32(n) for n in ns)
r.send(p32(ans&0xffffffff))
print r.recvall()
=======
p = remote("vortex.labs.overthewire.org", 5842)
print p.recvline()
>>>>>>> d56891b45199118ee4ea8a4ddf24812e629ee30a
