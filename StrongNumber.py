def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)
    
def strong_num(num):
    sum=0
    temp=num
    while temp>0:
        digit=fact(temp%10)
        sum=sum+digit
        temp=temp//10
    if sum==num:
        print(num,"is strong number")
    else:
        print(num,"is not strong number")