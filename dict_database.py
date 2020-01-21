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

    def db_rigster(self,n,p):
        try:
            self.sql='select name from user where name=n;'
            self.cur.execute(self.sql,n)
            db.commit()
        except Exception:
            db.rollback()
        data=self.cur.fetchone()
        if not data:
            self.sql='insert into user (name,password) values (n,p);'
            self.cur.execute(self.sql,n,p)
            db.commit()
            return '注册成功'
        else:
            return '用户名已存在'





# create database dictonline charset=utf8

# create table user(id int primary key auto_increment,
# name varchar(30),
# password varchar(60));

