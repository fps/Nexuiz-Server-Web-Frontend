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

def rcon(msg): 
    db = DAL('sqlite://storage.sqlite')
    db.define_table('server_setup', Field('key', 'string'), Field('value', 'string'))

    query = db.server_setup.key=='host'
    set = db(query)
    records = set.select()

    host = records[0].value
    
    query = db.server_setup.key=='rcon_password'
    set = db(query)
    records = set.select()
    
    rcon_password = records[0].value
    
    p = Popen(bufsize=100000, args=["/home/tapas/local/bin/rcon.pl", msg], env={"rcon_address":host, "rcon_password":rcon_password, "rcon_colorcodes_raw":"1", "rcon_timeout":"10", "rcon_timeout_inter":"3", "rcon_timeout_challenge":"10"}, stdout=PIPE)
    
    answer = p.stdout.read()
    
    #for line in p.stdout:
    #    answer = answer + line
    #return answer
    
    regex = re.compile("\\^[0-9]", re.UNICODE)
    regex2 = re.compile("\\^x[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]", re.UNICODE)
    return regex2.sub('', regex.sub('', answer))
    #return "bla"
