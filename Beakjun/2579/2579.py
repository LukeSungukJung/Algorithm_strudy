import sys
sys.setrecursionlimit(10**6)

num = int(input())

stair_list = []
stair_scores = []
last_index = num-1
consecutive_maximum=2;
consecutive_status=0;
max_sum=0

for idx in range(num):
    stair_list.append(int(input()))

stair_scores.append(stair_list[0])
stair_scores.append(stair_list[0]+stair_list[1])
stair_scores.append(max(stair_list[0]+stair_list[2],stair_list[1]+stair_list[2]))

for idx in range(3,num):
    stair_scores.append(max(stair_scores[idx-2]+stair_list[idx],stair_scores[idx-3]+stair_list[idx-1]+stair_list[idx]))
    

print(stair_scores[-1])
