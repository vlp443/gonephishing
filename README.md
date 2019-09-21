# ultraphish (renaming as I need new features)


Simple tool to generate phishing urls.  Of course this is just for demo purposes and not to be used for evil.

### Requires

pip3 install htmlmin

### Usage

#### Reflected XSS
This is all very new so treat it gently. It may not have long to go (chrome browser security for example)

 * Generate a minified version of an html file and optionally base64 encode it (on by default, as it will be in most use cases so you can switch it off on the command line --base64 0), then inject it into some javascript/html and urlencode the entire string.  The javascript must contain a %s field to mark location to inject html into.  

~~~
python3 ./ultraphish.py --xss --html "@./text.html" --js '<script>document.body.innerHTML=atob("%s")</script>'
~~~

#### GMAIL Redirect

~~~
python3 ./ultraphish.py --gmail  --dest https://cutecatsinhats.com/ 
~~~


### About
The OWASP top ten 2013 included A10-Unvalidated Redirects and Forwards with the following description:
Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation, attackers can redirect victims to phishing or malware sites, or use forwards to access unauthorized pages. 

This item does not appear in the top ten 2017

google.com has over 40 unsecured redirects  This is unlikely to change as google do not see it as a vulnerability. https://sites.google.com/site/bughunteruniversity/nonvuln/open-redirect


I would expect that the majority of users would trust a site if they were redirected via mail server domain that they were logged into.  This would then cause the user to be more likely to accept a squatted domain of the type described in the quiz below due to the fact that they trust the url via which they were redirected.
 https://phishingquiz.withgoogle.com/



