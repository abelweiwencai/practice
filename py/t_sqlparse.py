"""
测试 sqlparse 库
参考文档: https://sqlparse.readthedocs.io/en/latest/intro/
"""

import sqlparse
from sqlparse.sql import Where
from sqlparse.sql import Statement
from sqlparse.sql import IdentifierList

# 拆分sql
sql = 'select * from foo; select * from bar;'
parsed_sql = sqlparse.split(sql)
# print(parsed_sql)
# print('*' * 80)

# 格式化sql
sql = 'select * from foo where id in (select id from bar);'
# print(sqlparse.format(sql, reindent=True, keyword_case='upper'))
# print('*' * 80)

# parse 函数
sql = '''-- lime comment1  
 /* comment1 */ select * from 
 --sdf
 mytable where id = 1     /* comment3 */'''
parsed = sqlparse.parse(sql)
print(parsed[0].get_type())

sql = '''update table_name_info set file_name = '20190220.csv;replacement_20190220.csv;.ok', status = 0 where       id = 123;
         update table_name_info set file_name = '20190220.csv;replacement_20190220.csv;.ok', status = 0 where  id in （select id from t1）;
         update table_name_info set file_name = '20190220.csv;replacement_20190220.csv;.ok;.ok', status = 0 where  id in （select id from t1）;
         update table_name_info set file_name = 'update t1 set id = 1 where id = 3;', status = 0 where id in （1, 2, 3, 4, 5, 6, 7, 8）/* select  */ 
         -- sdfa
         ;
         UPDATE table1  LEFT JOIN table2 ON table1.xx=table2.xx   SET table1.xx=value,table2.xx=value WHERE table1.xx=xx;'''

sql = '''
         UPDATE table1  LEFT JOIN table2 ON table1.xx=table2.xx   SET table1.xx=value,table2.xx=value WHERE table1.xx=xx;'''

parsed = sqlparse.parse(sql)
# sql_statement = parsed[0]
# print(sql_statement.flatten())
for sql_statement in parsed:
    print('*' * 100)
    print('sql type:', sql_statement.get_type())  # sql type , the first ddl or dml type
    # print(sql_statement.get_alias())
    print('table name:', sql_statement.get_name())  # table name
    print(sql_statement._get_first_name())
    has_where = False
    for t in reversed(sql_statement.tokens):
        if isinstance(t, Where):
            print('where statement:', t.value)  # where 条件
            print(t.get_name())
            has_where = True
            break
        else:
            print('not where')
    print('has where', has_where)
    print(sql_statement.value)
print(len(parsed))
# print(sql_statement.get_parent_name())
# print(sql_statement.get_real_name())
# print(sql_statement.Where)
# print(sql_statement.get_token_at_offset(3))
# print(sql_statement.group_tokens()) --
# print(sql_statement.has_alias())
# print(sql_statement.insert_after())--
# print(sql_statement.insert_before())--
# print(sql_statement.token_first())
# print(sql_statement.token_prev(2))
# print(sql_statement.get_token_at_offset())--


# 考虑条件  1. 嵌套where 2.replace 语句 3. 一条sqlinsert 多条sql 4. update 多条（in）
# 1. 前面有单行、多行注释 2.中间有单行、多行注释  3.结束有单行、多行注释
# 获取sql类型 dml ddl
# sql_statement.get_type()
# 获取表名

# 获取 where 条件
