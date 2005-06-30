#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Manu <manunature@rediffmail.com>
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

str1 = "Unable to get gui handle"
str2 = "Verify table cell failed"

#--Definition for Contact creation
def contact (data):
	listname = data[0].strip()
	try:
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuContactList')
		wait(3)
		comboselect ('dlgContactListEditor', 'cmbWhere', '    Personal')
		check ('dlgContactListEditor', 'chkHideaddresseswhensendingmailtothislist')
		settextvalue ('dlgContactListEditor', 'txtListname', listname)
		setcontext ("Contact List Editor", listname)
		
		for j in range (1, len(data)):
			settextvalue ('dlgContactListEditor', 'txtTypeanemailaddressordragacontactintothelistbelow', data[j].strip())
		  	click ('dlgContactListEditor','btnAdd')	
	        
		click ('dlgContactListEditor', 'btnSelect')
		settextvalue ('dlgContactListMembers','txtSearch',listname)

		if (doesrowexist ('dlgContactListMembers', 'tblContacts')):
		   selectrowindex ('dlgContactListMembers', 'tblContacts', 0)
		   click ('dlgContactListMembers', 'btnMembers')
		   click ('dlgContactListMembers', 'btnClose')
		else:
		   click('dlgContactListMembers','btnClose')

	        selectrowindex ('dlgContactListEditor', 'tblmail', 1)
		click ('dlgContactListEditor', 'btnRemove')
		click ('dlgContactListEditor', 'btnOk')
     		log ('ContactCreationPassed', 'pass')	    
     		
	except error, msg:
		if string.find (str(msg), str1) == -1:
		  print "Error!"
    		print "Creation Failing"
		log ('ContactCreationFailed','fail')	    
     
#--Definition for verifying contact	
def contactverify (data):
     MAX_PAN = 5
     row = 0
     col = 0	
     listname = data[0].strip ()	           	
     click ('Evolution-Mail', 'tbtnCont')
     wait (3)
     selectrowindex ('Evolution-Contacts', 'treetblml', 1)
     for pan in range (1, MAX_PAN):
        try:   
           #print 'pan:', pan
           selectpanel ('Evolution-Contacts', 'pnlAddbook', pan)
	   selectmenuitem ('Evolution-Contacts', 'mnuFile;mnuOpen')
	   setcontext ('Contact List Editor', listname)
           wait (1)
       	   verifysettext ('dlgContactListEditor', 'txtListname', listname)
	   
	   for j in range (1, len(data)):
	      try:
		verifytablecell ('dlgContactListEditor', 'tblmail', row, col, data[j].strip())
		row = row + 1
		#print 'j:',j
	      except error,msg:
		print "Email Contact Not Found"
	   
	   click ('dlgContactListEditor', 'btnOk')
	   log ('ContactVerification', 'pass')	
	   break 
	except error,msg:
	    if string.find (str(msg), str1) == -1:
		print "Error!"
	    print "Contact Not Found"	
	    log('ContactVerification','fail')	


def Cancelling(item):
    i = 0
    try:
	while i < 2: #0 for Discard and 1 for cancel
		selectmenuitem ('Evolution-Mail', 'mnuFile;mnuNew;mnuContactList')
		settextvalue ('dlgContactListEditor', 'txtListname', item)
		setcontext ("Contact List Editor", item)
		click ('dlgContactListEditor', 'btnCancel')
		if i == 0:
			click ('dlgEvolutionQuery', 'btnDiscard')
		elif i==1:
			click ('dlgEvolutionQuery', 'btnCancel')
		else:
			break
		i = i + 1	
	if i == 2:
		click ('dlgContactListEditor', 'btnCancel')
		click ('dlgEvolutionQuery', 'btnSave')
		wait(3)
		click ('dlgDuplicateContactDetected','btnAdd')
    except error,msg:
	if string.find (str(msg), str1) == -1:
	   print "Error!"
	print "Cancellation Failed"    
        	
#--Main Block---
try:
	file=open('contactlist.dat','r')
	fp=open('contactlist.dat','r')
	lines=file.readlines()
	record=fp.readlines()
	fp.close()
	file.close()

except IOError:
	print IOError
	sys.exit()

#--Contact list creation--
log ('ContactListCreation','teststart')	
for i in range (0, len(lines)):
	data = string.split (lines[i], ',')
	#contact (data)
log ('ContactListCreation', 'testend')

#--Contact list verfication--
log ('ContactVerification', 'teststart')
for i in range(0, len(lines)):
	#print 'i:',i
	data = string.split (lines[i], ',')
	contactverify (data)
log ('ContactVerification', 'testend')

#--Cancelling the addition of contacts in Contact List--
log ('CancellationOfContact','teststart')
fp = open ('contactlist.dat', 'r')
record1 = fp.readline()
record2 = string.split(record1, ',')
Cancelling (record2[0])
log ('CancellationOfContact', 'testend')


