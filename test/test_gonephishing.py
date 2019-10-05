import unittest

import xssutils


class TestXssutils(unittest.TestCase):

    def test_it_minifies_html(self):
        html = """<html>
                        <table>
                            <tr><td>hello</td></tr>
                        </table>
                    </html>
        """
        self.assertEqual(xssutils.minify_html(html), '<html><table><tr><td>hello</td></tr></table></html>');

    def test_it_url_encodes_all_chars(self):
        str="https://asdfghj+-%20aaaaaa";
        self.assertEqual(xssutils.pcnt_encode_all_chars(str), '%68%74%74%70%73%3a%2f%2f%61%73%64%66%67%68%6a%2b%2d%25%32%30%61%61%61%61%61%61')

    def test_it_hex_encodes_all_chars(self):
        str="https://asdfghj+-%20aaaaaa";
        self.assertEqual(xssutils.js_hex_encode_all_chars(str), '\\x68\\x74\\x74\\x70\\x73\\x3a\\x2f\\x2f\\x61\\x73\\x64\\x66\\x67\\x68\\x6a\\x2b\\x2d\\'
                                                                'x25\\x32\\x30\\x61\\x61\\x61\\x61\\x61\\x61')


    def test_it_base64_encodes_strings(self):
        str="something to say here";
        self.assertEqual(xssutils.base64_encode_string(str), 'c29tZXRoaW5nIHRvIHNheSBoZXJl')

    def test_it_reads_files(self):
        self.assertEqual(xssutils.read_file('test.txt'), "this is a test\nadf")