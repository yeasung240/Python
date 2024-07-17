# multiple of 3 is the sum of all digit should be multiple of 3
# multiple of 10 is the last digit is 0 


lis = []
a = input()
for i in a:
    lis.append(int(i))
    
sun = 0 
for i in lis:
    sun += i 

    
if 0 in lis and (counter % 3 == 0):
    lis.sort(reverse = True)
    for i in lis:
        print(i,end = '')
else:
    print(-1)
