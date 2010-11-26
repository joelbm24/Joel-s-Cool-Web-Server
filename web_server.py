import socket
import sys

try:
    host = sys.argv[1]
    port = int(sys.argv[2])
except:
    host = "127.0.0.1"
    port = 8080

f = open('index.html', 'rw')
file = f.readlines()

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

c.bind((host, port))
c.listen(1)

print "Joel's Cool Web Server started"
print "Host:", host
print "Port:", port

while 1:
    csock, caddr = c.accept()
    cfile = csock.makefile('rw', 0)

    line = cfile.readline().strip()

    for lin in file:
        cfile.write(lin)

    cfile.close()
    csock.close()
