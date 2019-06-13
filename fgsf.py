a1,b1=map(int,input().split())
for n1 in range(a1+1,b1):
  temp=n1
  sum=0
  while(temp!=0):
    a1=temp%10
    sum=sum+a1**3
    temp=temp//10
  if(n1==sum):
    print(n1,end=' ')
