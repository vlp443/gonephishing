import htmlmin
import base64

def minify_html(html):
    return htmlmin.minify(html, remove_empty_space=True)


def hex_encode_prefix(prefix, payload):
    encoded = payload.encode('utf-8').hex()
    return prefix + prefix.join(a + b for a, b in zip(encoded[::2], encoded[1::2]))


def js_hex_encode_all_chars(payload):
    return hex_encode_prefix("\\x", payload)

def url_encode_all_chars(payload):
    return hex_encode_prefix("%", payload)



def base64_encode_string(str):
    return base64.b64encode(str.encode()).decode()

def read_file(filename):
    with open(filename, 'r') as file:
        result = file.read()
        file.close()
    return result
