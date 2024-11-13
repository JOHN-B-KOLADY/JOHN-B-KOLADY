p_list=[]
name=eval(input("enter the names:"))
for i in range (len(name)):
    if name[i][0]=="s":
        print(name[i])
        p_list.append(name[i])
print(p_list)