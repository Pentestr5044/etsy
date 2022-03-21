#imports first
import time
import urllib3
import certifi
#define argparse argument for threads
#define variables
http = urllib3.PoolManager(ca_certs=certifi.where())
url = input("enter url: ")
#user agent randomized per request
#Origin header to cycle through proxy IP, localhost IP, and target ip range.

#define our functions
#function 1 wordlist definition/generator


attack_field0 = input("please enter file location: ")
attack_field1 = open(attack_field0,"rb")
attack_field = attack_field1.readlines()
#headers = open("./useragents.txt", 'r')
v = 0
#function 3 iteration and threading
if len(attack_field) > 0:
    if v < len(attack_field):
        attacks = []
        this = attack_field
        for i in this:
            this1 = str(i).strip('b\'')
            this2 = this1.strip('\\r\\n')
            attacks.append(this2)
        for attempts in attacks:
            url1 = url + attempts
        # for header in headers:
            try:
                r = http.request("GET", url1, retries=False)
                if r.status == 200:
                    print("found")
                    print(r.status)
                    print(url1)
                elif r.status == 403:
                    print("found")
                    print(r.status)
                    print(url1)
                elif r.status == 500:
                    print("found")
                    print(r.status)
                    print(url1)
                else:
                    print()
            except urllib3.exceptions.NewConnectionError:
                print()
                time.sleep(2)
    time.sleep(5)
    v += 1
