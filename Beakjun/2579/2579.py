import sys
sys.setrecursionlimit(10**6)

num = int(input())

stair_list = []
stair_status = []
last_index = num-1
consecutive_maximum=2;
consecutive_status=0;
max_sum=0

for idx in range(num):
    stair_list.append(int(input()))


def get_max_val(stairs,total,consecutive_status,now,end):
    step=1
    if(now>end):
        return 0;
    elif(now==end-1 and consecutive_status==2):
        return 0;
    if(now==end):
        consecutive_status+=1
        if(consecutive_status>consecutive_maximum):
           # print("fail_res:",consecutive_status)
            return 0;
        #print("res:",consecutive_status)
        return (total+stairs[now])
    
    if(consecutive_status==consecutive_maximum):
        #print("cmax",consecutive_status,",",consecutive_status,"now",now)
        now+=1
        consecutive_status=0
        if(now>end):
            return 0;
    total+=stairs[now]
    #print(total,",",stairs[now],"now:",now,",","end",end,"con",consecutive_status)
    now=now+step
    consecutive_status+=1
    if(now==end):
        consecutive_status+=1
        if(consecutive_status>consecutive_maximum):
            #print("fail_res:",consecutive_status)
            return 0;
        #print("res:",consecutive_status)
        return (total+stairs[now])
    
    
    return max(get_max_val(stairs,total,consecutive_status,now,end),get_max_val(stairs,total,consecutive_status,now+1,end))
    

print(get_max_val(stair_list,0,0,0,num-1))