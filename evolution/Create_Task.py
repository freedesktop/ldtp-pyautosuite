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

#log('Verify-a-Creat_task','teststart')

#reading args from the file
file = open('create_task.dat', 'r')
argmts = file.readlines()
txtsummary = argmts[0].strip( )
txtsetcontext = argmts[1].strip( )
txtclassification = argmts[2].strip( )
txtgroup = argmts[3].strip  # txtgroup var has preceeding white spaces in appmap and if we strip it loses the preceeding white spaces 
txtdescription = argmts[4].strip( ) 
txtduedate = argmts[5].strip( ) 
txtstartdate = argmts[6].strip( )
txtpriority = argmts[7].strip( )
txtcategory = argmts[8].strip( )
status = argmts[9].strip( )
datecompleted=argmts[10].strip( )
num=argmts[11].strip( )
s1 ='Unable to get gui handle'
#Function to implement task_create()

def task_create():
    try:
        selectmenuitem('Evolution-Tasks','mnuFile;mnuNew;mnuTask')
        selecttab ('dlgTask-Nosummary','ptlTask-No summary', '0')
        settextvalue ('dlgTask-Nosummary', 'txtSummry', txtsummary)
        setcontext ('Task - No summary', txtsetcontext)
        wait(5)
        comboselect ('dlgTask-Nosummary', 'cmbClassfication',txtclassification)
        comboselect ('dlgTask-Nosummary', 'cmbGroup','    Personal')
        click ('dlgTask-Nosummary','btnCategories')
        settextvalue ('dlgCategories', 'txtItem', txtcategory)
        click ('dlgCategories','btnOK')    
        settextvalue ( 'dlgTask-Nosummary', 'txtDescription', txtdescription)
        settextvalue ( 'dlgTask-Nosummary','txtdueDate',txtduedate)
        settextvalue ( 'dlgTask-Nosummary','txtstartDate',txtstartdate)
        selecttab ('dlgTask-Nosummary','ptlTask-No summary', '1')
 	comboselect ( 'dlgTask-Nosummary','cmbStatus', status)
        comboselect ( 'dlgTask-Nosummary','cmbPriority', txtpriority)
	setvalue('dlgTask-Nosummary','sbtnPercentcomplete',num)
	settextvalue (  'dlgTask-Nosummary','txtTextDateEntry',datecompleted)
        click ('dlgTask-Nosummary','btnOK')
    except error,msg:
			if string.find(str(msg),s1)== -1:
				print "File not found(nt cz of gui handle)...so  stilll continuing"	
			print "--File  nt found..bt  stilll continuing"
    releasecontext (txtsetcontext, 'Task - No summary')



###Verify task creation function

def verify_create_task ():
    try:
	log('verify-the-task','pass')
        #click ('Evolution-Tasks', 'togbtnTask')
	selectmenuitem('Evolution-Tasks','mnuView;mnuWindow;mnuTasks')
	wait(5)
        selectlastrow('Evolution-Tasks', 'tblTasks')
        selectmenuitem('Evolution-Tasks','mnuFile;mnuOpenTask')
        setcontext ('Task - No summary',txtsetcontext)
	selecttab('dlgTask-Nosummary','ptlTask-No summary', '0')
	log('verifies-summary','pass')
        verifysettext ('dlgTask-Nosummary', 'txtSummry', txtsummary)
        verifyselect ('dlgTask-Nosummary', 'cmbClassfication',txtclassification)
        verifyselect ('dlgTask-Nosummary', 'cmbGroup', '    Personal')
        verifysettext ('dlgTask-Nosummary', 'txtCategories', txtcategory)
	log('verifies-description','pass')
        verifysettext ('dlgTask-Nosummary', 'txtDescription', txtdescription)
        verifysettext ( 'dlgTask-Nosummary','txtdueDate',txtduedate)
        verifysettext ( 'dlgTask-Nosummary','txtstartDate',txtstartdate)
        selecttab ('dlgTask-Nosummary', 'ptlTask-No summary', '1')
	verifysetvalue('dlgTask-Nosummary','sbtnPercentcomplete','70')
        click ('dlgTask-Nosummary','btnCancel')

    except error,msg:
		if string.find(str(msg),s1)== -1:
				print "File not found(nt cz of gui handle)...so  stilll continuing"	
			        print "--File  nt found..bt  stilll continuing"
    

#calling the Task verify function
log('create-the-task','teststart')
task_create()
log('create-the-task','testend')
verify_create_task()

