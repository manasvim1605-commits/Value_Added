arr=[-4,-2,1,0,-2,1,3,-4]
freq=[0]*8
for i in arr:
    freq[i+4]+=1
print(freq)
