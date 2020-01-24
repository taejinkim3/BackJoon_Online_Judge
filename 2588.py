x,y=map(int,input().split())

result1=x*((y%100)%10)
result2=x*((y%100)//10)
result3=x*(y//100)
res=x*y
print(result1,result2,result3,res,sep='\n')
print('hello world',end=" ")
print('hello world2')