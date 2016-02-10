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
        orgnames = [selectDataWhere("orgs", "name", id=i)[0][0] for i in orgids]
        orgnames.reverse()
        users_info_reverse = users_info[::-1] 
        self.render("admin_users.html", users=users_info_reverse, orgs=orgnames)

    def post(self):
        """
        delete the orgnazation.
        """
        user_id = self.get_argument("id")
        
        if deleteLine("users", id=user_id):
            self.write("1")
        else:
            self.write("0")

class AdminNewUserHandler(tornado.web.RequestHandler):
    """
    add new user
    """
    def get(self):
        orgs = selectData("orgs", "name")
        self.render("admin_newuser.html", orgs=orgs)
    
    def post(self):
        """
        get the data from before web page.
        """
        user_mobilephone = self.get_argument("mobilephone")
        user_name = self.get_argument("username")
        user_password = self.get_argument("password")
        user_org = self.get_argument("org")
        user_starttime = self.get_argument("starttime")
        user_endtime = self.get_argument("endtime")
        print user_mobilephone
        
        result = selectDataWhere("users", "id", mobilephone=user_mobilephone)
        if result:
            self.write("-1")
        else:
            orgname_id = selectDataWhere("orgs", "id", name=user_org)[0][0]
            try:
                insertData("users", username=user_mobilephone, mobilephone=user_mobilephone, name=user_name, orgnameID=orgname_id, password=user_password, starttime=user_starttime, endtime=user_endtime, status=1)
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


class AdminDispUserHandler(tornado.web.RequestHandler):
    """
    list the information of the user. 
    """
    def get(self):
        user_id = self.get_argument("id")
        user_info = selectDataWhere("users", "mobilephone", "name", "orgnameID", "status", "starttime", "endtime", id=user_id)
        org_id = user_info[0][2]
        org_name = selectDataWhere("orgs", "name", id=org_id)
        org_name = org_name[0][0]
        self.render("admin_dispuser.html", userinfo=user_info[0], orgname=org_name, userid=user_id)
