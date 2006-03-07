#!/usr/bin/env python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
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

def deletecontact(name):
     log ('Deleting a contact','teststart')
     try:
         #selectcontact (titleappend(name)[1:])
         selectmenuitem ('frmEvolution-Contacts','mnuEdit;mnuDelete')
         waittillguiexist ('dlgQuestion')
         time.sleep (2)
         click ('dlgQuestion','btnDelete')
     except:
         log ('Deleting Contact Failed','error')
         log ('Deleting a contact','testend')
         raise LdtpExecutionError(0)
     log ('Deleting a contact','testend')

def getcurwindow():
     if guiexist ('frmEvolution-Mail')==1:
          print "found"
          return 'frmEvolution-Mail'
     elif guiexist ('frmEvolution-Contacts')==1:
          return 'frmEvolution-Contacts'
     elif guiexist ('frmEvolution-Calendars')==1:
          return 'frmEvolution-Calendars'
     elif guiexist ('frmEvolution-Memos')==1:
          return 'frmEvolution-Memos'
     elif guiexist ('frmEvolution-Tasks')==1:
          return 'frmEvolution-Tasks'
               
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

def selectContactPane():
    """Selects the Contacts Pane in Evolution"""
    log ('Open Evolution Contacts Pane','teststart')
    try:
         window_id=getcurwindow()
         click (window_id,'tbtnContacts')
         waittillguiexist ('frmEvolution-Contacts')
    except:
        log ('error selecting Contacts pane','error')
        log ('Open Evolution Contacts Pane','testend')
        raise LdtpExecutionError(0)
    
    log ('Open Evolution Contacts Pane','testend')

def selectMailPane():
    """Selects the Contacts Pane in Evolution"""
    log ('Open Evolution Mail Pane','teststart')
    try:
         print "b4 getcurinwdow"
         window_id=getcurwindow()
         print "after getcurinwdow"
         click (window_id,'tbtnMail')
         waittillguiexist ('frmEvolution-Mail')
    except:
        log ('error selecting Mail pane','error')
        log ('Open Evolution Mail Pane','testend')
        raise LdtpExecutionError(0)
    
    log ('Open Evolution Mail Pane','testend')

def selectContactPane():
    """Selects the Contacts Pane in Evolution"""
    log ('Open Evolution Contacts Pane','teststart')
    try:
         window_id=getcurwindow()
         click (window_id,'tbtnContacts')
         waittillguiexist ('frmEvolution-Contacts')
    except:
        log ('error selecting Contacts pane','error')
        log ('Open Evolution Contacts Pane','testend')
        raise LdtpExecutionError(0)
    
    log ('Open Evolution Contacts Pane','testend')


def selectMemoPane():
    """Selects the Calendars Pane in Evolution"""
    log ('Open Evolution Memos Pane','teststart')
    try:
         window_id=getcurwindow()
         click (window_id,'tbtnMemos')
         waittillguiexist ('frmEvolution-Memos')
    except:
        log ('error selecting Memos pane','error')
        log ('Open Evolution Memos Pane','testend')
        raise LdtpExecutionError(0)
    
    log ('Open Evolution Memos Pane','testend')

def selectTaskPane():
    """Selects the Contacts Pane in Evolution"""
    log ('Open Evolution Tasks Pane','teststart')
    try:
         window_id=getcurwindow()
         click (window_id,'tbtnTasks')
         waittillguiexist ('frmEvolutions-Tasks')
    except:
        log ('error selecting Tasks pane','error')
        log ('Open Evolution Tasks Pane','testend')
        raise LdtpExecutionError(0)
    
    log ('Open Evolution Tasks Pane','testend')

def selectCalendarPane():
    """Selects the Contacts Pane in Evolution"""
    log ('Open Evolution Calendars Pane','teststart')
    try:
         window_id=getcurwindow()
         click (window_id,'tbtnCalendars')
         waittillguiexist ('frmEvolution-Calendars')
    except:
        log ('error selecting Calendars pane','error')
        log ('Open Evolution Calendars Pane','testend')
        raise LdtpExecutionError(0)
    
    log ('Open Evolution Calendars Pane','testend')


def selectaddrbook (name):
     log ('Selecting a given Address book','teststart')
     try:
          selectContactPane()
          #remap ('evoltion','frmEvolution-Contacts')
          selectrow ('frmEvolution-Contacts','ttblContactSourceSelector',name)
          #undoremap ('evolution','frmEvolution-Contacts')
     except:
          log ('Unable to Select AddressBook','error')
          log ('Selecting a given Address book','testend')
          raise LdtpExecutionError (0)
     log ('Selecting a given Address book','testend')
          

# def selectcontact(name):
#     """Select a particular contact by full name"""
    
#     log ('Selecting Contact','teststart')
#     try:
#         #selectContactPane()
#         time.sleep (10)
#         if gettextvalue ('frmEvolution-Contacts','txtSearchTextEntry')!='':
#              settextvalue ('frmEvolution-Contacts','txtSearchTextEntry','aaa')
#              time.sleep (5)
#         settextvalue ('frmEvolution-Contacts','txtSearchTextEntry',name)
#         click ('frmEvolution-Contacts','btnFindNow')
#         time.sleep(2)
#         remap ('evolution','frmEvolution-Contacts')
#         time.sleep(2)
#         value=2
# #         if 'pnlcurrentaddressbookfolderhas0cards' in getobjextlist('frmEvolution-Contacts') and 'pnlcurrentaddressbookfolderhas0cards1' in getobjectlist('frmEvolution-Contacts'):
# #              print "out in 0"
# #              time.sleep (10)
# #              raise LdtpExecutionError(0)
#         print "out of 0"
#         time.sleep (3)
#         try:
#              print "come into 1"
#              time.sleep (10)
#              selectpanel ('frmEvolution-Contacts','pnlcurrentaddressbookfolderhas1card',1)
#              selectpanel ('frmEvolution-Contacts','pnlcurrentaddressbookfolderhas1card',1)
#         except:
#              while True:
#                   try:
#                        print value
#                        time.sleep (3)
#                        selectpanelname ('frmEvolution-Contacts','pnlcurrentaddressbookfolderhas'+str(value)+'cards',value)
#                        selectpanel ('frmEvolution-Contacts','pnlcurrentaddressbookfolderhas'+str(value)+'cards',value)
#                        break
#                   except:
#                        value += 1
#                        continue
#         undoremap ('evolution','frmEvolution-Contacts')
#         time.sleep (2)
        
#     except:
#         log ('Unable to select Contact','error')
#         log ('Selecting Contact','testend')
#         raise LdtpExecutionError(0)
    
#     log ('Selecting Contact','testend')



def selectcontact(name):
     log ('Select Contact','teststart')
     if guiexist ('frmEvolution-Contacts')!=1:
          selectContactPane()          
     try:
          #remap ('evolution','frmEvolution-Contacts')
          print "HERE"
          print getobjectlist ('frmEvolution-Contacts')
          print "AFTER"
          for obj in getobjectlist ('frmEvolution-Contacts'):
               if obj.startswith ('pnlcurrentaddressbook'):
                    panel_name=obj
                    break
          time.sleep (2)
          selectpanelname ('frmEvolution-Contacts',panel_name,name)
          selectpanelname ('frmEvolution-Contacts',panel_name,name)
          time.sleep (2)
     except:
          log ('Select Contact Failed','error')
          log ('Select Contact','testend')
          raise LdtpExecutionError(0)
     log ('Select Contact','testend')
               
     
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
    #import sys
    #try:
    log ('Get Modified Values','teststart')
    data_object = LdtpDataFileParser (datafilename)
    AddrBook=data_object.gettagvalue ('AddrBook')
    FullName==data_object.gettagvalue ('Name')
    NewWorkEmail=data_object.gettagvalue ('NewWorkEmail')
    NewHomeEmail=data_object.gettagvalue ('NewHomeEmail')
    NewHomeAdd=data_object.gettagvalue ('NewHomeAddress')
    NewWordAdd=data_object.gettagvalue ('NewWorkAddress')
    NewOtherAdd=data_object.gettagvalue ('NewOtherAddress')
    log ('Get Modified Values','testend')
    return AddrBook,FullName,NewWorkEmail,NewHomeEmail,NewHomeAdd,NewWorkAdd,NewOtherAdd
#     except:
#          log ('error in getting values for contact modification','error')
#          log ('Get Modified Values','testend')
#          print sys.exc_info()
#          raise LdtpExecutionError(    log ('Get Modified Values','testend')


def getcontactlistvals(datafilename):
    log ('Get Contact List values','teststart')
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
        log ('Get Contact List values','testend')
        raise LdtpExecutionError(0)
    log ('Get Contact List values','testend')
    return ListName,EmailAddresses


def getmodlistvals(datafilename):
    log ('Get Modify Contact List values','teststart')
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
        log ('Get Contact List values','testend')
        raise LdtpExecutionError(0)
    log ('Get Contact List values','testend')
    return ListName,AddEmailAddresses,DelEmailAddresses
    
def opencontactlist(ListName):
    log ('Open Contact List','teststart')
    try:
        selectcontact (ListName[0])
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        setcontext ('Contact List Editor',ListName[0])
        waittillguiexist ('dlgContactListEditor')
    except:
        log ('could not open Contact list','error')
        log ('Open Contact List','testend')
        raise LdtpExecutionError(0)
    log ('Open Contact List','testend')

def deletecontactlist(name):
    log ('Delete Contact List','teststart')
    try:
        deletecontact(name)
    except:
        log ('Delete Contact List Failed','error')
        log ('Delete Contact List','testend')
        raise LdtpExecutionError(0)
    log ('Delete Contact List','testend')

def addcontact(AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd):
    """ Adds a new contact to evolution"""
    log ('Add New Contact','teststart')
    #OPEN CONTACT EDITOR
    try:
        #=getcontactvals(datafilename)
        selectContactPane()
        selectaddrbook (AddrBook[0])
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuNew;mnuContact')
        time.sleep(2)
        waittillguiexist ('dlgContactEditor')
    except:
        log ('Could Not select Contacts Button','error')
        log ('Add New Contact','testend')
        raise LdtpExecutionError(0)

    #SET VALUES FOR CONTACT TAB
    try:
        selecttab ('dlgContactEditor','ptl0','Contact')
        settextvalue ('dlgContactEditor','txtFullName', FullName[0])
#         name=FullName[0].split(' ')
#         appendtext=''
#         for x in range(1,len(name)):
#             appendtext=' '+name[x]
#         if len(name)>1:
#             appendtext+=', '
#             appendtext+=name[0]
#         else:
#             appendtext+=name[0]
        setcontext ('Contact Editor','Contact Editor -'+titleappend(FullName[0]))
        if len(Nick)>0:
            settextvalue ('dlgContactEditor','txtNickname',Nick[0])

        if len(WorkEmail)>0:
            settextvalue ('dlgContactEditor','txtWork',WorkEmail[0])

        if len(HomeMail)>0:
            settextvalue ('dlgContactEditor','txtHome',HomeMail[0])

        if len(BusPhone)>0:
            settextvalue ('dlgContactEditor','txtBusinessPhone',BusPhone[0])
        #print "YAHOO[0]",Yahoo[0]
        if len(Yahoo)>0:
            print "INSIDE"
            settextvalue ('dlgContactEditor','txtYahoo',Yahoo[0])
    except:
        log ('Error While setting values in 1st tab','error')
        log ('Add New Contact','testend')
        raise LdtpExecutionError(0)
    time.sleep(2)

    #PERSONAL INFORMATION TAB
    try:
        if len(HomePage)>0 or len(Profession)>0 or  len(Notes)>0:
            selecttab ('dlgContactEditor','ptl0','Personal Information')
            time.sleep(1)
            if len(HomePage)>0:
                settextvalue ('dlgContactEditor','txtHomePage',HomePage[0])
            if len(Profession)>0:
                settextvalue ('dlgContactEditor','txtProfession',Profession[0])
            if len(Notes)>0:
                settextvalue ('dlgContactEditor','txtNotes',Notes[0])
    except:
        log ('Error While setting values in 2nd tab','error')
        log ('Add New Contact','testend')
        raise LdtpExecutionError(0)
    time.sleep(2)
    #MAILING ADDRESS TAB
    try:
        if  len(HomeAdd)>0 or len(WorkAdd)>0 or len(OtherAdd)>0:
            selecttab ('dlgContactEditor','ptl0','Mailing Address')
            time.sleep(1)
            if len(HomeAdd)>0:
                settextvalue ('dlgContactEditor','txtAddress',HomeAdd[0])
            if len(WorkAdd)>0:
                settextvalue ('dlgContactEditor','txtAddress1',WorkAdd[0])
            if len(OtherAdd)>0:
                settextvalue ('dlgContactEditor','txtAddress2',OtherAdd[0])
    except:
        log ('Error While setting values in 3rd tab','error')
        log ('Add New Contact','testend')
        raise LdtpExecutionError(0)

    time.sleep (2)
    try:
        click ('dlgContactEditor','btnOK')
        time.sleep (5)
        if guiexist ('dlgDuplicateContactDetected')==1:
            log ('contact already exists','info')
            click ('dlgDuplicateContactDetected','btnAdd')
            time.sleep(2)
        verifyaddedcontact(AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd)
        time.sleep(2)
    except:
        log ('Contact Addition Failed!','error')
        log ('Add New Contact','testend')
        raise LdtpExecutionError(0)
    log ('Add New Contact','testend')


def verifyaddedcontact(AddrBook,FullName,Nick,WorkEmail,HomeMail,BusPhone,Yahoo,HomePage,Profession,Notes,HomeAdd,WorkAdd,OtherAdd):
    log ('Verify Added Contact','teststart')
    try:
        selectaddrbook (AddrBook[0])
        temp=titleappend(FullName[0])[1:]
#        print temp
#        raw_input ("temp")
        selectcontact(temp)
        time.sleep (2)
        selectmenuitem ('frmEvolution-Contacts','mnuFile;mnuOpen')
        title='dlgContactEditor-'+titleappend(FullName[0]).replace(' ','')
        setcontext ('Contact Editor','Contact Editor -'+titleappend(FullName[0]))
        waittillguiexist ('dlgContactEditor')
        time.sleep(2)
        if gettextvalue ('dlgContactEditor','txtFullName')!=FullName[0]:
            log ('Full Name does not match','info')
            raise LdtpExecutionError(0)

        if len(Nick)>0 and gettextvalue ('dlgContactEditor','txtNickname')!=Nick[0]:
            log ('Nick Name matches','info')
            raise LdtpExecutionError(0)
        if len (WorkEmail)>0 and gettextvalue ('dlgContactEditor','txtWork')!=WorkEmail[0]:
            log ('Work Email matches','info')
            raise LdtpExecutionError(0)
        if len(HomeMail)>0 and  gettextvalue ('dlgContactEditor','txtHome')!=HomeMail[0]:
            log ('Home Email matches','info')
            raise LdtpExecutionError(0)
        if len(BusPhone)>0 and gettextvalue ('dlgContactEditor','txtBusinessPhone')!=BusPhone[0]:
            log ('Business Phone matches','info')
            raise LdtpExecutionError(0)
        print "Bus phone over"
        if len (Yahoo)>0 and  gettextvalue ('dlgContactEditor','txtYahoo')!=Yahoo[0]:
            log ('Yahoo ID matches','info')
            raise LdtpExecutionError(0)
        if len(HomePage)>0 and  gettextvalue ('dlgContactEditor','txtHomePage')!=HomePage[0]:
            log ('Home Page matches','info')
            raise LdtpExecutionError(0)
        if len( Profession)>0 and  gettextvalue ('dlgContactEditor','txtProfession')!=Profession[0]:
            log ('Profession matches','info')
            raise LdtpExecutionError(0)
        if len(Notes)>0 and  gettextvalue ('dlgContactEditor','txtNotes')!=Notes[0]:
            log ('Notes matches','info')
            raise LdtpExecutionError(0)
        #homeaddress=gettextvalue ('dlgContactEditor','txtAddress')
#         if len(HomeAdd)>0 and   gettextvalue ('dlgContactEditor','txtAddress')!=HomeAdd[0]:
#             #print "Error here","from dialog:"+homeaddress+"a","from xml file:"+HomeAdd[0]
#             log ('Home Address matches','info')
#             raise LdtpExecutionError(0)
#         if len (WorkAdd)>0 and  gettextvalue ('dlgContactEditor','txtAddress1')!=WorkAdd[0]:
#             log ('Work Address matches','info')
#             raise LdtpExecutionError(0)
#         if len(OtherAdd)>0 and  gettextvalue ('dlgContactEditor','txtAddress2')!=OtherAdd[0]:
#             log ('Other Address matches','info')
#             raise LdtpExecutionError(0)
        undoremap ('evolution','frmEvolution-Mail')
        click ('dlgContactEditor','btnCancel')
    except:
        log ('Contact has not been added correctly','error')
        log ('Verify Added Contact','testend')
        raise LdtpExecutionError(0)
    log ('Verify Added Contact','testend')
