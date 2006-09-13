
from ldtp import *
from ldtputils import *

def get_window (component=None):
	window_id = ''
        if guiexist ('frmEvolution-Calendars') == 1:
            	window_id = 'frmEvolution-Calendars'
        elif guiexist ('frmEvolution-Tasks') == 1:
            	window_id = 'frmEvolution-Tasks'
        elif guiexist ('frmEvolution-Contacts') == 1:
            	window_id = 'frmEvolution-Contacts'
	elif guiexist ('frmEvolution-Memos') == 1:
            	window_id = 'frmEvolution-Memos'
	elif guiexist ('frmEvolution-*') == 1:
            	window_id = 'frmEvolution-*'
	if component:
		if window_id:
                        click (window_id, str('tbtn'+ component))
			time.sleep (3)
			return 1
		else:	
			return 0
	else:
		return window_id

def selectContactPane():
    """Selects the Contacts Pane in Evolution"""
    try:
         window_id=get_window()
         click (window_id,'tbtnContacts')
         waittillguiexist ('frmEvolution-Contacts')
    except:
        log ('error selecting Contacts pane','error')
        raise LdtpExecutionError(0)
    
def selectMailPane():
    """Selects the Contacts Pane in Evolution"""
    try:
         window_id = get_window()
         click (window_id,'tbtnMail')
         time.sleep (2)
    except:
        log ('error selecting Mail pane','error')
        raise LdtpExecutionError(0)

def selectContactPane():
    """Selects the Contacts Pane in Evolution"""
    try:
         window_id=get_window()
         click (window_id,'tbtnContacts')
         waittillguiexist ('frmEvolution-Contacts')
    except:
        log ('error selecting Contacts pane','error')
        raise LdtpExecutionError(0)
    

def selectMemoPane():
    """Selects the Calendars Pane in Evolution"""
    try:
         window_id=get_window()
         click (window_id,'tbtnMemos')
         waittillguiexist ('frmEvolution-Memos')
    except:
        log ('error selecting Memos pane','error')
        raise LdtpExecutionError(0)
    

def selectTaskPane():
    """Selects the Contacts Pane in Evolution"""
    try:
         window_id = get_window()
         click (window_id,'tbtnTasks')
         waittillguiexist ('frmEvolution-Tasks')
    except:
        log ('error selecting Tasks pane','error')
        raise LdtpExecutionError(0)
    


def selectCalendarPane():
    """Selects the Contacts Pane in Evolution"""
    try:
         window_id = get_window()
         click (window_id,'tbtnCalendars')
         waittillguiexist ('frmEvolution-Calendars')
    except:
        log ('error selecting Calendars pane','error')
        raise LdtpExecutionError(0)


def go_offline():
    time.sleep (10)
    remap ('evolution','frmEvolution-*')
    try:
        window_id = 'frmEvolution-*'
        flag=False
	if 'mnuWorkOffline' in getobjectlist(window_id):
	    flag=True
        if flag==True:
            selectmenuitem (window_id,'mnuFile;mnuWorkOffline')
            log ('going offline','info')
        else:
            log ('already offline','info')
            return
        time.sleep (3)
#         remap ('evolution','frmEvolution-*')
# 	time.sleep (1)
#         flag=False
# 	if 'mnuWorkOnline' in getobjectlist (window_id):
#	    flag = True
#         for x in getobjectlist (window_id):
#             if x == 'mnuWorkOnline':
#                 flag=True
#                 break
        if flag == False:
            log ('Work Online not available','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Could not go offline','error')
        raise LdtpExecutionError (0)


def go_online ():
    time.sleep (10)
    remap ('evolution','frmEvolution-*')
    try:
        window_id = 'frmEvolution-*'
        flag=False
        if 'mnuWorkOnline' in getobjectlist(window_id):
	    flag=True

        if flag == True:
            selectmenuitem (window_id,'mnuFile;mnuWorkOnline')
            log ('going online','info')
        else:
            log ('already online','info')
            return
        time.sleep (3)
        remap ('evolution','frmEvolution-*')
	
	time.sleep (1)
#        flag=False
# 	if 'mnuWorkOffline' in getobjectlist (window_id):
# 	    flag = True
#         for x in getobjectlist (window_id):
#             if x == 'mnuWorkOffline':
#                 flag=True
#                 break
        if flag == False:
            log ('Work Offline not available','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Could not go Online','error')
        raise LdtpExecutionError (0)


def get_mail_name (subject):
    if subject == '':
        return '*ComposeMessage*'
    else:
	return '*'+subject.replace(' ','')

def restartevolution():
    log ('Restart Evolution','teststart')
    try:
        time.sleep (3)
        window_id = 'frmEvolution-*'
        remap ('evolution',window_id)
        selectmenuitem (window_id,'mnuFile;mnuQuit')
        waittillguinotexist (window_id)
        undoremap ('evolution',window_id)
        time.sleep (2)
        launchapp ('evolution',1)
        time.sleep (2)
        if guiexist (window_id) == 1:
            log ('Evolution Restarted successfully','info')
        else:
            log ('Evolution window not open','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Restart evolution failed','error')
        log ('Restart Evolution','testend')
        raise LdtpExecutionError (0)
    log ('Restart Evolution','testend')

def select_mail(fldr,subject):
    try:
	if selectrowpartialmatch('frmEvolution-*','ttblMailFolderTree',fldr) == 1:
	    waittillguiexist ('frmEvolution-'+fldr+'*')
	    log('Folder selected','info')
	    if selectrow('frmEvolution-*','ttblMessages',subject) == 1:
	        log('Mail selected','info')
		#undoremap('evolution','frmEvolution-Mail')
		#log('select mail in a folder','testend')
		return 1
	    else:
		log('Unable to select the mail','error')
		#undoremap('evolution','frmEvolution-Mail')
		#log('select mail in a folder','testend')
		return 0
    except:
	log('Folder not found','cause')
	#log('select mail in a folder','testend')
	raise LdtpExecutionError (0)

