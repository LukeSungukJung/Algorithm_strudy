

def get_pattern_and_ans(a,b):
    patt_lst = []
    for n in range(1,b+1):
        sab = int(str(a**n)[-1])
        if(len(patt_lst)==0):
            patt_lst.append(sab)
            
        elif(sab not in patt_lst):
            patt_lst.append(sab)
        else:
            return patt_lst
    patt_lst.append(a**b)
    return patt_lst
            

tri = int(input())
res_lst = []
for a in range(tri):
    a_b = input()
    a_b = a_b.split()
    a =  int(a_b[0])
    b =  int(a_b[1])
    patt_lst = get_pattern_and_ans(a,b)
    patt_lst_len =  len(patt_lst)
    if(patt_lst_len==0):
        res_index = b%patt_lst_len
    else:
        res_index = b%patt_lst_len-1
    if(patt_lst[res_index]==0):
        res_lst.append(10)
    else:
        res_lst.append(patt_lst[res_index])
    

for res in res_lst:
    print(res)
 
    