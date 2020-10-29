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
    spiderurl.write("spider-urls for " + sub)
    spiderurl.write("=" * (16 + len(str(sub))) + '\n')
    zap =ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})
    print('Spidering target {}'.format(sub))
    scanID = zap.spider.scan(sub)
    while int(zap.spider.status(scanID)) < 100:
            print('Spider progress %: {}'.format(zap.spider.status(scanID)))
            time.sleep(10) # time between check of progress
    print('Spider has completed!')
    urls= '\n'.join(map(str, zap.spider.results(scanID)))
    spiderurl.write(urls)
    spiderurl.write('\n' + ("=" * 100) + '\n')
    print('Active Scanning target {}'.format(sub))
    scanID = zap.ascan.scan(sub)
    while int(zap.ascan.status(scanID)) < 100:
        # Loop until the scanner has finished
        print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
        time.sleep(5)

    print('Active Scan completed')
    # Print vulnerabilities found by the scanning
    print('Hosts: {}'.format(', '.join(zap.core.hosts)))
    print('Alerts: ')
    print(zap.core.alerts(baseurl=sub))

	
