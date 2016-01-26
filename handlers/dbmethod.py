#!/usr/bin/env python
# coding=utf-8

from db import *

def insertData(tablename, **kargs):
    """
    insert data to table, **kargs is the field and data, example name="qiwsir", password="123"
    """
    fields = ",".join(kargs.keys())
    values = tuple(kargs.values())
    p = ["%s"] * len(kargs.values())
    ps = ", ".join(p)

    sql = "insert into " + tablename + " (" + fields + ") values (" + ps + ")"
    cur.execute(sql, values)
    conn.commit()


def selectData(tablename, *fields):
    """
    select all the data of fields from table. 
    """
    fields = ", ".join(list(fields))
    sql = "select " + fields + " from " + tablename
    cur.execute(sql)
    return cur.fetchall()


if __name__ == "__main__":
    print selectData("orgs", "name", "address", "person", "phone", "wechat")
