#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handlers.index import IndexHandler
from handlers.login import LoginHandler
from handlers.admin_orgs import AdminOrgHandler
from handlers.admin_orgs import AdminNewOrgHandler
from handlers.admin_orgs import AdminEditOrgHandler
from handlers.admin_orgs import AdminReadOrgHandler

from handlers.admin_users import AdminUserHandler
from handlers.admin_users import AdminNewUserHandler
from handlers.admin_users import AdminDispUserHandler

from handlers.admin_courses import AdminCourseHandler
from handlers.admin_courses import AdminNewCourseHandler
from handlers.admin_courses import AdminDispCourseHandler

from handlers.admin_lessons import AdminLessonHandler
from handlers.admin_lessons import AdminNewLessonHandler


url=[
    (r'/', IndexHandler),                    # the index page
    (r'/login', LoginHandler),               # the administrator login into the web
    (r"/org", AdminOrgHandler),              # the list of org
    (r'/neworg', AdminNewOrgHandler),        # add a new org
    (r'/editorg', AdminEditOrgHandler),      # edit an org
    (r'/readorg', AdminReadOrgHandler),      # list an org

    (r'/user', AdminUserHandler),            # the list of users
    (r'/newuser', AdminNewUserHandler),        # add a new user
    (r'/dispuser', AdminDispUserHandler),    # display the all information of the user.

    (r'/course', AdminCourseHandler),        # the list of courses.
    (r'/newcourse', AdminNewCourseHandler),  # add a new course.
    (r'/dispcourse', AdminDispCourseHandler), #display the all information of the course
    
    (r'/lesson', AdminLessonHandler),        # the list of lessons.
    (r'/newlesson', AdminNewLessonHandler),  # add a new lesson.
    ]
