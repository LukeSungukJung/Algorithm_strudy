#entire_case_count = int(input())
import math 
def isAincludeB(a,b):
    Ax=a['x']
    Bx=b['x']

    Ay=a['y']
    By=b['y']
    
    Ar= a['r']
    Br= b['r']
    
    dis = math.sqrt((Ax-Bx)**2+(Ay-By)**2)
    if(Ar>dis and (Ar > Br)):
        return True
    return False;
        


start_end_point =input().split(" ")

start_x_y =  (int(start_end_point[0]),int(start_end_point[1]))
end_x_y =    (int(start_end_point[2]),int(start_end_point[3]))
planet_counts = int(input())

planets = []

for a in range(planet_counts):
    x_y_r_point =input().split(" ")
    x =int(x_y_r_point[0])
    y =int(x_y_r_point[1])
    r =int(x_y_r_point[2])
    planets.append({'x':x,'y':y,'r':r})
    
    
    
