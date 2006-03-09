from evoutils.mail import *

# Read input from file
data_object = LdtpDataFileParser (datafilename)
view_component = data_object.gettagvalue ('view_component')

try :
	log ('Change Compoent', 'teststart')

	if get_window (view_component[0]) == 0:
		log ('Change Component', 'fail')
	log ('Change Component', 'pass')
        log ('Change Compoent','testend')

except:
         log('Unable to change component','error')
         log('Change Compoent','testend')
         raise LdtpExecutionError(0)


