
GomTang = int(input())

bag_3 = 3
bag_5 = 5
OriginG = GomTang
def makeHappySangGun(GomTang):
    count3bag=0
    if(GomTang%bag_5 ==0  and (GomTang%bag_5)%bag_3 ==0):
        return GomTang//bag_5
    else:
        while(GomTang>0):
            GomTang-=bag_3
            count3bag+=1
            if(GomTang%bag_5==0):
                return count3bag+GomTang//bag_5
                    
                
        return -1

print(makeHappySangGun(GomTang))

#3 6 9 2 5 8 1 4 7 0 

#for a in range(3,5000):
#    print(makeHappySangGun(a))
