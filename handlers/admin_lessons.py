#!/usr/bin/env python
# coding=utf-8

import tornado.web
import datetime

from dbmethod import *

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class AdminLessonHandler(tornado.web.RequestHandler):
    """
    the list of lessons, you can add new, delete, set time and so on.
    """
    def get(self):
        """
        display the webpage, list all of the courses.
        """
        lessons_info = selectData("lessons", "lessonname", "courseID", "setuptime", "id")
        courseids = [i[1] for i in lessons_info]
        coursenames = [selectDataWhere("courses", "coursename", id=i)[0][0] for i in courseids]
        coursenames.reverse()
        lessons_info_reverse = lessons_info[::-1] 
        self.render("admin_lessons.html", lessons=lessons_info_reverse, courses=coursenames)

    def post(self):
        """
        delete the course.
        """
        course_id = self.get_argument("id")
        
        if deleteLine("courses", id=course_id):
            self.write("1")
        else:
            self.write("0")

class AdminNewLessonHandler(tornado.web.RequestHandler):
    """
    add new lesson.
    """
    def get(self):
        """
        list the form of add new video.
        """
        courses = selectData("courses", "coursename", "id")
        self.render("admin_newlesson.html", courses=courses)
    
    def post(self):
        """
        get the data from before web page.
        """
        course_name = self.get_argument("coursename")
        teacher_name = self.get_argument("teachername")
        about_teacher = self.get_argument("aboutteacher")
        
        result = selectDataWhere("courses", "id", coursename=course_name)
        if result:
            self.write("-1")
        else:
            try:
                insertData("courses", coursename=course_name, teachername=teacher_name, aboutteacher=about_teacher, status=0, setuptime=datetime.date.today(), countlessons=0)
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


class AdminDispCourseHandler(tornado.web.RequestHandler):
    """
    list the information of the course. 
    """
    def get(self):
        """
        display the information of the course.
        """
        course_id = self.get_argument("id")
        course_info = selectDataWhere("courses", "coursename", "teachername", "aboutteacher", "status", "setuptime", "countlessons", id=course_id)

        self.render("admin_dispcourse.html", courseinfo=course_info[0], id=course_id)

    def post(self):
        """
        set the couse on line.
        """
        course_id = int(self.get_argument("id"))
        course_status = int(self.get_argument("status"))
        updatething = {"status": course_status}
        condition = {"id": course_id}
        try:
            updateLineWhere("courses", updatething, condition)
            self.write("1")
        except:
            self.write('0')
