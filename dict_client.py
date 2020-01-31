from socket import *
import sys


ADDR = '0.0.0.0'
POST = 8801
s = socket()
s.connect((ADDR,POST))

def do_register(s):
    name = input('请输入用户名：')
    psd = input('请输入密码:')
    msg = 'R ' + name + ' ' + str(psd)
    s.send(msg.encode())
    data=s.recv(64).decode()
    print(data)

def do_login(s):
    name=input('请输入用户名：')
    password=input('请输入密码：')
    msg='L '+name+' '+str(password)
    s.send(msg.encode())
    data=s.recv(64).decode()
    if data=='OK':
        level2(s,name)
    else:
        print(data)

def do_query(s,name):
    word=input('输入要查询的单词：')
    msg='Q '+name+' '+word
    s.send(msg.encode())
    data=s.recv(1024).decode()
    print(data)


def his(s,name):
    msg='H '+name
    s.send(msg.encode())
    while True:
        data=s.recv(2048).decode()
        print(data)
        if data==' ':
            break


def level2(s,name):
    while True:
        print('======================')
        print('1 查询 2 历史记录 3 返回')
        print('======================')
        cmd=input('输入命令：')
        if cmd=='1':
            do_query(s,name)
        elif cmd=='2':
            his(s,name)
        elif cmd=='3':
            level1(s)



def level1(s):
    while True:
        print('===============')
        print('1注册 2登录 3退出')
        print('===============')
        cmd=input('输入命令：')
        if cmd=='1':
            do_register(s)
        elif cmd=='2':
            do_login(s)
        elif cmd=='3':
            s.send(b'E')
            sys.exit('谢谢使用')
        else:
            print('请输入正确命令')




def main():
    level1(s)


if __name__ == '__main__':
    main()