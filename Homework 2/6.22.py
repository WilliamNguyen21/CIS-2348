#William Nguyen
#1824617
ax = int(input())
ay = int(input())
az = int(input())
bx = int(input())
by = int(input())
bz = int(input())
k = False

for x in range (-10,11):
    for y in range (-10,11):
        if ax*x+ay*y==az and bx*x+by*y==bz:
            print (x,y)
            k = True
if k == False:
    print("No solution")
          
            
            
