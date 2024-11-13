list=eval(input("enter the input"))
comp_no_lar=0
comp_no_small=list[0]
for i in range(len(list)):
    if list[i]>comp_no_lar:
        comp_no_lar=list[i]
    if list[i]<comp_no_small:
        comp_no_small=list[i]
print("the smallest one is",comp_no_small,"largest one is ",comp_no_lar)