from pwn import *

host = "vortex.labs.overthewire.org"
user = "vortex5"
password = ":4VtbC4lr"

shell = ssh(host=host, user=user, password=password)
r = shell.run("/vortex/vortex5")
r.sendline("rlTf6")
r.interactive()
