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
def testSaveAll(str,paths):
	try:
		log('Testing Save All Option','info')	
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
			time.sleep(5)
		#i=0
		#get the file contents before appending text
		contents_before=range(2)
		i=0
		for path in paths:
			fp=open(path,'r')
			contents_before[i]=fp.read()
			i=i+1
			fp.close()
		i=0
		for path in paths:
			time.sleep(3)
			selecttab('*gedit','ptl1',path)
			time.sleep(2)
			remap('evolution','*gedit')
			textbox='txt'+ repr(i)
			appendtext('*gedit',textbox,str);
			i=i+1
		#test close all
		selectmenuitem('*gedit','mnuDocuments;mnuSaveAll')
		time.sleep(4)
		#add up the new appended text to the contents_before
		contents_before[0]=contents_before[0]+str+"\n"
		contents_before[1]=contents_before[1]+str+"\n"
		#check the new contents_before with the contents of each file in a loop
		i=0
		for path in paths:
			fp=open(path,'r')
			new_contents=fp.read()
			if (new_contents==contents_before[i]):
				pass
			else:
				log('Test Save All option Failed','error')
				raise LdtpExecutionError(0)
				return
			i=i+1	
			fp.close()
	except:
       		log('Test Save All Option Failed','error')
       	        raise LdtpExecutionError(0)
       		return
   	log('Test Save All Option Success','info')

		
try:
	log('Test Save All Option','teststart')	
	launchapp('gedit',1)
	waittillguiexist('*gedit')
	#get the data from the data xml
	obj = LdtpDataFileParser(datafilename)
	fpath1= obj.gettagvalue('file0')[0] # file 1
	fpath2=obj.gettagvalue('file1')[0] #file 2
	str=obj.gettagvalue('text')[0]
	sorttext=obj.gettagvalue('sorttext')[0]
	strlist=split(sorttext)
	#Create the files if they dont exist
	if os.path.exists(os.getcwd() + '/' + fpath1) == 0: 
		 fp=open(fpath1,'w')
		 i=0
		 length=len(strlist)
		 while i<length:
			 fp.write(strlist[i]+'\n')
			 i=i+1
		 fp.close()
	if os.path.exists(os.getcwd() + '/' + fpath2) == 0: 
		 fp=open(fpath2,'w')
		 i=0
		 length=len(strlist)
		 while i<length:
			 fp.write(strlist[i]+'\n')
			 i=i+1
		 fp.close()
	paths=[fpath1,fpath2]
	testSaveAll(str,paths)
except:
	log('Test Save All Option','error')
	raise LdtpExecutionError(0)
time.sleep(5)
selectmenuitem('*gedit','mnuFile;mnuQuit')
time.sleep(5)
if guiexist('dlgQuestion')==1:
	click('dlgQuestion','btnClosewithoutSaving')
time.sleep(5)
log('Test Save All Option','testend')
