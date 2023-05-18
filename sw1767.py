directions = [(-1,0), (1,0), (0,-1), (0,1)]

def possible_direction(core, maxinos) :
    N = len(maxinos)
    result = []
    for d in directions :
        cur_point = core
        cur_point = tuple(ci + di for ci, di in zip(cur_point, d))
        while True :
            if maxinos[cur_point[0]][cur_point[1]] == 1 :
                break
            if cur_point[0] == 0 or cur_point[0] == N-1 or cur_point[1] == 0 or cur_point[1] == N-1 :
                result.append(d)
                break
            cur_point = tuple(ci + di for ci, di in zip(cur_point, d))
    return result

def add_line(core, maxinos, direction) :
    cur_point = core
    length = 0
    while True :
        if cur_point[0] == 0 or cur_point[0] == N-1 or cur_point[1] == 0 or cur_point[1] == N-1 :
            break
        cur_point = tuple(ci + di for ci, di in zip(cur_point, direction))
        maxinos[cur_point[0]][cur_point[1]] = 1
        length += 1
    return maxinos, length
        
def is_possible_direction(core, maxinos, direction) :
    cur_point = core
    cur_point = tuple(ci + di for ci, di in zip(cur_point, direction))
    while True :
        if cur_point[0] < 0 or cur_point[0] >= N or cur_point[1] < 0 or cur_point[1] >= N :
            return True
        if maxinos[cur_point[0]][cur_point[1]] == 1 :
            return False
        next_point = tuple(ci + di for ci, di in zip(cur_point, direction))
        cur_point = next_point

def BFS(cores, maxinos, sum_line_length) :
    print(len(cores))
    if len(cores) == 0 : return sum_line_length, maxinos
    for core in cores :
        if core[2] == 0 :
            cores.remove(core)
            continue
        # print(core, possible_direction(core, maxinos))
        for d in directions :
            if is_possible_direction(core, maxinos, d) is True :
                next_maxinos, line_length = add_line(core, maxinos, d)
                next_cores = []
                for c in cores : next_cores.append(c)
                next_cores.remove(core)
                rest_line_length, next_maxinos = BFS(next_cores, next_maxinos, sum_line_length+line_length)
        

T = int(input())
for t in range(T) :
    N = int(input())
    maxinos = []
    cores = []
    sum_line_length = 0
    for n in range(N) :
        lst = list(map(int, input().split()))
        maxinos.append(lst)
        for idx, l in enumerate(lst) :
            if l == 1 :
                edge_dist = min(n, N-n-1, idx, N-idx-1)
                cores.append((n, idx, edge_dist))
    cores = sorted(cores, key=lambda x: x[2])
    
    sum_line_length = BFS(cores, maxinos, sum_line_length)



    print(f"#{t+1} {sum_line_length}")
