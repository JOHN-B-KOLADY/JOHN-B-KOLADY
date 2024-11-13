list=eval(input("enter the numbers:"))
for i in range (len(list)):
    if list[i]%3==0 and list[i]%5==0:
        list.remove(list[i])
print(list)