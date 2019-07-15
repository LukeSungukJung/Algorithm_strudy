
begin_number = int(input("start:"))
last_number = int(input("last:"))+1
num_list =  list(range(begin_number,last_number))
clone_list = num_list.copy()
two =  2
three = 3
five = 5
seven = 7 
pop_index =[]

for num in (clone_list):
    
    if num%2==0:
        if(num==2):
            continue
        num_list.remove(num)
        continue
    if num%3==0:
        if(num==3):
            continue
        num_list.remove(num)
        continue
    if num%5==0:
        if(num==5):
            continue
        num_list.remove(num)
        continue
    if num%7==0:
        if(num==7):
            continue
        num_list.remove(num)
        continue

def print_eratos(lst):
    sstr =""
    for idx,ele in enumerate(lst):
        idx=idx+1
        sstr= sstr + " " + str(ele)
        if(idx%5==0):
            sstr= sstr+"\n"
    print(sstr)

print_eratos(num_list)