

count =input()



memoization = []
key_memoization = []

def fibo(number):
    if(number ==0):
        zero_ones_count[0]=zero_ones_count[0]+1
        return 0
    elif(number ==1):
        zero_ones_count[1]=zero_ones_count[1]+1
        return 1
    else:
        if((number-1) in key_memoization):
            kidx = key_memoization.index((number-1))
            zero_ones_count[0] = memoization[kidx][0]+zero_ones_count[0]
            zero_ones_count[1] = memoization[kidx][1]+zero_ones_count[1]
        else:
            fibo(number-1)
        if((number-2) in key_memoization):
            kidx = key_memoization.index((number-2))
            zero_ones_count[0] = memoization[kidx][0]+zero_ones_count[0]
            zero_ones_count[1] = memoization[kidx][1]+zero_ones_count[1]
        else:
            fibo(number-2)
        if(number not in key_memoization):
            key_memoization.append(number)
            memoization.append((zero_ones_count[0],zero_ones_count[1]))
       

#num = int(input())

#trash =fibo(num)
#print(zero_ones_count[0]," ",zero_ones_count[1])
res = []
for a in range(int(count)): 
    zero_ones_count =[0,0]
    num = int(input())
    fibo(num)
    res.append((zero_ones_count[0],zero_ones_count[1]))

for r in res:
    print(r[0],r[1])
