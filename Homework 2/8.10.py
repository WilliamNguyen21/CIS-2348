#William Nguyen
#1824617
x = str(input())
y = str("")
for i in range(len(x)):
    y += x[len(x)-1-i]
if x.replace(" ","") == y.replace(" ",""):
    print (x + " is a palindrome")
else: print (x + " is not a palindrome")
