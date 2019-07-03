import sys
sys.setrecursionlimit(10**6)

row_cols_inputs = input()

row_cols_inputs =  row_cols_inputs.split(' ')
row_cols_inputs =  [int(rc) for rc in row_cols_inputs]

row=row_cols_inputs[0]
col=row_cols_inputs[1]

mine = []

for r in range(row):
    line = input()
    each_line = []
    for ele in line:
        each_line.append(ele)
    mine.append(each_line)

mine.reverse()

attck_count =int(input())
attck_points = input()
attck_points = attck_points.split(' ')
attck_points =[int(atk)-1 for atk in attck_points]

def recover_mine(mine):
    for i,ilst in enumerate(mine):
        for j,ele in enumerate(ilst):
            if(ele=='o'):
                mine[i][j]='x'
            

def attck_mineral(atk_point,mine,turn):
    if(turn==0):
        for j,_ in enumerate(mine[atk_point]):
            if(mine[atk_point][j]=='x'):
                mine[atk_point][j]='.'
                return mine
    else:
        mine[atk_point].reverse()
        for j,_ in enumerate(mine[atk_point]):
            if(mine[atk_point][j]=='x'):
                mine[atk_point][j]='.'
                mine[atk_point].reverse()
                return ;
        mine[atk_point].reverse()
    return ;

def dfs_is_not_collapse(i,j,mine):
     if(i-1>=0):
        if(mine[i-1][j]=='x'):
            mine[i-1][j]='o'
            dfs_is_not_collapse(i-1,j,mine)
     if(i+1<row):
         if(mine[i+1][j]=='x'):
            mine[i+1][j]='o'
            dfs_is_not_collapse(i+1,j,mine)   
     if(j-1>=0):
        if(mine[i][j-1]=='x'):
            mine[i][j-1]='o'
            dfs_is_not_collapse(i,j-1,mine)
     if(j+1<col):
         if(mine[i][j+1]=='x'):
            mine[i][j+1]='o'
            dfs_is_not_collapse(i,j+1,mine)
     return ;

def collapse_mineral_dfs(mine,i,j,distance,visited_lst):
     visited_lst.append((i,j))
     mine[i][j] = '.'
     if(i-1>=0):
        if(mine[i-1][j]=='x'):
            collapse_mineral_dfs(mine,i-1,j,distance,visited_lst)
     if(i+1<row):
         if(mine[i+1][j]=='x'):
            collapse_mineral_dfs(mine,i+1,j,distance,visited_lst)   
     if(j-1>=0):
        if(mine[i][j-1]=='x'):
            collapse_mineral_dfs(mine,i,j-1,distance,visited_lst)
     if(j+1<col):
         if(mine[i][j+1]=='x'):
            collapse_mineral_dfs(mine,i,j+1,distance,visited_lst)   
            
"""
def exceed_distance(mine,i,j):
    for btm in range(len(i)):
        if(mine[btm][j]=='x'):
            if(mine[btm+1]=='x'):
                continue
            return i-btm
    
            
def get_dropped_distance(mine,visited_i_js):
    first_line= [] 
    for i_j in visited_i_js:
    if(len(first_line)==0):
        first_line.append(i_j)

    distance= min()
            
"""                
                

def collapse_chk(mmine):
    duple_mine = mmine.copy()
    collapse_coeff = 0
    collapse_points =[]
    collapse=False
    btm_i=0
    for i, ilst in enumerate(duple_mine):
        if(len(collapse_points)!=0): 
            break
        
        for j,btm in enumerate(ilst):
            if(btm=='x'):
                if(collapse_coeff!=0):
                    if(i>0):
                        collapse_coeff=collapse_coeff+1 
                        collapse=True
                        collapse_points.append((i,j))
                        break
                if(duple_mine[btm_i][j]=='x'):
                        duple_mine[btm_i][j]='o'
                        dfs_is_not_collapse(0,j,duple_mine)
                collapse_coeff=collapse_coeff+1 
                

    if(collapse):
        first_i_j = collapse_points.pop()
        distance = first_i_j[0]-0
        collapse_mineral_dfs(mine,first_i_j[0],first_i_j[1],distance, collapse_points)
        
        for ij_tuple in collapse_points:
            mine[ij_tuple[0]-distance][ij_tuple[1]] = 'x'
    return mine
        
        
        
        
        
def print_mine(mine):
    res = ""
    for line in mine:
        tmp_str = "".join(line)
        res = res+tmp_str+'\n'
    return res

for i,atk in enumerate(attck_points):
    turn = i%2
    attck_mineral(atk,mine,turn)
    collapse_chk(mine)
    recover_mine(mine)
mine.reverse()

print(print_mine(mine))  
        
        
        
        
        
