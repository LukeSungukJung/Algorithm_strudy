num = input()
input_list = []

for one in range(int(num)):

    new_oneint=int(input())
    if(len(input_list)>=1):
        for list_index,ip_one in enumerate(input_list):
            if(new_oneint<ip_one):
                input_list.insert(list_index,new_oneint)
                break;
        input_list.append(new_oneint)
    else:
        input_list.append(new_oneint)
        
                
                
                
        
now_index=0
roop_index=0

        
for i in input_list:
    print(i)


#input_list.sort()