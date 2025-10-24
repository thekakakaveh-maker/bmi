name_list=[]
while True:
    name = input("enter your name:")
    if name == "exit" :
     break
    else:
       name_list.append(name)
print(name_list)