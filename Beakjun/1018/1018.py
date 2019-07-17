import sys

sys.setrecursionlimit(10**5)

x_y = input()
x_y =  x_y.split(' ')
x_y =  [int(a) for a in x_y]
x = x_y[0]
y = x_y[1]




g_map = []

for ix in range(x):
    line = input()
    tmp = []
    for m in line:
        tmp.append(m)
    g_map.append(tmp)




def custom_slice_lst(gmap,xycut,start_x=0,start_y=0):
    res_lst = []
    for x in range(xycut):
            tx = x+start_x
            res_lst.append(gmap[tx][start_y:start_y+xycut])
    return res_lst



def reverse_spot(gmap,xymax,ix,iy,count):
    if(ix ==xymax-1 and iy==xymax-1):
        return count
    xmax=xymax
    ymax=xymax
    now = gmap[ix][iy]
    ano=""
    if(now =='B'):
        ano='W'
    else:
        ano='B'
        
    if(iy-1>=0 and gmap[ix][iy-1]==now):
        gmap[ix][iy-1]=ano
        count=count+1
        count = reverse_spot(gmap,xymax,ix,iy-1,count)
    if(iy+1<=ymax-1 and gmap[ix][iy+1]==now):
        gmap[ix][iy+1]=ano
        count=count+1
        count =reverse_spot(gmap,xymax,ix,iy+1,count)
    elif(iy+1<=ymax-1):
        count =reverse_spot(gmap,xymax,ix,iy+1,count)
            
        
    if(ix-1>=0 and gmap[ix-1][iy]==now):
        gmap[ix-1][iy]=ano
        count=count+1
        count =reverse_spot(gmap,xymax,ix-1,iy,count)    
    if(ix+1<=xmax-1 and gmap[ix+1][iy]==now):
        gmap[ix+1][iy]=ano
        count=count+1
        count =reverse_spot(gmap,xymax,ix+1,iy,count)
    elif(ix+1<=xmax-1):
        count =reverse_spot(gmap,xymax,ix+1,iy,count)    
    return count

count_list= []


def get_count_lst(gmap):
    x_y_grap_size = 8
    x_lst_len = len(gmap)-x_y_grap_size+1
    y_lst_len = len(gmap[0])-x_y_grap_size+1
    for ix in range(x_lst_len):
        for iy in range(y_lst_len):
            tmp_count=0
            sliced_gmap = custom_slice_lst(gmap,x_y_grap_size,ix,iy)
            tmp_count = reverse_spot(sliced_gmap,x_y_grap_size,0,0,0) 
            count_list.append(tmp_count)
get_count_lst(g_map)
print(min(count_list))
    
    
