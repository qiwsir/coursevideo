#!/usr/bin/env python
# coding=utf-8

import tornado.web

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class AdminOrgHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("admin_orgs.html")

    def post(self):
        """
        user login the website.
        """
        user_name = self.get_argument("username")
        user_pwd = self.get_argument("password")
        
        if user_name and user_pwd:
            sql = "select * from users where username='{0}'".format(user_name)

        try:
            cur.execute(sql)
            password_in = cur.fetchone()[2]
            if user_pwd == password_in:
                self.write("1")
            else:
                self.write("0")
        except:
            self.write("-1")
       
class AdminNewOrgHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("admin_neworg.html")
