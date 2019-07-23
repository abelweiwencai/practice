"""
试用inception
"""

import config
import MySQLdb


def inception_execute(op_type, sql, db_name='weiwencai'):

    sql = r"""
    /*--user={username};--password={password};--host={host};
    --enable-{op_type};--enable-ignore-warnings;--enable-remote-backup;
    --port={port};*/
    inception_magic_start;
    use {database};
    {sql}
    inception_magic_commit;
    """.format(username=config.MYSQL_USER,
               password=config.MYSQL_PASSWORD,
               host=config.MYSQL_HOST,
               port=config.MYSQL_PORT,
               op_type=op_type,
               database=db_name,
               sql=sql)

    try:
        conn = MySQLdb.connect(host=config.INCEPTION_HOST,
                               user=config.INCEPTION_USERNAME,
                               port=config.INCEPTION_PORT,
                               charset='utf8')
        if len(conn._server_version) == 2 and not conn._server_version[0]:
            # 当conn._server_version = (None, 1) 的时候，MySQLdb库会报错
            conn._server_version = (5, 1)
        cur = conn.cursor()
        ret = cur.execute(sql)
        result = cur.fetchall()
        # num_fields = len(cur.description)
        field_names = [i[0].lower() for i in cur.description]
        cur.close()
        conn.close()
    except Exception as e:
        print(f'sql:{sql}')
        if e.args[0] == 2576:
            err_msg = f'sql审核失败，请确认sql语法是否正确，并且用分号作为每个sql结束！{e.args[0]}'
        else:
            err_msg = f'sql审核失败，请DBA确保该库已经加入inception的白名单！{e.args[0]}'

        raise Exception(err_msg)
        # return False, err_msg

    from pprint import pprint
    pprint(field_names)
    pprint(result)

    if len(result) == 1 or result[0][2] == 2:
        raise Exception('连接到 {} 失败：{}'.format(db_name, result[0][4]))

    tmp_r = result[0]
    tmp_r = [str(x) for x in tmp_r]
    print(','.join(tmp_r))
    print(f'返回结果数量：{len(result)}')
    result = result[1:]
    return result, field_names


if __name__ == '__main__':
    sql = """
    CREATE TABLE `test_user1` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        PRIMARY KEY (`id`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
    """
    sql = """
    update test_user set username='nnnn' where id in (34,35,36,37);
    insert into test_user(`id`, `username`) values (57, 'name7'), (88, 'name8');
    insert into test_user(`id`, `username`) values (36, 'name2');
    insert into test_user(`id`, `username`) values (46, 'name2');
    insert into test_user(`id`, `username`) values (47, 'name2');
    insert into test_user(`id`, `username`) values (48, 'name2');
    """
    sql = 'alter table test_user add test_column number;'  

#     sql = '''
#     CREATE TABLE `ops_test_user4` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#   `is_staff` tinyint(1) NOT NULL,
#   `is_deleted` tinyint(1) NOT NULL,
#   `full_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#   `is_active` tinyint(1) NOT NULL,
#   PRIMARY KEY (`id`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
#    '''
#
    # sql = '''
    # delete from ops_test_user4  where username = \'rr\';
    # '''
    inception_execute(op_type='execute', sql=sql, db_name='weiwencai')

