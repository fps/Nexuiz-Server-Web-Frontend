#!/usr/bin/env python 
# coding: utf8 
from gluon.html import *
from gluon.http import *
from gluon.validators import *
from gluon.sqlhtml import *
from gluon.sql import *
# request, response, session, cache, T, db(s) 
# must be passed and cannot be imported!

from subprocess import Popen
from subprocess import PIPE
import re

def value(db, key):
    query = db.server_setup.key==key
    set = db(query)
    records = set.select()

    return records[0].value
 

def rcon(msg): 
    db = DAL('sqlite://storage.sqlite')
    db.define_table('server_setup', Field('key', 'string'), Field('value', 'string'))

    host = value(db, 'host')
    rcon_password = value(db, 'rcon_password')
    rcon_script = value(db, 'rcon_script')
    
    p = Popen(bufsize=100000, args=[rcon_script, msg], env={"rcon_address":host, "rcon_password":rcon_password, "rcon_colorcodes_raw":"1", "rcon_timeout":"10", "rcon_timeout_inter":"3", "rcon_timeout_challenge":"10"}, stdout=PIPE)
    
    answer = p.stdout.read()
    
    #for line in p.stdout:
    #    answer = answer + line
    #return answer
    
    regex = re.compile("\\^[0-9]", re.UNICODE)
    regex2 = re.compile("\\^x[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]", re.UNICODE)
    return regex2.sub('', regex.sub('', answer))
    #return "bla"
