A=[10,20,30,40,50,60]
sum=0
i=1
for x in A:
    if i%2==0:
        sum+=x
    i=i+1
print(sum)