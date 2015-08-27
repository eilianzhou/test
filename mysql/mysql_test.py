#-*- coding:utf-8 -*-

import sys
import os
import time
import traceback

def test_sql():
   import MySQLdb
   dbname = "BOfYGEsvNiVxxfIUdNPh"
   api_key = "fZyKjZKkc9QXbQGgwHuLXQ2x"
   secret_key = "SjMbCfoSajp4ANrBuAtpFM8Aw4Tn2uoN"

   mydb = MySQLdb.connect(
           host   = "sqld.duapp.com",
           port   = 4050,
           user   = api_key,
           passwd = secret_key,
           db = dbname)

   cursor = mydb.cursor()

   cmd = '''CREATE TABLE IF NOT EXISTS test (
         id int(4) auto_increment,
         name char(20) not null,
         age int(2),
         sex char(8) default 'man',
         primary key (id))'''

   cursor.execute(cmd)

   mydb.close()
   return 'create table test success!'

#--------------main-----------

#--------- user action begin -------------
try:
    test_sql()
except:
    print traceback.format_exc()
#--------- user action end -------------

'''
def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    #--------- user action begin -------------
    try:
        return test_sql()
    except:
        return 'handle exceptions'
    #--------- user action end -------------

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
'''
