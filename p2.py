arr=[100,101,100,102,101,103]
freq=[0]*4
for i in arr:
    freq[i-100]+=1
print(freq)
        