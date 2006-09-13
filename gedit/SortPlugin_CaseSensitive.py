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


from string import *
from ldtp import *
from ldtputils import *
def testSortPluginwithcase(filename): #case sensitive
	try:
		log('Testing Sort Plugin with case sensitive','info')	
		time.sleep(5)
       	 	selectmenuitem('*gedit','mnuEdit;mnuPreferences')
    	        waittillguiexist('dlggeditPreferences')
       	        if guiexist('dlggeditPreferences') == 1:
			selecttab('dlggeditPreferences','ptl0','Plugins')
			index=gettablerowindex ('dlggeditPreferences','tbl1','Sort')
			checkrow('dlggeditPreferences','tbl1',index,0)
			click('dlggeditPreferences','btnClose')
			#open a file
			selectmenuitem('*gedit','mnuFile;mnuOpenLocation')
                        waittillguiexist('dlgOpenLocation')
                        if guiexist('dlgOpenLocation')==1:
                                settextvalue('dlgOpenLocation','cboEnterthelocation(URI)ofthefileyouwouldliketoopen',filename)
                                click('dlgOpenLocation','btnOpen')
                        else:
                                log('Open Location dialog does not appear','error')
                                raise LdtpExecutionError(0)
			#select Sort with case sensitive option
			time.sleep(5)
               		selectmenuitem('*gedit','mnuEdit;mnuSort')
			waittillguiexist('dlgSort')
			if guiexist('dlgSort') == 1:
				if verifycheck('dlgSort','chkIgnorecase') == 1:
					click('dlgSort','chkIgnorecase')
					click('dlgSort','btnSort')
					time.sleep(5)
					selectmenuitem('*gedit','mnuFile;mnuSave')
					time.sleep(5)
					#test case sensitive Sort
					fp=open(filename)
					a=fp.readline()
					b=fp.readline()
					#compare lines in pair ..eg line 1 with 2 then 2 with
					#3 etc					
					#here considering only alphabets so skipping over the other characters
					while a!='':
						i=0
                                        	j=0
                                	        while ((i<len(a)) and(a[i] not in lowercase) and (a[i] not in uppercase)):
                                	            i=i+1
                                	        while ((j<len(b)) and (b[j] not in lowercase) and (b[j] not in uppercase)):
                                	            j=j+1
                                	        				
					        if((a[i:]>b[j:]) or  (lower(a[i:])<=lower(b[j:]))):
					                a=fp.readline()
					                b=fp.readline()
       						else:
							log('Test Sort plugin with Case sensitive Failed','error')
							raise LdtpExecutionError(0)
							return
			else:
				log('Sort Dialog does not appear','error')
				raise LdtpExecutionError(0)
			#select Sort with case insensitive option
			time.sleep(2)
               		selectmenuitem('*gedit','mnuEdit;mnuSort')
			waittillguiexist('dlgSort')	
			if guiexist('dlgSort') == 1:
				if verifyuncheck('dlgSort','chkIgnorecase') == 1:
					click('dlgSort','chkIgnorecase')
				click('dlgSort','btnSort')
				time.sleep(5)
				selectmenuitem('*gedit','mnuFile;mnuSave')
				time.sleep(5)
					
			else:
				log('Sort Dialog does not appear','error')
				raise LdtpExecutionError(0)
		else:
		        log('Preferences dialog does not appear','error')
        	        raise LdtpExecutionError(0)
   	except:
       		log('Test Sort Plugin with case sensitive Failed','error')
       	        raise LdtpExecutionError(0)
       		return
   	log('Test Sort Plugin with case sensitive Success','info')

		
try:
	log('Test Sort Plugin with case sensitive','teststart')	
	launchapp('gedit',1)
	waittillguiexist('*gedit')
	#get the data from the data xml
	obj = LdtpDataFileParser(datafilename)
        filename = obj.gettagvalue('file0')[0]
	sorttext=obj.gettagvalue('sorttext')[0]
	strlist=rsplit(sorttext,':')
	#Create the files if they dont exist
	if os.path.exists(os.getcwd() + '/' + filename) == False: 
		 a=open(filename,'w')
		 i=0
		 length=len(strlist)
		 while i<length:
			 a.write(strlist[i]+'\n')
			 i=i+1
		 a.close()
	testSortPluginwithcase(filename)
except:
	log('Test Sort Plugin with case sensitive failed','error')
	raise LdtpExecutionError(0)
selectmenuitem('*gedit','mnuFile;mnuQuit')
time.sleep(5)
if guiexist('dlgQuestion'):
	click('dlgQuestion','btnClosewithoutSaving')
log('Test Sort Plugin with case sensitive','testend')
