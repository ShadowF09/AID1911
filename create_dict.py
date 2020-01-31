# create table words(id int primary key auto_increment,
# word varchar(30),
# meaning varchar(1024));创建词典表 并加索引

import pymysql
import re

db=pymysql.connect(host='0.0.0.0',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dictonline',
                   charset='utf8')
cur=db.cursor()
f=open('dict.txt')
arg_list=[]
for line in f:
    word=re.findall(r'(\w+)\s(.*)',line)
    arg_list.extend(word)

sql='insert into words (word,meaning) values (%s,%s);'
try:
    cur.executemany(sql,arg_list)
    db.commit()
except:
    db.rollback()
f.close()
cur.close()
db.close()
