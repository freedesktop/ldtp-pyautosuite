#############################################################################
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#	T V Lakshmi Narasimhan <lakshminaras2002@gmail.com>
#
#  Copyright 2004 - 2006 Novell, Inc.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#
#############################################################################


from ldtp import *
from ldtputils import *
from string import *
def testCloseAll(str,paths):
	try:
		log('Testing Close All Option','info')	
		#delay
		time.sleep(5)
		selectmenuitem('*gedit','mnuDocuments;mnuCloseAll')
		#open the files
		for path in paths:
			selectmenuitem('*gedit','mnuFile;mnuOpenLocation')
			waittillguiexist('dlgOpenLocation')	
			if guiexist('dlgOpenLocation')==1:
				settextvalue('dlgOpenLocation','txt0',path)
				click('dlgOpenLocation','btnOpen')
			else:
				log('OpenLocation Dialog does not appear','error')
				raise LdtpExecutionError(0)
			time.sleep(3)
		i=0
		for path in paths:
			time.sleep(3)
			selecttab('*gedit','ptl1',path)
			time.sleep(2)
			remap('evolution','*gedit')
			#the textbox name is generated here
			textbox='txt'+ repr(i)
			appendtext('*gedit',textbox,str);
			i=i+1
		#test close all with cancel
		selectmenuitem('*gedit','mnuDocuments;mnuCloseAll')
		time.sleep(5)
		if guiexist('dlgQuestion')==1:
			click('dlgQuestion','btnCancel')
		else:
			log('dlgQuestion does not appear','error')
			raise LdtpExecutionError(0)
			return 
		#test close all with CloseAll
		time.sleep(5)
		selectmenuitem('*gedit','mnuDocuments;mnuCloseAll')
		time.sleep(5)
		if guiexist('dlgQuestion')==1:
			if getrowcount('dlgQuestion','tblSelectthedocumentsyouwanttosave')==len(paths):
				log('Test Close All Success','info')
				click('dlgQuestion','btnClosewithoutSaving')
				time.sleep(5)
			
		else:
			log('Question dialog does not appear','error')
			raise LdtpExecutionError(0)
	except:
       		log('Test Close All Option Failed','error')
       	        raise LdtpExecutionError(0)
       		return
   	log('Test Close All Option Success','info')

		
try:
	log('Test Close All Option','teststart')	
	launchapp('gedit',1)
	waittillguiexist('*gedit')
	#get the data from the data xml
	obj = LdtpDataFileParser(datafilename)
	fpath1= obj.gettagvalue('file0')[0] # file 1
	fpath2=obj.gettagvalue('file1')[0] #file 2
	str=obj.gettagvalue('text')[0]
	sorttext=obj.gettagvalue('sorttext')[0]
	strlist=rsplit(sorttext,':')
	#Create the files if they dont exist
	if os.path.exists(os.getcwd() + '/' + fpath1) == False: 
		 a=open(fpath1,'w')
		 i=0
		 length=len(strlist)
		 while i<length:
			 a.write(strlist[i]+'\n')
			 i=i+1
		 a.close()
	if os.path.exists(os.getcwd() + '/' + fpath2) == False: 
		 a=open(fpath2,'w')
		 i=0
		 length=len(strlist)
		 while i<length:
			 a.write(strlist[i]+'\n')
			 i=i+1
		 a.close()
	paths=[fpath1,fpath2]
	testCloseAll(str,paths)
except:
	log('Test Close All Failed','error')
	raise LdtpExecutionError(0)
if guiexist('*gedit')==1:
	selectmenuitem('*gedit','mnuFile;mnuQuit')
	time.sleep(5)
	if guiexist('dlgQuestion')==1:
		click('dlgQuestion','btnClosewithoutSaving')
	time.sleep(5)
log('Test Close All','endtest')
