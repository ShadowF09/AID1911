from socket import *
from multiprocessing import Process
import signal
from dict_database import *
from time import sleep

ADDR='0.0.0.0'
POST=8801
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((ADDR,POST))
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
s.listen(3)

def handle(c,addr):
    while True:
        data=c.recv(1024).decode()
        tmp=data.split(' ',2)
        d=Database()
        if tmp[0]=='R':
            n=tmp[1]
            p=tmp[2]
            result=d.db_rigster(n,p)
            print(result)
            c.send(result.encode())
        elif tmp[0]=='L':
            n=tmp[1]
            p=tmp[2]
            result=d.db_login(n,p)
            print(result)
            c.send(result.encode())
        elif tmp[0]=='Q':
            n=tmp[1]
            w=tmp[2]
            result=d.db_query(n,w)
            print(result)
            if result:
                result=result[0]+result[1]
                c.send(result.encode())
            else:
                c.send('您所查询的单词不存在'.encode())
        elif tmp[0]=='H':
            n=tmp[1]
            result=d.db_his(n)
            print(result)
            if not result:
                c.send('无记录'.encode())
            else:
                for r in result:
                    msg='%s %s %s %s'%r
                    c.send(msg.encode())
                    sleep(0.05)
                c.send(b' ')
        elif tmp[0]=='E':
            return






def main():
    while True:
        c,addr=s.accept()
        print('conncet from:',addr)
        p=Process(target=handle,args=(c,addr))
        p.start()



if __name__ == '__main__':
    main()
