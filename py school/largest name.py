list=eval(input("enter the names:"))
comp_var=''
for i in range (len(list)):
    if list[i]>comp_var:
        comp_var=list[i]
print(comp_var)