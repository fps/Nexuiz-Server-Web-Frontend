# coding: utf8
# try something like
from subprocess import Popen
from subprocess import PIPE
import re

import applications.nexuiz_server.modules.rcon as rcon
#import applications.nexuiz_server.controllers.default as default

def setup():
    return dict()

def data_management():
    return dict(files=["bla.pk3", "blub.pk3", "foobar.pk3"])

def restart_map(): 
    response.flash = T('Restart Map')
    rcon.rcon("restart")
    return dict(message="Map restarted")

def restart_map_request():
    session.alert_message = "Restart current map"
    session.alert_yes_action = ["server", "restart_map"]
    session.alert_no_action = ["default", "index"]
    redirect(URL(r=request, c="default", f="confirmation"))   
    return dict()

def status(): 
    response.flash = T('Server Status')
    return dict(message=rcon.rcon("status"))

def console():
    response.flash = T('Server Console')
    if session.log == None:
        session.log = ""
        
    max_log_size = 16384
    if request.vars.command:
        session.log = "" or rcon.rcon(request.vars.command) + "\n-----------\n" + session.log
        if len(session.log) > max_log_size:
            session.log = session.log[0:max_log_size]
        
    return dict()

def upload():
    pass
