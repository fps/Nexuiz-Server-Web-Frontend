#!/usr/bin/env python 
# coding: utf8 
from gluon.html import *
from gluon.http import *
from gluon.validators import *
from gluon.sqlhtml import *
# request, response, session, cache, T, db(s) 
# must be passed and cannot be imported!

from subprocess import Popen
from subprocess import PIPE
import re

def rcon(msg): 
    answer = "";
    p = Popen(bufsize=100000, args=["/home/tapas/local/bin/rcon.pl", msg], env={"rcon_address":"host:port", "rcon_password":"****", "rcon_colorcodes_raw":"1", "rcon_timeout":"30", "rcon_timeout_inter":"3", "rcon_timeout_challenge":"30"}, stdout=PIPE)
    answer = p.stdout.read()
    #for line in p.stdout:
    #    answer = answer + line
    #return answer
    regex = re.compile("\\^[0-9]", re.UNICODE)
    regex2 = re.compile("\\^x[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]", re.UNICODE)
    return regex2.sub('', regex.sub('', answer))
