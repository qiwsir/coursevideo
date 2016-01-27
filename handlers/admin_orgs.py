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
        orgs_info = selectData("orgs", "name", "person", "phone", "wechat")
        
        self.render("admin_orgs.html", orgs=orgs_info)

    def post(self):
        """
        delete the orgnazation.
        """
        org_name = self.get_argument("orgname")
        
        if deleteLine("orgs", name=org_name):
            print "delete"
            self.write("1")
        else:
            self.write("0")

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
        
        result = selectDataWhere("orgs", "id", name=org_name)
        if result:
            self.write("-1")
        else:
            try:
                insertData("orgs", name=org_name, person=org_person, phone=org_phone, wechat=org_wechat, address=org_address)
                self.write("1")
            except:
                self.write("0")
    
