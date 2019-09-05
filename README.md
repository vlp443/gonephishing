# googlePhish

Simple tool to generate redirects from mail.google.com to any url that is searchable by google

### Abstract
The OWASP top ten 2013 included A10-Unvalidated Redirects and Forwards with the following description:
Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation, attackers can redirect victims to phishing or malware sites, or use forwards to access unauthorized pages. 

This item does not appear in the top ten 2017

google.com has over 40 unsecured redirects, so I have created this tool to generate encoded links from mail.google.com to a passed in location.  

Of course it is intended purely for demonstration purposes.

For googles take see https://sites.google.com/site/bughunteruniversity/nonvuln/open-redirect

I thought the google phishing quiz was worth adding as it pushes the point of hovering over the link and checking the domain in the browser status bar.  

https://phishingquiz.withgoogle.com/

I would expect that the majority of users would trust a site if they were redirected via mail server domain that they were logged into.  This would then cause the user to be more likely to accept a squatted DNS of the type described in the phishingquiz above due to the fact that they trust the redirector.

### Usage
~~~
python3 ./googlePhish.py --url https://pixabay.com/images/search/kitten/
~~~
