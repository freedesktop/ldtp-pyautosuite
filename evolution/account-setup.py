#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
# 
#  Author:
#     A. Nagappan <anagappan@novell.com>
# 
#  Copyright 2004 - 2005, Novell, Inc.
# 
#  This library is free software; you can redistribute it and/or
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
from evoutils.password import *
import time

class EvolutionAccountSetup:
    def create_new_account (self):
        """
        Create a new account
        This function is applicable only when already some accounts are configured
        """
        window_id = ''
        if guiexist ('frmEvolution-Mail') == 1:
            window_id = 'frmEvolution-Mail'
        elif guiexist ('frmEvolution-Calendars') == 1:
            window_id = 'frmEvolution-Calendars'
        elif guiexist ('frmEvolution-Tasks') == 1:
            window_id = 'frmEvolution-Tasks'
        elif guiexist ('frmEvolution-Contacts') == 1:
            window_id = 'frmEvolution-Contacts'
        if window_id != '':
            selectmenuitem (window_id, 'mnuEdit;mnuPreferences')
        else:
            log ('Unable to get Evolution window handle: ' + window_id, 'error')
            raise LdtpExecutionError (0)
                                
        # Wait till the gui appears
        waittillguiexist ('dlgEvolutionSettings')
        # Select mail accounts tab
        selecttab ('dlgEvolutionSettings', 'ptl0', 'Mail Accounts')
        click ('dlgEvolutionSettings', 'btnAdd')
        
    def enter_identify_info (self, xmlfilename):
        account_setup_xml = LdtpDataFileParser (xmlfilename)
        time.sleep (1)
        waittillguiexist ('frmEvolutionAccountAssistant')

        # Click button in First window
        click ('frmEvolutionAccountAssistant', 'btnForward')
        mailid = account_setup_xml.gettagvalue ('email')
        if mailid != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtEmailAddress', mailid[0])
        else:
            log ('Email id is missing - Its a mandatory field', 'error')
            raise LdtpExecutionError (0)
        acct_name = account_setup_xml.gettagvalue ('name')
        if acct_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtFullName', acct_name[0])
        default_acct = account_setup_xml.gettagvalue ('defaultaccount')
        if default_acct != []:
            if default_acct[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkMakethismydefaultaccount')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkMakethismydefaultaccount')
        reply_to = account_setup_xml.gettagvalue ('replyto')
        if reply_to != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtReply-To', reply_to[0])
        organization = account_setup_xml.gettagvalue ('organization')
        if organization != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtOrganization', organization[0])
        time.sleep (1)
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)

    def configure_imap_receiving_mail (self, xmlfilename):
        receiving_mail_xml = LdtpDataFileParser (xmlfilename)
        server_name = receiving_mail_xml.gettagvalue ('imapserver')
        if server_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtServer', server_name[0])
        else:
            log ('Imap server name missing', 'error')
            raise LdtpExecutionError (0)
        user_name = receiving_mail_xml.gettagvalue ('imapusername')
        if user_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtUsername', user_name[0])
        else:
            log ('Username missing', 'error')
            raise LdtpExecutionError (0)
        secure_connection = receiving_mail_xml.gettagvalue ('imapsecureconnection')
        if secure_connection != []:
            comboselect ('frmEvolutionAccountAssistant', 'cboUseSecureConnection', secure_connection[0])
        password_type = receiving_mail_xml.gettagvalue ('imappasswordtype')
        if password_type != []:
            comboselect ('frmEvolutionAccountAssistant', 'cboPassword', password_type[0])
        remember_password = receiving_mail_xml.gettagvalue ('imaprememberpassword')
        if remember_password != []:
            if remember_password[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkRememberpassword')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkRememberpassword')
        time.sleep (1)
        # click forward button to move to next page
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)

    def imap_receiving_options (self, xmlfilename):
        receiving_options_xml = LdtpDataFileParser (xmlfilename)
        check_mail = receiving_options_xml.gettagvalue ('checkmail')
        if check_mail != []:
            if check_mail[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkAutomaticallycheckfornewmailevery')
                mail_check_interval = receiving_options_xml.gettagvalue ('mailcheckinterval')
                if mail_check_interval != []:
                    setvalue ('frmEvolutionAccountAssistant', 'sbtn0', mail_check_interval[0])
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkAutomaticallycheckfornewmailevery')
        check_all_folders = receiving_options_xml.gettagvalue ('checkallfolders')
        if check_all_folders != []:
            if check_all_folders[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkCheckfornewmessagesinallfolders')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkCheckfornewmessagesinallfolders')
        use_custom_cmd = receiving_options_xml.gettagvalue ('usecustomcommand')
        if use_custom_cmd != []:
            if use_custom_cmd[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkUsecustomtoconnecttoserver')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkUsecustomtoconnecttoserver')
        custom_cmd = receiving_options_xml.gettagvalue ('customcommand')
        if custom_cmd != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txt0', custom_cmd[0])

        display_subscribed_folders = receiving_options_xml.gettagvalue ('displaysubscribedfoldersonly')
        if display_subscribed_folders != []:
            if display_subscribed_folders[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkShowonlysubscribedfolders')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkShowonlysubscribedfolders')
        overrider_server_folder_namespace = receiving_options_xml.gettagvalue ('overrideserverfoldernamespace')
        if overrider_server_folder_namespace != []:
            if overrider_server_folder_namespace[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkOverrideserver-suppliedfoldernamespace')
                namespace = receiving_options_xml.gettagvalue ('namespace')
                if namespace != []:
                    settextvalue ('frmEvolutionAccountAssistant', 'txt1', namespace[0])
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkOverrideserver-suppliedfoldernamespace')
        apply_filters = receiving_options_xml.gettagvalue ('applyfilters')
        if apply_filters != []:
            if apply_filters[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkApplyfilterstonewmessagesinINBOXonthisserver')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkApplyfilterstonewmessagesinINBOXonthisserver')
        check_junk = receiving_options_xml.gettagvalue ('checkjunk')
        if check_junk != []:
            if check_junk[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkChecknewmessagesforJunkcontents')
                check_inbox_junk = receiving_options_xml.gettagvalue ('checkinboxjunk')
                if check_inbox_junk != []:
                    if check_inbox_junk[0] == '1':
                        check ('frmEvolutionAccountAssistant', 'chkOnlycheckforJunkmessagesintheINBOXfolder')
                    else:
                        check ('frmEvolutionAccountAssistant', 'chkOnlycheckforJunkmessagesintheINBOXfolder')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkChecknewmessagesforJunkcontents')
        sync_remote_mail = receiving_options_xml.gettagvalue ('syncimapmail')
        if sync_remote_mail != []:
            if sync_remote_mail[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkAutomaticallysynchronizeremotemaillocally')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkAutomaticallysynchronizeremotemaillocally')
        time.sleep (1)
        # click forward button to move to next page
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)

    def configure_smtp (self, xmlfilename):
        sending_mail_xml = LdtpDataFileParser (xmlfilename)

        server_name = sending_mail_xml.gettagvalue ('smtpserver')
        if server_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtServer1', server_name[0])
        else:
            log ('SMTP server name missing', 'error')
            raise LdtpExecutionError (0)

        server_requires_auth = sending_mail_xml.gettagvalue ('serverrequiresauth')
        if server_requires_auth != []:
            if server_requires_auth[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkServerrequiresauthentication')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkServerrequiresauthentication')

        secure_connection = sending_mail_xml.gettagvalue ('smtpsecureconnection')
        if secure_connection != []:
            comboselect ('frmEvolutionAccountAssistant', 'cboUseSecureConnection1', secure_connection[0])

        password_type = sending_mail_xml.gettagvalue ('stmppasswordtype')
        if password_type != []:
            comboselect ('frmEvolutionAccountAssistant', 'cboType', password_type[0])

        user_name = sending_mail_xml.gettagvalue ('smtpusername')
        if user_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtUsername1', user_name[0])

        remember_password = sending_mail_xml.gettagvalue ('smtprememberpassword')
        if remember_password != []:
            if remember_password[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkRememberpassword1')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkRememberpassword1')
        time.sleep (1)

        # click forward button to move to next page
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)

    def authenticate_exchange (self, xmlfilename):
        auth_exchange_xml = LdtpDataFileParser (xmlfilename)
        click ('frmEvolutionAccountAssistant', 'btnAuthenticate')
        title_text = ''
        title = auth_exchange_xml.gettagvalue ('passwordtitle')
        if title != []:
            title_text = title[0]
        password_text = ''
        exchange_password = auth_exchange_xml.gettagvalue ('exchangepassword')
        if exchange_password != []:
            password_text = exchange_password[0]
        else:
            # Its not advaisable to test this scenario, so we are throwing an exception
            log ('password text empty', 'error')
            LdtpExecutionError (0)
        remember = False
        remember_passwd = auth_exchange_xml.gettagvalue ('rememberpassword')
        if remember_passwd != []:
            if remember_passwd[0] == '1':
                remember = True
            else:
                remember = False
        try:
            evolutionPass = EvoPassword ()
            evolutionPass.EnterPassword (password_text, remember, title_text)
        except LdtpExecutionError:
            log ('Unable to enter password', 'error')
            LdtpExecutionError (0)

    def configure_exchange_receiving_mail (self, xmlfilename):
        receiving_mail_xml = LdtpDataFileParser (xmlfilename)
        owa_url = receiving_mail_xml.gettagvalue ('OWAUrl')
        if owa_url != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtOWAUrl', owa_url[0])
        else:
            log ('Exchange OWA URL missing', 'error')
            raise LdtpExecutionError (0)
        exchange_user_name = receiving_mail_xml.gettagvalue ('exchangeusername')
        if exchange_user_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtUsername', exchange_user_name[0])
        else:
            log ('Exchange username missing', 'error')
            raise LdtpExecutionError (0)

        self.authenticate_exchange (xmlfilename)

        time.sleep (1)
        # click forward button to move to next page
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)
        
    def exchange_receiving_options (self, xmlfilename):
        receiving_options_xml = LdtpDataFileParser (xmlfilename)
        check_mail = receiving_options_xml.gettagvalue ('checkmail')
        if check_mail != []:
            if check_mail[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkAutomaticallycheckfornewmailevery')
                mail_check_interval = receiving_options_xml.gettagvalue ('mailcheckinterval')
                if mail_check_interval != []:
                    setvalue ('frmEvolutionAccountAssistant', 'sbtn0', mail_check_interval[0])
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkAutomaticallycheckfornewmailevery')
        gal_server_name = receiving_options_xml.gettagvalue ('galservername')
        if gal_server_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txt0', gal_server_name[0])
        limit_gal_response = receiving_options_xml.gettagvalue ('limitgal')
        if limit_gal_response != []:
            if limit_gal_response[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkLimitnumberofGALresponses')
                gal_limit_number = receiving_options_xml.gettagvalue ('gallimitnumber')
                if gal_limit_number != []:
                    setvalue ('frmEvolutionAccountAssistant', 'sbt0', gal_limit_number[0])
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkLimitnumberofGALresponses')
        password_expiry = receiving_options_xml.gettagvalue ('passwordexpiry')
        if password_expiry != []:
            if password_expiry[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkPasswordExpiryWarningperiod')
                password_expiry_period = receiving_options_xml.gettagvalue ('passwordexpiryperiod')
                if password_expiry_period != []:
                    setvalue ('frmEvolutionAccountAssistant', 'sbt0', password_expiry_period[0])
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkPasswordExpiryWarningperiod')
        apply_filters = receiving_options_xml.gettagvalue ('applyfilters')
        if apply_filters != []:
            if apply_filters[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkApplyfilterstonewmessagesinInboxonthisserver')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkApplyfilterstonewmessagesinInboxonthisserver')
        check_junk = receiving_options_xml.gettagvalue ('checkjunk')
        if check_junk != []:
            if check_junk[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkChecknewmessagesforJunkcontents')
                check_inbox_junk = receiving_options_xml.gettagvalue ('checkinboxjunk')
                if check_inbox_junk != []:
                    if check_inbox_junk[0] == '1':
                        check ('frmEvolutionAccountAssistant', 'chkOnlycheckforJunkmessagesintheINBOXfolder')
                    else:
                        check ('frmEvolutionAccountAssistant', 'chkOnlycheckforJunkmessagesintheINBOXfolder')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkChecknewmessagesforJunkcontents')
        sync_remote_mail = receiving_options_xml.gettagvalue ('syncexchangemail')
        if sync_remote_mail != []:
            if sync_remote_mail[0] == '1':
                check ('frmEvolutionAccountAssistant', 'chkAutomaticallysynchronizeaccountlocally')
            else:
                uncheck ('frmEvolutionAccountAssistant', 'chkAutomaticallysynchronizeaccountlocally')
        time.sleep (1)
        # click forward button to move to next page
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)

    def set_account_name (self, xmlfilename):
        acct_name_xml = LdtpDataFileParser (xmlfilename)
        acct_name = acct_name_xml.gettagvalue ('accountname')
        if acct_name != []:
            settextvalue ('frmEvolutionAccountAssistant', 'txtName', acct_name[0])
        # click forward button to move to next page
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)


    def select_time_zone (self, xmlfilename):
        time_zone_xml = LdtpDataFileParser (xmlfilename)
        time_zone = time_zone_xml.gettagvalue ('timezone')
        if time_zone != []:
            comboselect ('frmEvolutionAccountAssistant', 'cboTimeZoneCombobox', time_zone[0])
        # click forward button to move to next page
        if stateenabled ('frmEvolutionAccountAssistant', 'btnForward') == 1:
            click ('frmEvolutionAccountAssistant', 'btnForward')
        else:
            log ('Forward button not enabled', 'error')
            raise LdtpExecutionError (0)
        
    def apply_changes (self):
        time.sleep (1)
        # click apply button to save the account settings
        if stateenabled ('frmEvolutionAccountAssistant', 'btnApply') == 1:
            click ('frmEvolutionAccountAssistant', 'btnApply')
        else:
            log ('Apply button not enabled', 'error')
            raise LdtpExecutionError (0)

# Script execution starts here...
first_time_acct_setup = False

try:
    try:
        log ('Account setup', 'teststart')
        config_acct_xml = LdtpDataFileParser (datafilename)
        AcctSetup = EvolutionAccountSetup ()

        # First time account setup dialog title name is different
        setcontext ('Evolution Account Assistant', 'Evolution Setup Assistant')
        if guiexist ('frmEvolutionAccountAssistant') == 1:
            #do remap
            remap ('evolution', 'frmEvolutionAccountAssistant')
            first_time_acct_setup = True
        else:
            releasecontext ()

            # Needs to be done only when we have already accounts configured
            AcctSetup.create_new_account ()
            time.sleep (1)

        AcctSetup.enter_identify_info (datafilename)
        time.sleep (1)
        if first_time_acct_setup == True:
            # Undo remap
            undoremap ('evolution', 'frmEvolutionAccountAssistant')

        recv_type = config_acct_xml.gettagvalue ('recvservertype')
        if recv_type != []:
            comboselect ('frmEvolutionAccountAssistant', 'cboServerType', recv_type[0])
            if recv_type[0] == 'IMAP':
                time.sleep (2)
                # do remap
                remap ('evolution', 'frmEvolutionAccountAssistant')
                log ('Executing imap receiving mail configuration', 'info')
                AcctSetup.configure_imap_receiving_mail (datafilename)
                time.sleep (1)

                log ('Executing imap receiving options configuration', 'info')
                AcctSetup.imap_receiving_options (datafilename)
                time.sleep (1)

                # Undo remap
                undoremap ('evolution', 'frmEvolutionAccountAssistant')
            elif recv_type[0] == 'Microsoft Exchange':
                time.sleep (2)
                # do remap
                remap ('evolution', 'frmEvolutionAccountAssistant')
                log ('Executing Microsoft Exchange receiving mail configuration', 'info')
                AcctSetup.configure_exchange_receiving_mail (datafilename)
                time.sleep (1)

                log ('Executing Microsoft Exchange receiving options configuration', 'info')
                AcctSetup.exchange_receiving_options (datafilename)
                time.sleep (1)

                # Undo remap
                undoremap ('evolution', 'frmEvolutionAccountAssistant')

        time.sleep (1)
        # do remap
        remap ('evolution', 'frmEvolutionAccountAssistant')

        send_type = config_acct_xml.gettagvalue ('sendservertype')
        if send_type != []:
            comboselect ('frmEvolutionAccountAssistant', 'cboServerType1', send_type[0])
            if send_type[0] == 'SMTP':
                AcctSetup.configure_smtp (datafilename)
                time.sleep (1)

        AcctSetup.set_account_name (datafilename)
        time.sleep (1)

        if first_time_acct_setup == True:
            AcctSetup.select_time_zone (datafilename)

        AcctSetup.apply_changes ()

        # Undo remap
        undoremap ('evolution', 'frmEvolutionAccountAssistant')

        if first_time_acct_setup == True:
            releasecontext ()
        else:
            click ('dlgEvolutionSettings', 'btnClose')
    except error, msg:
        log ('' + str (msg), 'error')
        try:
            time.sleep (1)
            click ('frmEvolutionAccountAssistant', 'btnCancel')
            if first_time_acct_setup == True:
                releasecontext ()
            else:
                click ('dlgEvolutionSettings', 'btnClose')
            raise LdtpExecutionError (0)
        except error, msg:
            log ('' + str (msg), 'error')
            raise LdtpExecutionError (0)

    acct_name = config_acct_xml.gettagvalue ('accountname')
    setcontext ('Enter password','Enter Password for '+acct_name[0])
    if waittillguiexist ('dlgEnterpassword')!=1:
        log ('Password remainder window did not come up','warning')
        #raise LdtpExecutionError (0)
    else:
        password = config_acct_xml.gettagvalue ('password')
        if password != []:
            settextvalue ('dlgEnterpassword','txt0',password[0])
            check ('dlgEnterpassword','chkRememberthispassword')
            click ('dlgEnterpassword','btnOK')
        else:
            click ('dlgEnterpassword','btnCancel')
            time.sleep (2)
            if guiexist ('dlgEnterpassword')==1:
                click ('dlgEnterpassword','btnCancel')
    releasecontext()
except LdtpExecutionError:
    if first_time_acct_setup == True:
        releasecontext ()
    else:
        click ('dlgEvolutionSettings', 'btnClose')
    log ('Account setup', 'fail')
    log ('Account setup', 'testend')
    raise LdtpExecutionError (0)
log ('Account setup', 'pass')
log ('Account setup', 'testend')
