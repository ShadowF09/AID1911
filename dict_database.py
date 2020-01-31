import pymysql
db=pymysql.connect(host='0.0.0.0',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dictonline',
                   charset='utf8')
class Database():
    def __init__(self):
        self.cur=db.cursor()

    def db_login(self,n,p):
        self.sql='select name,password from user where name=%s and password=%s;'
        self.cur.execute(self.sql,[n,p])
        data=self.cur.fetchone()
        if data:
            return 'OK'
        else:
            return '登录失败'



    def db_rigster(self,n,p):
        self.sql='select name from user where name=%s;'
        self.cur.execute(self.sql,n)
        data=self.cur.fetchone()
        if not data:
            try:
                self.sql='insert into user (name,password) values (%s,%s);'
                self.cur.execute(self.sql,[n,p])
                db.commit()
                return '注册成功'
            except Exception:
                db.rollback()
                return '注册失败'
        else:
            return '用户名已存在'

    def db_query(self,n,w):
        self.sql='select word,meaning from words where word=%s;'
        self.cur.execute(self.sql,w)
        data=self.cur.fetchone()
        if data:
            try:
                self.sql='insert into history (word,name) values (%s,%s);'
                self.cur.execute(self.sql,[w,n])
                db.commit()
                return data
            except Exception:
                db.rollback()
        else:
            return

    def db_his(self,n):
        self.sql='select * from history where name=%s order by time desc limit 5;'
        self.cur.execute(self.sql,n)
        data=self.cur.fetchall()
        return data





# create database dictonline charset=utf8 创建库

# create table user(id int primary key auto_increment,
# name varchar(30),
# password varchar(60)); 创建用户表

# create table history(id int primary key auto_increment,
# word varchar(30),
# meaning varchar(256),
# time datetime); 创建历史记录表


