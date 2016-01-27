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
    fields = ", ".join(fields)
    sql = "select " + fields + " from " + tablename
    cur.execute(sql)
    return cur.fetchall()

def selectDataWhere(table, *fields, **condition):
    """
    select data from table by the condition.
    """
    fields = ", ".join(fields)
    values = [ "'" + str(i) + "'" for i in condition.values() ]
    wheres = ", ".join([ "=".join(one) for one in zip(condition.keys(), values) ])
    sql = "select " + fields + " from " + table + " where " + wheres
    cur.execute(sql)
    return cur.fetchall()

def deleteLine(tablename, **condition):
    """
    delete some lines from table by the condition
    """
    values = [ "'" + str(i) + "'" for i in condition.values() ]
    wheres = ", ".join([ "=".join(one) for one in zip(condition.keys(), values) ])
    sql = "delete from " + tablename + " where " + wheres
    try:
        cur.execute(sql)
        conn.commit()
        return True
    except:
        return False

if __name__ == "__main__":
    print selectDataWhere("orgs", "id", wechat="jjjj")
