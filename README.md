# gonephishing


Generate phishing urls for demos and fun (serious security research).

### clone

git clone --recurse-submodules https://github.com/vlp443/gonephishing.git

### Requires

pip3 install htmlmin

### Usage

#### Reflected XSS
This is all very new so treat it gently. It may not have long to go (chrome browser security blocks the examples given Firefox is ok IE/Edge probably okay not tested yet)

 Generate a minified version of an html file and optionally encode it then inject it into some javascript/html and urlencode the entire string.  
 
 The javascript must contain a %s field to mark location to inject html into.  
 
 Current supported encoders are b64 (base64) and hex ('\xAA\xBB' etc).

~~~
python3 ./gonephishing.py --xss --html "@./text.html" --js '<script>document.body.innerHTML=atob("%s")</script>'  --encoders --encoders b64

python3 ./gonephishing.py --xss --html "@./text.html" --js '<script>document.body.innerHTML=("%s")</script>'  --encoders --encoders hex

python3 ./gonephishing.py --xss --html "@./text.html" --js '<script>document.body.innerHTML=atob("%s")</script>'  --encoders --encoders b64,hex 
~~~
Paste the generated link into the vulnerable request parameter and the page should be overwritten with the supplied html.


#### GMAIL Redirect

~~~
python3 ./gonephishing.py --gmail  --dest https://cutecatsinhats.com/ 
~~~


### About
The OWASP top ten 2013 included A10-Unvalidated Redirects and Forwards with the following description:
Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation, attackers can redirect victims to phishing or malware sites, or use forwards to access unauthorized pages. 

This item does not appear in the top ten 2017

google.com has over 40 unsecured redirects  This is unlikely to change as google do not see it as a vulnerability. https://sites.google.com/site/bughunteruniversity/nonvuln/open-redirect


I would expect that the majority of users would trust a site if they were redirected via mail server domain that they were logged into.  This would then cause the user to be more likely to accept a squatted domain of the type described in the quiz below due to the fact that they trust the url via which they were redirected.
 https://phishingquiz.withgoogle.com/



