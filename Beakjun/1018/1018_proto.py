import sys

sys.setrecursionlimit(10**5)

x_y = input()
x_y =  x_y.split(' ')
x_y =  [int(a) for a in x_y]
x = x_y[0]
y = x_y[1]

WB_board = [['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],
            ['B','W','B','W','B','W','B','W']]

BW_board =  [[ 'B','W','B','W','B','W','B','W' ],
             [ 'W','B','W','B','W','B','W','B' ],
			 [ 'B','W','B','W','B','W','B','W' ],
             [ 'W','B','W','B','W','B','W','B' ],
			 [ 'B','W','B','W','B','W','B','W' ],
		     [ 'W','B','W','B','W','B','W','B' ],
			 [ 'B','W','B','W','B','W','B','W' ],
			 [ 'W','B','W','B','W','B','W','B' ]]

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


count_list= []

def compare_maps(sliced_gmap):
    tmp_count=0
    if(BW_board==sliced_gmap or WB_board == sliced_gmap):
        count_list.append(tmp_count)
    else:
        w_tmp=0
        for ix,xlst in enumerate(sliced_gmap):
            for iy,ele in enumerate(xlst):
                if(WB_board[ix][iy]!=ele):
                    w_tmp=w_tmp+1
        b_tmp=0
        stop=False
        for ix,xlst in enumerate(sliced_gmap):
            if(stop):
                break
            for iy,ele in enumerate(xlst):
                if(BW_board[ix][iy]!=ele):
                    b_tmp=b_tmp+1     
                    if(b_tmp>w_tmp): 
                        stop=True
                        break
        count_list.append(min(b_tmp,w_tmp))
def get_count_lst(gmap):
    x_y_grap_size = 8
    x_lst_len = len(gmap)-x_y_grap_size+1
    y_lst_len = len(gmap[0])-x_y_grap_size+1
    
    for ix in range(x_lst_len):
        for iy in range(y_lst_len):
            sliced_gmap = custom_slice_lst(gmap,x_y_grap_size,ix,iy)
            compare_maps(sliced_gmap)
    
get_count_lst(g_map)
print(min(count_list))
