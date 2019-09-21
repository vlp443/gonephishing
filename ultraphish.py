from argument_manager import parser
from argument_manager.parser import ParameterError, ActionError
import  sys

print (""" _   _ _    ___________  ___ ______ _   _ _____ _____ _   _ 
| | | | |  |_   _| ___ \/ _ \| ___ \ | | |_   _/  ___| | | |
| | | | |    | | | |_/ / /_\ \ |_/ / |_| | | | \ `--.| |_| |
| | | | |    | | |    /|  _  |  __/|  _  | | |  `--. \  _  |
| |_| | |____| | | |\ \| | | | |   | | | |_| |_/\__/ / | | |
 \___/\_____/\_/ \_| \_\_| |_|_|   \_| |_/\___/\____/\_| |_/
                                                            
                                                            """)


def url_encode_all_chars(url):
    encoded = url.encode('utf-8').hex()
    return '%' + '%'.join(a+b for a,b in zip(encoded[::2], encoded[1::2]))

def gmail_redirect(values):
    print("https://mail.google.com/webhp#?uid=Z2l0aHViLmNvbS92bHA0NDM=&q=%s=&btnI=I" % url_encode_all_chars(values.get_dest()))


argManager = parser.get_manager()\
    .add_value('--dest', metavar='Destination URL (for gmail)', nargs=1)

argManager.add_action(argManager.print_help, '--help', help='Show this message', action='store_true')\
    .add_action(gmail_redirect, '--gmail', help='Redirect vial mail.google.com', action='store_true')

try:
    if len(sys.argv) > 1:
        argManager.exec()
    else:
        argManager.print_help()

except (ParameterError) as e:
    if argManager.get_current_action() is None:
        print('Input parameter Error: "%s"' % e)
    else:
        print('Input parameter Error: "%s" while executing the %s command: ' % e, argManager.get_current_action())

except ActionError as e:
    print("Action Error: " +  str(e))