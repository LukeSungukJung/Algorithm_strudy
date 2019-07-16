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


count = 0

def custom_slice_lst(gmap,xycut,start_x=0,start_y=0):
    res_lst = []
    for x in range(xycut):
            tx = x+start_x
            res_lst.append(gmap[tx][start_y:start_y+xycut])
    return res_lst


def reverse_spot(gmap):
    x_lst = len(gmap)
    y_lst = len(gmap[0])
    x_y_grap_size = 8
    sliced_map = []