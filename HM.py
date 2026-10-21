n=9767805016
freq=[0]*10
while(n!=0):
    ld=n%10
    freq[ld]+=1
    n//=10
print(freq)

#def countfreq(n):
#   freq=[0]*10
#   while(n!=0):
#      ld=n%10
#     freq[ld]+=1
#      n//=10
#   return freq
# n=9767805016
#res= countfreq(n)
#for i in range (len(res)):
#   print(f"{i}->{res[i]}")
