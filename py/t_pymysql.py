import pymysql
import config
import re


def execute_select():
    conn = pymysql.connect(
            host=config.LOCAL_MYSQL_HOST,
            user=config.LOCAL_MYSQL_USER,
            passwd=config.LOCAL_MYSQL_PASSWORD,
            db=config.LOCAL_MYSQL_DB,
            charset='utf8mb4',
            read_timeout=10,
            port=3306
        )
    sql = 'select * from test_user , test_user t1, test_user t2, test_user t3, test_user t4  where t1.id=1 and  t2.id=3 and t3.id=3 and t4.id=4 limit 1'
    # self.db.cursor(pymysql.cursors.DictCursor);
    with conn.cursor() as cursor:
        cursor.execute(sql)
        field = cursor.description
        field_list = []
        for f in field:
            tmp_field_name = f[0]
            while tmp_field_name in field_list:
                sr = re.search(r'\(\d+\)', tmp_field_name)
                if sr:
                    cnt = int(sr.group()[1:-1]) + 1
                else:
                    cnt = 1
                tmp_field_name = re.sub(r'\(\d+\)', '', tmp_field_name) + f'({cnt})'
            field_list.append(tmp_field_name)
        result = cursor.fetchall()
        r = [dict(zip(field_list, r)) for r in result]
        print(r)

    conn.close()


if __name__ == '__main__':
    execute_select()
