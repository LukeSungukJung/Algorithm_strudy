num = input()
input_list = []

for one in range(int(num)):
    input_list.append(int(input()))
input_index_list = [False]*int(num) 
now_index=0
roop_index=0

while False in input_index_list:
    if(now_index<int(num)-1):
        if(input_list[now_index]>input_list[now_index+1]):
            temp = input_list[now_index]
            input_list[now_index] = input_list[now_index+1]
            input_list[now_index+1] =temp
            now_index+=1
        else:
            input_index_list[now_index]=True
            if(False not in input_index_list):
                break
            else:
                now_index = input_index_list.index(False)
    else:
        input_index_list[now_index]=True
        now_index = input_index_list.index(False)
        
for i in input_list:
    print(i)