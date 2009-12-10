# coding: utf8

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('A simple server control frontend for nexuiz')

##########################################
## this is the authentication menu
## remove if not necessary
##########################################

if 'auth' in globals():
    if not auth.is_logged_in():
       response.menu_auth = [
           [T('Login'), False, auth.settings.login_url,
            [
                   [T('Register'), False,
                    URL(request.application,'default','user/register')],
                   [T('Lost Password'), False,
                    URL(request.application,'default','user/retrieve_password')]]
            ],
           ]
    else:
        response.menu_auth = [
            ['User: '+auth.user.first_name,False,None,
             [
                    [T('Logout'), False, 
                     URL(request.application,'default','user/logout')],
                    [T('Edit Profile'), False, 
                     URL(request.application,'default','user/profile')],
                    [T('Change Password'), False,
                     URL(request.application,'default','user/change_password')]]
             ],
            ]

##########################################
## this is the main application menu
## add/remove items as required
##########################################
if 'auth' in globals():
    if auth.is_logged_in():
        response.menu = [
            [T('Index'), False, 
             URL(request.application,'default','index'), []],
            [T('Server Setup'), False, 
             URL(request.application,'server','setup'), []],
            [T('Server Status'), False, 
             URL(request.application,'server','status'), []],
            [T('Server Console'), False, 
             URL(request.application,'server','console'), []],
            [T('Server One Click Actions'), False, 
             URL(request.application,'server','one_click_actions'), []],
            [T('Server Data Management'), False, 
             URL(request.application,'server','data_management'), []],
            [T('Restart Map'), False, 
             URL(request.application,'server','restart_map_request'), []],
            ]
