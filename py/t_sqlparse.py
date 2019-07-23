"""
测试 sqlparse 库
参考文档: https://sqlparse.readthedocs.io/en/latest/intro/
"""

import sqlparse
from sqlparse.sql import Where
from sqlparse.sql import Statement
from sqlparse.sql import IdentifierList
def test_parse_sql():
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
import re
def tables_in_query(sql_str):

    # remove the /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])

    # split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)

    # scan the tokens. if we see a FROM or JOIN, we set the get_next
    # flag, and grab the next one (unless it's SELECT).

    result = set()
    get_next = False
    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                result.add(tok)
            get_next = False
        get_next = tok.lower() in ["from", "join"]

    return result

from sqlparse.sql import IdentifierList
from sqlparse.tokens import Keyword


# def parse_sql_tables(sql):
#     tables = []
#     parsed = sqlparse.parse(sql)
#     stmt = parsed[0]
#     from_seen = False
#     for token in stmt.tokens:
#         if from_seen:
#             if token.ttype is Keyword:
#                 continue
#             else:
#                 if isinstance(token, IdentifierList):
#                     for identifier in token.get_identifiers():
#                         tables.append(SQLParser.get_table_name(identifier))
#                 elif isinstance(token, Identifier):
#                     tables.append(SQLParser.get_table_name(token))
#                 else:
#                     pass
#         if token.ttype is Keyword and token.value.upper() == "FROM":
#             from_seen = True
#     return tables


def test_parse_alter_for_gh_ost():
    sql = 'alter table table_name drop column c'
    sql = 'alter table table_name add column c varchar(20);'
    sql_statement = sqlparse.parse(sql)[0]
    table_name = sql_statement.get_name()
    first_name = sql_statement._get_first_name()
    print(sql_statement.tokens.get_identifiers())
    condition = 'alter table table_name drop column c'
    # table_name = tables_in_query(sql)
    print(table_name)
    print(first_name)


def test_alter(sql=None):
    if not sql:
        sql = '      /* alter    table `table_name` drop column c   ;*/alter    table table_name drop column c   ;  '
        # sql = 'create index idex_name on table_name(cname)'
    stmt = sqlparse.parse(sql)[0]
    stmt_type = stmt.get_type()
    if stmt_type != 'ALTER':
        print(stmt_type)
        print('不是alter语句，请dba手工执行')
    value_list = []
    for t in stmt.tokens:
        value = t.value
        if t.is_whitespace or value.startswith('/*') or value.startswith('--') or value == ';':
            continue
        else:
            value_list.append(value)
    print(value_list)
    print(' '.join(value_list))
    print('table name:', value_list[2])
    print('gh-ost condition:', ' '.join(value_list[3:]))


if __name__ == '__main__':
    # test_parse_alter_for_gh_ost()
    test_alter()