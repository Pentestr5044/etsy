#imports first
import time
import urllib3
import certifi
#define argparse argument for threads
#define variables
http = urllib3.PoolManager(ca_certs=certifi.where())
url = "https://www.etsy.com/"
words = []
assetFuzz = "./assetnoteslist.txt"
wordlistBase3 = "./actionwords.txt"
wordlistBase1 = "./massivewordlist.txt"
directories1 = "./directories.txt"
#user agent randomized per request
#Origin header to cycle through proxy IP, localhost IP, and target ip range.

#define our functions
#function 1 wordlist definition/generator


def wordlist_builder(wordlistBase1, wordlistBase3, directories1, assetFuzz):
    wf3 = open(assetFuzz, "rb")
    wf1 = open(wordlistBase3, "rb")
    wf = open(wordlistBase1, "rb")
    wf2 = open(directories1, "rb")
    fuzz = wf3.readlines()
    baseWords = wf.readline()
    actionWords = wf1.readlines()
    directories = wf2.readlines()
    for i in fuzz:
        words.append(i)
    wf3.close()
    for i in baseWords:
        words.append(i)
    wf.close()
    for i in actionWords:
        words.append(i)
    wf1.close()
    for i in directories:
        words.append(i)
    wf2.close()
    return words


attack_field = wordlist_builder(wordlistBase1, wordlistBase3, directories1, assetFuzz)
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
