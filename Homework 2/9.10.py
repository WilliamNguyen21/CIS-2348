#William Nguyen
#1824617
import csv

with open(input(),'r') as wordsfile:
    words = csv.reader(wordsfile)
    for r in words:
        wordlist=r
xlist=list(dict.fromkeys(wordlist))
length = len(xlist)

for i in range(length):
    print(xlist[i],wordlist.count(xlist[i]))

    
