import htmlmin
import base64

def minify_html(html):
    return htmlmin.minify(html, remove_empty_space=True)


def url_encode_all_chars(url):
    encoded = url.encode('utf-8').hex()
    return '%' + '%'.join(a+b for a,b in zip(encoded[::2], encoded[1::2]))

def base64_encode_string(str):
    return base64.b64encode(str.encode()).decode()

def read_file(filename):
    with open(filename, 'r') as file:
        result = file.read()
        file.close()
    return result
