# -*- coding: utf-8 -*-

import MySQLdb
from MySQLdb.cursors import DictCursor
import sys
import datetime

if __name__ == '__main__':

    userName = sys.argv[1]
    dateWindow = int(sys.argv[2])

    from_tm = datetime.datetime.now() + datetime.timedelta(days=-dateWindow)

    db = MySQLdb.connect("localhost", "root", "root", "portaldb", charset='utf8')

    cursor = db.cursor()

    sql = "select count(*) " \
          "from sys_user u, user_access_log l " \
          "where u.user_id = l.user_id " \
          "and u.user_name = '%s' " \
          "and user_op_type = 0 " \
          "and l.log_time > '%s'" % (userName, from_tm.strftime('%Y-%m-%d %H:%M:%S'))

    cursor.execute(sql)

    result = cursor.fetchone()

    db.close()

    print result[0]

