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

url=[
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r"/org", AdminOrgHandler),
    (r'/neworg', AdminNewOrgHandler),
    (r'/editorg', AdminEditOrgHandler),
    ]
