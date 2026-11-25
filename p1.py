arr=[100,101,100,102,101,100]
cnt={}
for i in arr:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
print(cnt)
        