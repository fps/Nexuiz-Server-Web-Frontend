# coding: utf8
# try something like

import applications.nexuiz_server.modules.rcon as rcon

@auth.requires_login()
def one_click_actions():
    response.flash = T('One Click Actions')
    rows = db().select(db.one_click_actions.ALL)
    inputs = []
    for row in rows:
        new_input = INPUT(_type="button", _value=row.name);
        if new_input.accepts(request_vars):
            pass
        
        inputs.append([new_input, row.command, row.helptext])
        
    return dict(rows=rows, inputs=inputs)

@auth.requires_login()
def setup():
    response.flash = T('Server Setup')

    db.server_setup.key.requires=IS_NOT_EMPTY()
    db.server_setup.value.requires=IS_NOT_EMPTY()
    
    rows = db().select(db.server_setup.ALL)

    sqlrows=[]
    for row in rows:
        newform = SQLFORM(db.server_setup, row, deletable=True, linkto="server/setup_submit")
        if newform.accepts(request.vars):
            session.flash="Submitted new key/value pair"
            redirect(URL(r=request, f='setup'))
        sqlrows.append(newform)

    form = SQLFORM(db.server_setup)
    
    if form.accepts(request.vars):
        response.flash="Submitted new key/value pair"
        redirect(URL(r=request, f='setup'))
        
    return dict(rows=sqlrows, form=form)


@auth.requires_login()
def data_management():
    response.flash = T('Server Data Management')
    return dict(files=["bla.pk3", "blub.pk3", "foobar.pk3"])

@auth.requires_login()
def restart_map(): 
    response.flash = T('Restart Map')
    try: 
        rcon.rcon("restart")
    except:
        return dict(message="rcon failed. check the server setup")
    
    return dict(message="Map restarted")

@auth.requires_login()
def restart_map_request():
    session.alert_message = "Restart current map"
    session.alert_yes_action = ["server", "restart_map"]
    session.alert_no_action = ["default", "index"]
    redirect(URL(r=request, c="default", f="confirmation"))   
    return dict()

@auth.requires_login()
def status(): 
    response.flash = T('Server Status')
    try:
        status = rcon.rcon("status")
    except:
        return dict(message="rcon failed. check the server setup")

    return dict(message=status)

@auth.requires_login()
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

@auth.requires_login()
def upload():
    response.headers['content-type'] = 'text/xml'
    #file = request.body.read() 
    filename = request.post_vars['filename'].filename
    file = request.post_vars['filename'].file
    
    postfile = file.read()

    f = open(filename, "w")
    f.write(postfile)

    return dict(filename=filename, success='succeeded')
