from socket import *

ADDR = '0.0.0.0'
POST = 8888

def do_register(s):
    name = input('请输入用户名：')
    psd = input('请输入密码:')
    msg = 'R ' + name + ' ' + str(psd)
    s.send(msg.encode())


def level1(s):
    print('===============')
    print('1注册 2登录 3退出')
    print('===============')
    cmd=input('输入命令：')
    if cmd==1:
        do_register(s)

    elif cmd==2:
        pass
    else:
        pass




def main():
    s = socket()
    s.connect((ADDR,POST))
    level1(s)


if __name__ == '__main__':
    main()