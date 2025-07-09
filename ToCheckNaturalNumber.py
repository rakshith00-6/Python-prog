num = int(input("Enter the number:"))

if num < 0:
    print("please Enter the positive Number")
else:
    sum = 0 
    while num > 0:
        sum +=num
        num -= 1
        
    print (num)
    