from ldtp import *
from ldtputils import *
from contact import *
from evoutils import *
from evoutils.calendar import get_date_format


def gettaskdata(datafilename):
    data_object = LdtpDataFileParser (datafilename)
    Group = data_object.gettagvalue ('group')
    Summary = data_object.gettagvalue ('summary')
    Desc = data_object.gettagvalue ('desc')
    Start_date = data_object.gettagvalue ('start_date')
    Start_time = data_object.gettagvalue ('start_time')
    End_date = data_object.gettagvalue ('end_date')
    End_time = data_object.gettagvalue ('end_time')
    Time_zone = data_object.gettagvalue ('time_zone')
    Categories = data_object.gettagvalue ('Categories')
    return Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories


def fill_task (Group, Summary, Desc, Start_date, Start_time, End_date, End_time, Time_zone, Categories, window_id = 'frmTask-*'):
    try:
#         for obj in getobjectlist ('frmTask-*'):
#             if obj.startswith ('cbo'):
#                 grp_obj = obj
#                 break
        grp_obj = 'cboPersonal'
        if Group:
            comboselect (window_id, grp_obj, Group[0])
            time.sleep(3)
        settextvalue (window_id, 'txtSummary', Summary[0])
        if Desc:
            settextvalue (window_id, 'txtDescription', Desc[0])
        if Start_date:
            settextvalue (window_id, 'txtDate1',Start_date[0])
        if End_date:
            settextvalue (window_id, 'txtDate',End_date[0])
        if Start_time:
            settextvalue (window_id, 'txt8',Start_time[0])
        if End_time:
            settextvalue (window_id, 'txt6',End_time[0])
        #if Time_zone:
        #	menucheck (window_id,'mnuView;mnuTimeZone')
        #	settextvalue (window_id, 'txt4',Time_zone[0])
        #else:
        menuuncheck (window_id,'mnuView;mnuTimeZone')
        if Categories:
            menucheck (window_id,'mnuView;mnuCategories')
            settextvalue (window_id, 'txt0',Categories[0])
        else:
            menuuncheck (window_id,'mnuView;mnuCategories')
            log('User Details entered','info')
    except:
        print 'Error in entering the values'
        log('Error in entering the values','error')
        raise LdtpExecutionError(0)

    
def verify_task (Group, Summary, Desc, Start_date, Start_time, End_date,
		 End_time, Time_zone, Categories, windowname='frmTask-*'):
    try:
        selectmenuitem ('frmEvolution-Tasks','mnuFile;mnuOpenTask');
        if waittillguiexist (windowname) == 0:
            log ('Unable to open Task','cause')
            raise LdtpExecutionError (0)
        
        if Desc and verifysettext (windowname, 'txtDescription', Desc[0]) == 0:
            log ('Description not set','cause')
            raise LdtpExecutionError (0)
        
        # 		if Start_date and verifysettext (windowname, 'txtDate1',get_date_format(Start_date[0])) == 0:
        # 			log ('Start Date set incorrectly','cause')
        # 			raise LdtpExecutionError (0)
        # 		if End_date and verifysettext (windowname, 'txtDate',get_date_format(End_date[0])) == 0:
        # 			log ('End date set incorrectly','cause')
        # 			raise LdtpExecutionError (0)
        
        if Start_time and verifysettext (windowname, 'txt8',Start_time[0]) == 0:
            log ('Start time set incorrectly','cause')
            raise LdtpExecutionError (0)
        
        if End_time and verifysettext (windowname, 'txt6',End_time[0]) == 0:
            log ('End time set incorrectly','cause')
            raise LdtpExecutionError (0)
        
        # 		if Time_zone and verifysettext (windowname, 'txt4',Time_zone[0]) == 0:
        # 			log ('Time Zone set incorrecly','cause')
        # 			raise LdtpExecutionError (0)
        
        if Categories and verifysettext (windowname, 'txt0',Categories[0]) == 0:
            log ('Categories set incorrectly','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Task Verification failed','error')
        raise LdtpExecutionError (0)
			


def read_assignedtask_data (datafilename):
   try:
      data_object = LdtpDataFileParser (datafilename)
      index = 1
      attendee = []
      email = []
      while True:
         att = data_object.gettagvalue ('attendee'+str(index))
         em = data_object.gettagvalue ('email'+str(index))
         
         if att == []  or em == []:
            break
         attendee.append (att[0])
         email.append (em[0])
         index += 1
      addr_book = data_object.gettagvalue ('addr_book')
      Group = data_object.gettagvalue ('group')
      Summary = data_object.gettagvalue ('summary')
      Desc = data_object.gettagvalue ('Desc')
      Start_date = data_object.gettagvalue ('start_date')
      Start_time = data_object.gettagvalue ('start_time')
      End_date = data_object.gettagvalue ('due_date')
      End_time = data_object.gettagvalue ('due_time')
      Time_zone = data_object.gettagvalue ('time_zone')
      Categories = data_object.gettagvalue ('Categories')
      print Group, Summary, Desc, Start_date, Start_time, \
            End_date, End_time, Time_zone, Categories, attendee, email
      return Group, Summary, Desc, Start_date, Start_time, \
             End_date, End_time, Time_zone, Categories, addr_book, attendee, email

   except:
      log('Unable to read the user data or data file missing','error')
      raise LdtpExecutionError (0)
