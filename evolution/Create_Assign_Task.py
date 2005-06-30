#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Sheetal <svnayak18@yahoo.com>
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

# To create a assigned task
#reading args from the file
file = open('Create_Assign_Task.dat', 'r')
argmts = file.readlines()
txtsummary = argmts[0].strip( )
txtsetcontext = argmts[1].strip( )
txtclassification = argmts[2].strip( )
#txtgroup = argmts[3].strip 
txtdescription = argmts[4].strip( ) 
txtduedate = argmts[5].strip( ) 
txtstartdate = argmts[6].strip( )
txtpriority = argmts[7].strip( )
txtcategory = argmts[8].strip( )
status = argmts[9].strip( )
datecompleted=argmts[10].strip( )
num=argmts[11].strip( )
attendees=argmts[12].strip( )
search=argmts[13].strip( )
s1 ='Unable to get gui handle'

### U will have one section with diff value for classification.
#calls='Private'

###Function to implement assign_task_create()

def assign_task_create():
    try :
	
        selectmenuitem('Evolution-Tasks','mnuFile;mnuNew;mnuAssignedTask')
	wait(3)
        selecttab('dlgAssignedTask-Nosummary','ptlAssigned Task - No summary', '0')
        settextvalue ( 'dlgAssignedTask-Nosummary', 'txtSummary', txtsummary)
        setcontext ('Assigned Task - No summary', txtsetcontext)
        wait(5)
        comboselect ('dlgAssignedTask-Nosummary', 'cmbClassfication',txtclassification)
        comboselect ('dlgAssignedTask-Nosummary', 'cmbGroup', '    Personal')
        click ('dlgAssignedTask-Nosummary','btnCategories')
        #selectrow('dlgCategories', 'tblCategories', txtcategory)
        settextvalue ('dlgCategories', 'txtItem', txtcategory)
        click ('dlgCategories','btnOK')    
        settextvalue ( 'dlgAssignedTask-Nosummary', 'txtTaskDescription', txtdescription)
        settextvalue ( 'dlgAssignedTask-Nosummary','txtdueDate',txtduedate)
        settextvalue ( 'dlgAssignedTask-Nosummary','txtstartDate',txtstartdate)
        selecttab ('dlgAssignedTask-Nosummary','ptlAssigned Task - No summary', '1')
	comboselect ('dlgAssignedTask-Nosummary','cmbStatus', status)
        comboselect ('dlgAssignedTask-Nosummary','cmbPriority', txtpriority)
	setvalue('dlgAssignedTask-Nosummary','sbtnPercent',num)
	settextvalue ( 'dlgAssignedTask-Nosummary','txtTextDateEntry',datecompleted)
        selecttab ('dlgAssignedTask-Nosummary','ptlAssigned Task - No summary', '2')
	selectrowindex('dlgAssignedTask-Nosummary','tblAttendees',0)
	#click ('dlgAssignedTask-Nosummary','btnRemove')
	click ('dlgAssignedTask-Nosummary','btnOK')
        click ('dlgEvolutionQuery','btnSend')
    except error,msg:
			if string.find(str(msg),s1)== -1:
				print "File not found(nt cz of gui handle)...so  stilll continuing"	
			print "--File  nt found..bt  stilll continuing"
        #releasecontext (txtsetcontext, 'Assigned Task - No summary')
def verify_assign_task ():
    try:
	log('verify-the-task','pass')
        #click ('Evolution-Tasks', 'togbtnTask')
	wait(5)
	selectmenuitem('Evolution-Tasks','mnuView;mnuWindow;mnuTasks')
	wait(5)
        selectlastrow('Evolution-Tasks', 'tblTasks')
        selectmenuitem('Evolution-Tasks','mnuFile;mnuOpenTask')
        setcontext ('Assigned Task - No summary',txtsetcontext)
	selecttab('dlgAssignedTask-Nosummary','ptlAssigned Task - No summary', '0')
	log('verifies-summary','pass')
        verifysettext ('dlgAssignedTask-Nosummary', 'txtSummary', txtsummary)
        verifyselect ('dlgAssignedTask-Nosummary', 'cmbClassfication',txtclassification)
        verifysettext ('dlgAssignedTask-Nosummary', 'txtCategories', txtcategory)
	log('verifies-description','pass')
        verifysettext ('dlgAssignedTask-Nosummary', 'txtTaskDescription', txtdescription)
        verifysettext ( 'dlgAssignedTask-Nosummary','txtdueDate',txtduedate)
        verifysettext ( 'dlgAssignedTask-Nosummary','txtstartDate',txtstartdate)
        selecttab ('dlgAssignedTask-Nosummary', 'ptlAssigned Task - No summary', '1')
	verifysetvalue('dlgAssignedTask-Nosummary','sbtnPercent','70')
        click ('dlgAssignedTask-Nosummary','btnCancel')

    except error,msg:
			if string.find(str(msg),s1)== -1:
				print "File not found(nt cz of gui handle)...so  stilll continuing"	
			print "--File  nt found..bt  stilll continuing"
    



### Functions End


## Calling the function 
#summary = "Task Poornima"
log('create-the-assgned-meeting','teststart')
assign_task_create()
verify_assign_task ()
log('create-the-assgned-meeting','testend')
