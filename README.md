# zap-hunt
a collection of bash script and python to automate ZAP Security Tests 


# Installation 
you need to install (zaproxy ,  httprobe , subfinder , OWASP ZAP Python API) 


  * [zaproxy](https://www.zaproxy.org/)
  * [httprobe](https://github.com/tomnomnom/httprobe)
  * [subfinder](https://github.com/projectdiscovery/subfinder)
  * [OWASP ZAP Python API](https://github.com/zaproxy/zap-api-python)




you need  to change api key and the port ZAP runs on (defaults to 8080) on zspider.py line 8 , 22  
 
 ```python
import time
from zapv2 import ZAPv2
import os
from pprint import pprint
import pyfiglet

spidersub = open("https-subs.txt", "r") #the file contain subdomains you want to spider 
apikey = 'olg7ai1777h7ff0353gafnok9l' # you can get this from tools > option > apikey

#can't have a python script without a cool logo :D
word = pyfiglet.figlet_format("zap-hunt")

print (word )

for sub in spidersub :
    sub1=sub.strip()
    joined = os.path.join(sub1[8:] +".txt")
    spiderurl = open('./spiderurl/' + joined, "a+")
    spiderurl.write("spider-urls for " + sub)
    spiderurl.write("=" * (16 + len(str(sub))) + '\n')
    zap =ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})
```

# Usage 

* > git clone https://github.com/hamddy/zap-hunt.git
* > cd zap-hunt && sudo chmod +x zap-hunt.sh zspider.py
* > ./zap-hunt.sh  "your subdomain here"
 
 
 
# Reccommendations

* DO NOT USE ZAProxy or this ZAProxy automation tools collection to hack web sites and web applications you don't own or you don't have a written permission to pen-test.

* I do not assume any responsabilities for your actions, nor for the content of this repository.

* This automation tools collection sole purpose is to help people (especially the ones who can't afford expensive security solutions) to test security of their web applications and web sites to improve the quality and security of this world and not to make it worst!


