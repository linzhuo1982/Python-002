# coding:utf-8

import pandas as pd
import numpy as np

data = {
    'id':[600, 700, None, 900, 1000, 1100, None, 1200, 1300, 1400, 1500, 1600, None],
    'age':[35, 34, 33, 32, None, 30, 29, 28, 27, 26, None, 40, 99]
}
table1 = {
    'id':[600, 700, None, 900, 1000, 1100, None, 1200, 700, 1400, 10, 900, None],
    'age':[35, 34, 33, 32, None, 30, 29, 28, 27, 26, None, 40, 99],
    'order_id':[10001, 10002, 10003, 10001, 10005, 10006, 10001, 10008, 10009, 10010, 10011, 10010, 10013]
}    

table2 ={
    'id':[650, 700, None, 900, 1050, 1100, None, 1200, 750, 1400, 1550, 900, None],
    'age':[35, 34, 37, 32, None, 30, 29, 28, 37, 26, None, 40, 59],
    'order_id':[10001, 10012, 10003, 10001, 10015, 10006, 10001, 10011, 10009, 10010, 10011, 10020, 10013]
}

df = pd.DataFrame(data)
df1 = pd.DataFrame(table1)
df2 = pd.DataFrame(table2)	
#1. 显示全表，同等SELECT * FROM data;
df
df1
df2
#2. 显示限制10个，同等SELECT * FROM data LIMIT 10;
df[:10]
df.loc[:9]
#3. 显示指定列的内容，同等SELECT id FROM data;  //id 是 data 表的特定一列
df['id']

#4. 显示id列的统计，同等SELECT COUNT(id) FROM data;
df['id'].value_counts().sum()

#5. 显示表里id列小于1000且age列大于30的，同等SELECT * FROM data WHERE id<1000 AND age>30;
#df1 = df['id']<1000
#df2 = df['age']>30
#df[df1 & df2]
df[(df['id']<1000) & (df['age']>30)]

#6. 显示已id列为分组，对order_id列中重复的进行统计，同等SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df1.groupby(by=['id'])['order_id'].count() 

#7. 显示table1与table2里，id列内容相同的进行内连接，同等SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
df3 = pd.merge(df1, df2, left_on = 'id', right_on = 'id', how = 'inner')
df3

#8. SELECT * FROM table1 UNION SELECT * FROM table2;
df4 = pd.concat([df1, df2], axis = 0)
df4
#9. 删除table1里id=10的行，同等DELETE FROM table1 WHERE id=10;
df1[~df1['id'].isin([10])]

#10. ALTER TABLE table1 DROP COLUMN column_name;
df1.drop(columns=['age'])











# '''
# 通过连接本机MySql5.7版本数据库，进行SQL语句转换pandas的练习。
# '''

# host='localhost'
# user='root'
# passwd='rootroot'
# db='geek_practice'
# charset='utf8'


# conn= pms.connect(host = host, user = user, passwd = passwd, db = db, charset = charset)
# sql = 'SELECT * FROM week2_proxy'
# df = pd.read_sql(sql, conn)


# # conn.close()
# print(df)
# # loc用来显示行，列表里定义
# df.loc[:9]
# df['proxyip']
# df['realip'].value_counts().sum()+1
# df['age']<30
# df[df['age']<30]
# df[(df['age']<30) & (df['numbers']<1000)]
# df[(df['numbers']>)]
# df[(df['numbers']>1000) & (df['age']>30)]
# df[(df['numbers']<1000) & (df['age']>30)]
# df.groupby(by=['numbers'])['age'].count()
# df = df[df['id'].isin[10]]