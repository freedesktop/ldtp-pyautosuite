#!/usr/bin/python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Prashanth Mohan <prashmohan@gmail.com>
#     Khasim Shaheed <khasim.shaheed@gmail.com>
#
#  Copyright 2004 Novell, Inc.
#
#  This test script is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Library General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Library General Public License for more details.
#
#  You should have received a copy of the GNU Library General Public
#  License along with this library; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#



import time, re

from ldtp import *
from ldtputils import *
from evoutils import *

# Section to perform search for mail based on above search condition
def search (search_type, search_folder, search_text):
# Search for mail based on one of the following search conditions
# a) Subject or Sender contains 
# b) Subject contains
# c) Sender contains
	try:
		selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', search_folder)
		waittillguiexist ('frmEvolution-'+search_folder+'*')
		time.sleep (2)
		search_mail_count = 0
		total_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
		
		print 'Counting the number of mails which satisfy the condition...'
		regexp = re.compile (re.escape (search_text), re.I)

		if (search_type == 'Subject or Sender contains'):
			for i in range (total_mail_count):
				subject = getcellvalue ('frmEvolution-*', 'ttblMessages', i, 4)
				sender = getcellvalue ('frmEvolution-*', 'ttblMessages', i, 3)
				if (regexp.search (subject) or regexp.search (sender)):
					search_mail_count = search_mail_count + 1
		elif (search_type == 'Subject contains'):			
			for i in range (total_mail_count):
				subject = getcellvalue ('frmEvolution-*', 'ttblMessages', i, 4)
				if (regexp.search (subject)): 
					search_mail_count = search_mail_count + 1
		elif (search_type == 'Sender contains'):	
			for i in range (total_mail_count):
				sender = getcellvalue ('frmEvolution-*', 'ttblMessages', i, 3)
				if (regexp.search (sender)):
					search_mail_count = search_mail_count + 1
		else:
			log ('This type of search is not handled by this script', 'cause')
			log ('This type of search is not handled by this script', 'fail')
			return
		
		print '...done'
		comboselect ('frmEvolution-*', 'cboSearchType', search_type)
		settextvalue ('frmEvolution-*', 'txtSearch', search_text)
		click ('frmEvolution-*', 'btnFindNow')
		time.sleep (2)
		filter_mail_count = getrowcount ('frmEvolution-*', 'ttblMessages')
		click ('frmEvolution-*', 'btnClear')
		time.sleep (2)

		if search_mail_count == filter_mail_count:
			log ('Search based on ' + search_type + ' passed', 'pass')
		else:
			log ('Search based on ' + search_type + ' failed', 'cause')
			log ('Search based on ' + search_type + ' failed', 'fail')
			
	except ldtp.error, msg:
		log ('Search based on ' + search_type + ' failed '+ str (msg), 'cause')
		log ('Search based on ' + search_type + ' failed', 'fail')
		raise LdtpExecutionError (0)
			

def set_query (field, query, value, window_id='dlgAdvancedSearch'):
    remap ('evolution',window_id)
    obj_list = getobjectlist (window_id)
    sub_max = ''
    txt_max = '1'
    con_max = ''
    for obj in obj_list:
        if obj.startswith ('txt') and obj != 'txtSearchname':
            txt_max = obj
        elif obj.startswith ('cbo') and not obj.startswith ('cbospecific') and not obj.startswith ('cbowith'):
            if obj[3] < 'A' or obj[3] > 'Z':
                if obj > con_max:
                    con_max = obj
            else:
                if obj > sub_max:
                    sub_max = obj
    comboselect (window_id, sub_max, field)
    comboselect (window_id, con_max, query)
    settextvalue (window_id, txt_max, value)
                
    
def fill_search_box (dataobject, window_id='dlgAdvancedSearch'):
    index = 1
    constraint = []
    name = dataobject.gettagvalue ('name')
    settextvalue (window_id, 'txtSearchname', name[0])
    comboselect (window_id,'cboIfanycriteriaaremet','If any criteria are met')
    click (window_id, 'btnRemove1')
    while True:
        field = dataobject.gettagvalue ('field'+str(index))
        query = dataobject.gettagvalue ('query'+str(index))
        value = dataobject.gettagvalue ('value'+str(index))
        if field == [] or query == [] or value == []:
            break
        if index != 1:
            click (window_id, 'btnAdd')
        set_query (field[0], query[0], value[0], window_id)
        constraint.append ([field[0],query[0],value[0]])
        index += 1

    return constraint


def check (constraint, row):
    field = constraint [0]
    query = constraint [1]
    value = constraint [2]
    if field == 'Subject':
        col = 4
    elif field == 'Sender':
        col = 3
    elif field == 'Attachments':
        col = 1
    else:
        # cannot check. Assume correct
        return True

    val = getcellvalue ('frmEvolution-*','ttblMessages',row,col)

    if col == 1 and query == 'Exist':
        if val == 1:
            return True
        return False
    elif col == 1 and query == 'Do Not Exist':
        if val == 0:
            return True
        return False

    val = val.lower()
    value = value.lower()
    #regexp = re.compile (re.escape (search_text), re.I)
    if query == 'contains':
        if val.find (value) != -1:#regexp.search (value):
            return True
        return False
    elif query == 'does not contain':
        if not val.find (value) == -1:#regexp.search (value):
            return True
        return False
    elif query == 'is':
        if val == value:
            return True
        return False
    elif query == 'is not':
        if val != value:
            return True
        return False
    elif query == 'starts with':
        if val.startswith(value):
            return True
        return False
    elif query == 'does not start with':
        if not val.startswith(value):
            return True
        return False
    elif query == 'ends with':
        if val.endswith (value):
            return True
        return False
    elif query == 'does not end with':
        if not val.endswith (value):
            return True
        return False

    #query not support assume True
    return True
        

def check_constraints (constraint):
    total_count = getrowcount ('frmEvolution-*','ttblMessages')

    for val in range (total_count):
        print val
        for con in constraint:
            if check (con,val):
                continue
            return False
    return True


def advanced_search (dataobject):
    try:
        log ('Advanced Search','teststart')
        selectmenuitem ('frmEvolution-*','mnuSearch;mnuAdvancedSearch')
        waittillguiexist ('dlgAdvancedSearch')
        const = fill_search_box (dataobject,'dlgAdvancedSearch')
        click ('dlgAdvancedSearch', 'btnOK')
        waittillguinotexist ('dlgAdvancedSearch')
        #time.sleep (5)
        if check_constraints (const):
            click ('frmEvolution-*','btnClear')
            log ('Advanced Search','pass')

        else:
            click ('frmEvolution-*','btnClear')
            log ('Check failed','cause')
            raise LdtpExecutionError (0)
    except:
        log ('Advanced Search','fail')
        log ('Advanced Search','testend')
        raise LdtpExecutionError (0)
    log ('Advanced Search','testend')
        

def saved_search (dataobject):
    try:
        log ('Saved Search','teststart')
        selectmenuitem ('frmEvolution-*','mnuSearch;mnuSaveSearch')
        waittillguiexist ('dlgSaveSearch')
        
        objlist = getobjectlist ('frmEvolution-*')
        max_val = 0
        for obj in objlist:
            if obj.startswith ('mnu'):
                if obj[3] < '0' or obj[3] > '9':
                    continue
                if len(obj) != 4:
                    continue
                val = int (obj[3])
                if max_val < val:
                    max_val = val
        raw_input (str(max_val))
        const = fill_search_box (dataobject,'dlgSaveSearch')
        click ('dlgSaveSearch', 'btnOK')
        waittillguinotexist ('dlgSaveSearch')
        time.sleep (5)
        remap ('evolution','frmEvolution-*')
        selectmenuitem ('frmEvolution-*','mnuSearch;mnu'+str(max_val+1))
        time.sleep (5)
        if check_constraints (const):
            click ('frmEvolution-*','btnClear')
            log ('Saved Search','pass')
        else:
            click ('frmEvolution-*','btnClear')
            log ('Check failed','cause')
            raise LdtpExecutionError (0)
    except:
        click ('frmEvolution-*','btnClear')
        log ('Saved Search','fail')
        log ('Saved Search','testend')
        raise LdtpExecutionError (0)
    log ('Saved Search','testend')


def search_folder (dataobject):
    try:
        log ('Search Folder','teststart')
        name = dataobject.gettagvalue ('name')
        flag = False
        try:
            selectrow ('frmEvolution-*','ttblMailFolderTree',name[0])
        except:
            flag = True

        if flag:
            log ('A folder already exists with the same name','error')
            raise LdtpExecutionError (0)            

        selectmenuitem ('frmEvolution-*','mnuSearch;mnuCreateSearchFolderFromSearch')
        window_id = 'dlgNewSearchFolder'
        waittillguiexist (window_id)
        
        const = fill_search_box (dataobject,window_id)
        click (window_id, 'btnOK')
        time.sleep (2)
        if guiexist ('*EvolutionError*'):
            remap ('evolution','*EvolutionError*')
            click ('*EvolutionError*','btnOK')
            click (window_id, 'btnCancel')
            waittillguinotexist (window_id)
            log ('Search Already exists','cause')
            raise LdtpExecutionError (0)            
        
        waittillguinotexist (window_id)
        time.sleep (5)

        try:
            selectrow ('frmEvolution-*','ttblMailFolderTree',name[0])
        except:
            log ('Search Folder not available','cause')
            raise LdtpExecutionError (0)
        
        if check_constraints (const):
            click ('frmEvolution-*','btnClear')
            log ('Search Folder','pass')
        else:
            click ('frmEvolution-*','btnClear')
            log ('Check failed','cause')
            raise LdtpExecutionError (0)
    except:
        click ('frmEvolution-*','btnClear')
        log ('Search Folder','fail')
        log ('Search Folder','testend')
        raise LdtpExecutionError (0)
    time.sleep (8)
    log ('Search Folder','testend')
