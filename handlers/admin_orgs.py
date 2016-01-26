#!/usr/bin/env python
# coding=utf-8

import tornado.web

from dbmethod import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class AdminOrgHandler(tornado.web.RequestHandler):
    """
    the list of orgnazations, you can add new, delete, set time and so on.
    """
    def get(self):
        """
        display the webpage, list all of the orgnazations.
        """
        
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
    """
    add new orgnazations
    """
    def get(self):
        self.render("admin_neworg.html")
    
    def post(self):
        """
        get the data from before web page.
        """
        org_name = self.get_argument("orgname")
        org_person = self.get_argument("orgperson")
        org_phone = self.get_argument("orgphone")
        org_wechat = self.get_argument("orgwechat")
        org_address = self.get_argument("orgaddress")

        try:
            insertData("orgs", name=org_name, person=org_person, phone=org_phone, wechat=org_wechat, address=org_address)
            self.write("1")
        except:
            self.write("0")
    
