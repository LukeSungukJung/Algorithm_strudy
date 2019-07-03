import sys
sys.setrecursionlimit(10**6)


farm_count = int(input())


farm_list =[]

tuple_index_lst = []

for ch in range(farm_count):
    wid_hei_cabb =  input()
    wid_hei_cabb= wid_hei_cabb.split(' ')
    wid_hei_cabb =  [ int(ele) for ele in wid_hei_cabb ]
    cabb_count = wid_hei_cabb[2] 
    farm = [] 
    for a in range(wid_hei_cabb[0]+2):
       farm.append([0]*(wid_hei_cabb[1]+2))   
    for i in range(cabb_count):
       tmp_index = input()
       tmp_index = tmp_index.split(' ')
       tmp_index =[int(ele) for ele in tmp_index]
       farm[tmp_index[0]+1][tmp_index[1]+1] = 1
    farm_list.append(farm)
    
    
    
    


white_bug_count =0;

def find_bfs_cabbage(i,j,farm):
    if(farm[i+1][j]==1):
        farm[i+1][j]=-1
        find_bfs_cabbage(i+1,j,farm)
    if(farm[i-1][j]==1):
        farm[i-1][j]=-1
        find_bfs_cabbage(i-1,j,farm)
    if(farm[i][j+1]==1):
        farm[i][j+1]=-1
        find_bfs_cabbage(i,j+1,farm)
    if(farm[i][j-1]==1):
        farm[i][j-1]=-1
        find_bfs_cabbage(i,j-1,farm)
    return ;
        

for farm in farm_list:
    white_bug_count =0;
    for i,ilst in enumerate(farm):
        for j,ele in enumerate(ilst):
            if(ele==1):
                farm[i][j]=-1
                white_bug_count=white_bug_count+1
                find_bfs_cabbage(i,j,farm)

    print(white_bug_count)

    
    
"""

"""
