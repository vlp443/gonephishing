# googlePhish

Simple tool to generate redirects from mail.google.com to any url that is searchable by google

### Abstract
The OWASP top ten 2013 included A10-Unvalidated Redirects and Forwards with the following description:
Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation, attackers can redirect victims to phishing or malware sites, or use forwards to access unauthorized pages. 

This item does not appear in the top ten 2017

google.com has over 40 unsecured redirects, so I have created this tool to generate encoded links from mail.google.com to a passed in location.  

Of course it is intended purely for demonstration purposes.

### Usage
~~~
python3 ./googlePhish --url https://www.pets4homes.co.uk/sale/cats
~~~
