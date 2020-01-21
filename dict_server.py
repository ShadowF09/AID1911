from socket import *
from multiprocessing import Process
import signal
from dict_database import *

ADDR='0.0.0.0'
POST=8800
s=socket()
s.bind((ADDR,POST))
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(3)

def handle(c,addr):
    data=c.recv(1024).decode()
    tmp=data.split(' ',2)
    if tmp[0]=='R':
        n=tmp[1]
        p=tmp[2]
        d=Database()
        result=d.db_rigster(n,p)
        c.send(result.encode())
    elif tmp[0]=='L':
        pass
    elif tmp[0]=='Q':
        pass




def main():
    while True:
        c,addr=s.accept()
        print('conncet from:',addr)
        p=Process(target=handle,args=(c,addr))
        p.daemon
        print(1)
        p.start()



if __name__ == '__main__':
    main()
