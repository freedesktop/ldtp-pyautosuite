#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Prashanth Mohan  <prashmohan@gmail.com>
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

from ldtp import *
from ldtputils import *
from evoutils.mail import *
from evoutils import *

def deletecontact(name, contactlist=False):
     try:
         if contactlist == False:
              selectcontact (titleappend(name)[1:])
         else:
              selectcontact (name)
         selectmenuitem ('frmEvolution-Contacts','mnuEdit;mnuDeleteContact')
         waittillguiexist ('dlgQuestion')
         click ('dlgQuestion','btnDelete')
         waittillguinotexist ('dlgQuestion')
         try:
              if contactlist == False:
                   selectcontact (titleappend(name)[1:])
              else:
                   selectcontact (name)
         except:
              return
         raise LdtpExecutionError(0)
     except:
         log ('Deleting Contact Failed','error')
         raise LdtpExecutionError(0)

               
def getcontactvals(datafilename):
    """ GET INFORMATION FROM XML FILE FOR ADDING CONTACTS"""
    try:
        data_object = LdtpDataFileParser (datafilename)
        AddrBook=data_object.gettagvalue ('AddrBook')
        FullName=data_object.gettagvalue ('FullName')
        Nick=data_object.gettagvalue ('NickName')
        WorkEmail=data_object.gettagvalue ('WorkEmail')
        HomeMail=data_object.gettagvalue ('HomeEmail')
        BusPhone=data_object.gettagvalue ('BusinessPhone')
        Yahoo=data_object.gettagvalue ('Yahoo')
        HomePage=data_object.gettagvalue ('HomePage')
        Profession=data_object.gettagvalue ('Profession')
        Notes=data_object.gettagvalue ('Notes')
        HomeAdd=data_object.gettagvalue ('HomeAddress')
        WorkAdd=data_object.gettagvalue ('WorkAddress')
        OtherAdd=data_object.gettagvalue ('OtherAddress')

    except:
        log ('Error While reading values from XML file','error')
        log ('Add New Contact','testend')
        raise LdtpExecutionError(0)

    return AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd


def selectPanel(components='Mail'):
    """Selects Pane in Evolution"""
    try:
         window_id = 'frmEvolution-*'
         click (window_id, 'tbtn' + components)
         if components != 'Mail':
         	waittillguiexist ('frmEvolution-' + components)
    except:
        log ('error selecting pane','error')
        raise LdtpExecutionError(0)



def selectaddrbook (name):
     try:
          selectContactPane()
          if name:
               selectrow ('frmEvolution-Contacts','ttblContactSourceSelector',name)
     except:
          log ('Unable to Select AddressBook','error')
          raise LdtpExecutionError (0)

def selectcontact(name):
     if guiexist ('frmEvolution-Contacts')!=1:
          selectContactPane()          
     try:
          remap ('evolution','frmEvolution-Contacts')
          for obj in getobjectlist ('frmEvolution-Contacts'):
               if obj.startswith ('pnlcurrentaddressbook'):
                    panel_name=obj
                    break
          time.sleep (2)
          selectpanelname ('frmEvolution-Contacts',panel_name,name)
          time.sleep (2)
     except:
          log ('Select Contact Failed','error')
          raise LdtpExecutionError(0)
     
def titleappend(name):
     name=name.split (' ')
     append=''
     for x in range(1,len(name)):
          append=' '+name[x]
     if len(name)>1:
          append+=', '
          append+=name[0]
     else:
          append+=' '
          append+=name[0]
     return append
 
def getmodifiedvals(datafilename):
    """Get Data from an XML file for Contact Modification"""
    data_object = LdtpDataFileParser (datafilename)
    AddrBook=data_object.gettagvalue ('AddrBook')
    FullName==data_object.gettagvalue ('Name')
    NewWorkEmail=data_object.gettagvalue ('NewWorkEmail')
    NewHomeEmail=data_object.gettagvalue ('NewHomeEmail')
    NewHomeAdd=data_object.gettagvalue ('NewHomeAddress')
    NewWordAdd=data_object.gettagvalue ('NewWorkAddress')
    NewOtherAdd=data_object.gettagvalue ('NewOtherAddress')
    return AddrBook,FullName,NewWorkEmail,NewHomeEmail,NewHomeAdd,NewWorkAdd,NewOtherAdd


def getcontactlistvals(datafilename):
    data_object = LdtpDataFileParser (datafilename)
    ListName=data_object.gettagvalue ('ListName')
    EmailAddresses=[]
    try:
        indexval=1
        while True:
            try:
                mail=data_object.gettagvalue ('Email'+str(indexval))[0]
                EmailAddresses.append(mail)
                if mail=='':
                    break
            except:
                break
            indexval=indexval+1
    except:
        log ('error while getting contact list values','error')
        raise LdtpExecutionError(0)
    return ListName,EmailAddresses


def getmodlistvals(datafilename):
    data_object = LdtpDataFileParser (datafilename)
    ListName=data_object.gettagvalue ('ListName')
    AddEmailAddresses=[]
    DelEmailAddresses=[]
    addmail=''
    delmail=''
    try:
        indexval=1
        while True:
             try:
                  addmail=data_object.gettagvalue ('AddEmail'+str(indexval))
                  delmail=data_object.gettagvalue ('DelEmail'+str(indexval))
                  if len(addmail) ==0 and len (delmail)==0:
                       break                
                  if len (addmail)>0:
                       AddEmailAddresses.append (addmail[0])
                  if len(delmail)>0:
                       DelEmailAddresses.append (delmail[0])
             except:
                  log ('Error in Data read','error')
                  break
             indexval=indexval+1
        print AddEmailAddresses,DelEmailAddresses
        time.sleep (5)
    except:
        log ('error while getting contact list values','error')
        raise LdtpExecutionError(0)
    return ListName,AddEmailAddresses,DelEmailAddresses

    
def opencontactlist(ListName):
    try:
        selectcontact (ListName[0])
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        waittillguiexist ('*'+ListName[0]+'*')
    except:
        log ('could not open Contact list','error')
        raise LdtpExecutionError(0)


def deletecontactlist(name):
    try:
         deletecontact(name)
    except:
        log ('Delete Contact List Failed','error')
        raise LdtpExecutionError(0)

def opennewcontact (AddrBook=[]):
    #OPEN CONTACT EDITOR
    try:
        selectContactPane()
        if AddrBook:
             selectaddrbook (AddrBook[0])
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuNew;mnuContact')
        time.sleep(2)
        waittillguiexist ('*ContactEditor*')
    except:
        log ('Could Not select Contacts Button','error')
        raise LdtpExecutionError(0)


def addcontact(AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd):
    """ Adds a new contact to evolution"""
    #SET VALUES FOR CONTACT TAB
    try:
        selecttab ('*ContactEditor*','ptl0','Contact')
        settextvalue ('*ContactEditor*','txtFullName', FullName[0])
        if len(Nick)>0:
            settextvalue ('*ContactEditor*','txtNickname',Nick[0])

        if len(WorkEmail)>0:
            settextvalue ('*ContactEditor*','txtWork',WorkEmail[0])

        if len(HomeMail)>0:
            settextvalue ('*ContactEditor*','txtHome',HomeMail[0])

        if len(BusPhone)>0:
            settextvalue ('*ContactEditor*','txtBusinessPhone',BusPhone[0])
        #print "YAHOO[0]",Yahoo[0]
        if len(Yahoo)>0:
            print "INSIDE"
            settextvalue ('*ContactEditor*','txtYahoo',Yahoo[0])
    except:
        log ('Error While setting values in 1st tab','error')
        raise LdtpExecutionError(0)
    time.sleep(2)

    #PERSONAL INFORMATION TAB
    try:
        if len(HomePage)>0 or len(Profession)>0 or  len(Notes)>0:
            selecttab ('*ContactEditor*','ptl0','Personal Information')
            time.sleep(1)
            if len(HomePage)>0:
                settextvalue ('*ContactEditor*','txtHomePage',HomePage[0])
            if len(Profession)>0:
                settextvalue ('*ContactEditor*','txtProfession',Profession[0])
            if len(Notes)>0:
                settextvalue ('*ContactEditor*','txtNotes',Notes[0])
    except:
        log ('Error While setting values in 2nd tab','error')
        raise LdtpExecutionError(0)
    time.sleep(2)
    #MAILING ADDRESS TAB
    try:
        if  len(HomeAdd)>0 or len(WorkAdd)>0 or len(OtherAdd)>0:
            selecttab ('*ContactEditor*','ptl0','Mailing Address')
            time.sleep(1)
            if len(HomeAdd)>0:
                settextvalue ('*ContactEditor*','txtAddress',HomeAdd[0])
            if len(WorkAdd)>0:
                settextvalue ('*ContactEditor*','txtAddress1',WorkAdd[0])
            if len(OtherAdd)>0:
                settextvalue ('*ContactEditor*','txtAddress2',OtherAdd[0])
    except:
        log ('Error While setting values in 3rd tab','error')
        raise LdtpExecutionError(0)

    time.sleep (2)
    try:
        click ('*ContactEditor*','btnOK')
        time.sleep (5)
        if guiexist ('dlgDuplicateContactDetected')==1:
            log ('contact already exists','info')
            click ('dlgDuplicateContactDetected','btnAdd')
            time.sleep(2)
        verifyaddedcontact(AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd)
        time.sleep(2)
    except:
        log ('Contact Addition Failed!','error')
        raise LdtpExecutionError(0)


def verifyaddedcontact(AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd):
    try:
        selectaddrbook (AddrBook[0])
        temp=titleappend(FullName[0])[1:]
        selectcontact(temp)
        time.sleep (2)
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        title='*ContactEditor*-'+titleappend(FullName[0]).replace(' ','')
        waittillguiexist ('*ContactEditor*')
        time.sleep(2)
        if gettextvalue ('*ContactEditor*','txtFullName')!=FullName[0]:
            log ('Full Name does not match','info')
            raise LdtpExecutionError(0)

        if len(Nick)>0 and gettextvalue ('*ContactEditor*','txtNickname')!=Nick[0]:
            log ('Nick Name matches','info')
            raise LdtpExecutionError(0)
        if len (WorkEmail)>0 and gettextvalue ('*ContactEditor*','txtWork')!=WorkEmail[0]:
            log ('Work Email matches','info')
            raise LdtpExecutionError(0)
        if len(HomeMail)>0 and  gettextvalue ('*ContactEditor*','txtHome')!=HomeMail[0]:
            log ('Home Email matches','info')
            raise LdtpExecutionError(0)
        if len(BusPhone)>0 and gettextvalue ('*ContactEditor*','txtBusinessPhone')!=BusPhone[0]:
            log ('Business Phone matches','info')
            raise LdtpExecutionError(0)
        print "Bus phone over"
        if len (Yahoo)>0 and  gettextvalue ('*ContactEditor*','txtYahoo')!=Yahoo[0]:
            log ('Yahoo ID matches','info')
            raise LdtpExecutionError(0)
        if len(HomePage)>0 and  gettextvalue ('*ContactEditor*','txtHomePage')!=HomePage[0]:
            log ('Home Page matches','info')
            raise LdtpExecutionError(0)
        if len( Profession)>0 and  gettextvalue ('*ContactEditor*','txtProfession')!=Profession[0]:
            log ('Profession matches','info')
            raise LdtpExecutionError(0)
        if len(Notes)>0 and  gettextvalue ('*ContactEditor*','txtNotes')!=Notes[0]:
            log ('Notes matches','info')
            raise LdtpExecutionError(0)
        homeaddress=gettextvalue ('*ContactEditor*','txtAddress')
        if len(HomeAdd)>0 and   gettextvalue ('*ContactEditor*','txtAddress')!=HomeAdd[0]:
            #print "Error here","from dialog:"+homeaddress+"a","from xml file:"+HomeAdd[0]
            log ('Home Address matches','info')
            raise LdtpExecutionError(0)
        if len (WorkAdd)>0 and  gettextvalue ('*ContactEditor*','txtAddress1')!=WorkAdd[0]:
            log ('Work Address matches','info')
            raise LdtpExecutionError(0)
        if len(OtherAdd)>0 and  gettextvalue ('*ContactEditor*','txtAddress2')!=OtherAdd[0]:
            log ('Other Address matches','info')
            raise LdtpExecutionError(0)
        click ('*ContactEditor*','btnCancel')
    except:
        log ('Contact has not been added correctly','error')
        raise LdtpExecutionError(0)
