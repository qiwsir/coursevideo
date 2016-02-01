#!/usr/bin/env python
# coding=utf-8

import tornado.web

from dbmethod import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class AdminUserHandler(tornado.web.RequestHandler):
    """
    the list of users, you can add new, delete, set time and so on.
    """
    def get(self):
        """
        display the webpage, list all of the users.
        """
        users_info = selectData("users", "mobilephone", "name", "orgnameID", "status", "id")
        orgids = [i[2] for i in users_info]
        orgnames = [selectDataWhere("orgs", "name", id=i) for i in orgids]
        
        users_info_reverse = users_info[::-1] 
        self.render("admin_users.html", users=users_info_reverse, orgs=orgnames.reverse())

    def post(self):
        """
        delete the orgnazation.
        """
        org_name = self.get_argument("orgname")
        
        if deleteLine("orgs", name=org_name):
            self.write("1")
        else:
            self.write("0")

class AdminNewUserHandler(tornado.web.RequestHandler):
    """
    add new user
    """
    def get(self):
        self.render("admin_newuser.html")
    
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
   
class AdminEditOrgHandler(tornado.web.RequestHandler):
    """
    edit the information of the orgnazations
    """
    def get(self):
        org_id = self.get_argument("orgid")
        org_info = selectDataWhere("orgs", "address", "person", "phone", "wechat", "id", "name", id=org_id)

        self.render("admin_editorg.html", orginfo=org_info[0])

    def post(self):
        """
        get the information from before web to rewrite the org.
        """ 
        org_name = self.get_argument("orgname")
        org_person = self.get_argument("orgperson")
        org_phone = self.get_argument("orgphone")
        org_wechat = self.get_argument("orgwechat")
        org_address = self.get_argument("orgaddress")
        org_id = self.get_argument("orgid")
        
        updatethings = {"name":org_name, "person":org_person, "phone":org_phone, "wechat":org_wechat, "address":org_address}
        condition = {"id":org_id}
        try:
            updateLineWhere("orgs", updatethings, condition)
            self.write("1")
        except:
            self.write("0")


class AdminReadOrgHandler(tornado.web.RequestHandler):
    """
    list the information of the orgnazations
    """
    def get(self):
        org_id = self.get_argument("orgid")
        org_info = selectDataWhere("orgs", "address", "person", "phone", "wechat", "id", "name", id=org_id)

        self.render("admin_readorg.html", orginfo=org_info[0])
