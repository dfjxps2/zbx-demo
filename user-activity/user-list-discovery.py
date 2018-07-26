# -*- coding: utf-8 -*-

import MySQLdb
from MySQLdb.cursors import DictCursor
import json


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", "root", "root", "portaldb", charset='utf8', cursorclass=DictCursor)

    cursor = db.cursor()

    cursor.execute("select user_name, user_real_name from sys_user where user_state = 1")

    rs = cursor.fetchall()

    data = []
    for row in rs:
#        print "%s, %s" % (row['user_name'], row['user_real_name'])
        data.append({'{#USER_NAME}' : row['user_name'], '{#USER_REAL_NAME}': row['user_real_name']})

    db.close()

    print json.dumps({'data': data}, indent=4, ensure_ascii=False).encode('utf8')

