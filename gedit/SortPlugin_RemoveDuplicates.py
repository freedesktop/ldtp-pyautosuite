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
def testRemoveDuplicates(filename): #case insensitive
	try:
		log('Testing Sort Plugin with Remove Duplicates','info')	
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
			#select sort
			time.sleep(5)
			selectmenuitem('*gedit','mnuEdit;mnuSort')
                        time.sleep(5)
                        waittillguiexist('dlgSort')
                        if guiexist('dlgSort')==1:
                                click('dlgSort','btnSort')
                                time.sleep(6)
                                selectmenuitem('*gedit','mnuFile;mnuSave')
                                time.sleep(6)
                                #test Sort
                                fp=open(filename)
                                a=fp.readline()
                                b=fp.readline()
				#compare lines in pair ..eg line 1 with 2 then 2 with 3 etc
				#here considering only alphabets so skipping over the other characters
                                while (b!=''):
                                        i=0
                                        j=0
                                        while ((i<len(a)) and(a[i] not in lowercase) and (a[i] not in uppercase)):
                                            i=i+1
                                        while ((j<len(b)) and (b[j] not in lowercase) and (b[j] not in uppercase)):
                                            j=j+1
                                        if((lower(a[i:])<=lower(b[j:]))):
                                                a=b
                                                b=fp.readline()
                                        else:
                                                
                                                log('Sort did not happen in the natural order','error')
			                        raise LdtpExecutionError(0)
                                fp.close()
                        else:
                                log('Sort Dialog does not appear','error')
                                raise LdtpExecutionError(0)
			#select Sort with Remove Duplicates insensitive option
			time.sleep(2)
               		selectmenuitem('*gedit','mnuEdit;mnuSort')
			waittillguiexist('dlgSort')	
			if guiexist('dlgSort')==1:
				if verifyuncheck('dlgSort','chkRemoveduplicates')==1:
					click('dlgSort','chkRemoveduplicates')
				click('dlgSort','btnSort')
				time.sleep(5)
				selectmenuitem('*gedit','mnuFile;mnuSave')
				time.sleep(5)
				#test remove Duplicates
				fp1=open(filename)
				a=fp1.readline()
				#test the number of occurances of each line..if greater than
				#one then there are duplicates
				while a!='':
					fp2=open(filename)
					b=fp2.readline()
					count=0
					while b!='':
						if a==b:
							if(count==0):
								count=count+1
							else:
								log('Remove Duplicates Failed','error')
								raise LdtpExecutionError(0)
						else:
							if (a!=b):
								pass
							else:
								
								log('Remove Duplicates Failed','error')
								raise LdtpExecutionError(0)
						b=fp2.readline()
					a=fp1.readline()
					fp2.close()	
				fp1.close()
			else:		
				log('Sort Dialog does not appear','error')
				raise LdtpExecutionError(0)
		else:
		        log('Preferences dialog does not appear','error')
        	        raise LdtpExecutionError(0)
   	except:
       		log('Test Sort Plugin with Remove Duplicates Failed','error')
       	        raise LdtpExecutionError(0)
       		return
   	log('Test Sort Plugin with Remove Duplicates Success','info')

				


		
try:
	log('Test Sort Plugin with Remove Duplicates','teststart')	
	launchapp('gedit',1)
	waittillguiexist('*gedit')
	#get the data from the data xml	
	obj = LdtpDataFileParser(datafilename)
 	fname = obj.gettagvalue('file0')[0]
	sorttext=obj.gettagvalue('sorttext')[0]
	strlist=rsplit(sorttext)
	if os.path.exists(os.getcwd() + '/' + fname) == False: 
		 a=open(fname,'w')
		 i=0
		 length=len(strlist)
		 while i<length:
			 a.write(strlist[i]+'\n')
			 i=i+1
		 a.close()
	testRemoveDuplicates(fname)
except:
	log('Test Sort Plugin with Remove Duplicates Failed','error')
	raise LdtpExecutionError(0)
selectmenuitem('*gedit','mnuFile;mnuQuit')
time.sleep(8)
if guiexist('dlgQuestion')==1:
	click('dlgQuestion','btnClosewithoutSaving')
log('Test Sort Plugin with Remove Duplicates','testend')
