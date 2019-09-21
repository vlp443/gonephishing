# ultraphish (renaming as I need new features)


Simple tool to generate redirects from mail.google.com to any url that is searchable by google

### About
The OWASP top ten 2013 included A10-Unvalidated Redirects and Forwards with the following description:
Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation, attackers can redirect victims to phishing or malware sites, or use forwards to access unauthorized pages. 

This item does not appear in the top ten 2017

google.com has over 40 unsecured redirects  This is unlikely to change as google do not see it as a vulnerability. https://sites.google.com/site/bughunteruniversity/nonvuln/open-redirect


I would expect that the majority of users would trust a site if they were redirected via mail server domain that they were logged into.  This would then cause the user to be more likely to accept a squatted domain of the type described in the quiz below due to the fact that they trust the url via which they were redirected.
 https://phishingquiz.withgoogle.com/




### Usage
~~~
python3 ./googlePhish.py --url  https://cutecatsinhats.com/ 
~~~
Of course this is just for demo purposes and not to be used for evil.
