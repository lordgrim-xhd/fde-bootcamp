i=1
j=1
while i<=10:
    
    print(i)
    i+=1
total=0
while j<=100:
    
    total=total+j
    j+=1
print(total)
password = "fde123"
count = 0

while count < 3:
    print(f"请输入密码")
    password_1=input()
    if password_1==password:
        print(f"登录成功")
        break
    else:
        count+=1
        
        print(f"密码错误，还剩 {3 - count} 次机会") 
if  count==3:
    print(f"账号锁定")
