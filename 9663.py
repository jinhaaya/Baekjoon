import copy

N = int(input())
map = [[0 for _ in range(N)] for _ in range(N)]

result = 0

def put_queen(map, location) :
    temp_map = copy.deepcopy(map)
    for i in range(N) :

        if map[location[0]][i] == 2 : return None
        temp_map[location[0]][i] = 1

        if map[i][location[1]] == 2 : return None
        temp_map[i][location[1]] = 1

        if location[0]-i >= 0 and location[1]-i >= 0 :
            if map[location[0]-i][location[1]-i] == 2 : return None
            temp_map[location[0]-i][location[1]-i] = 1

        if location[0]-i >= 0 and location[1]+i < N :
            if map[location[0]-i][location[1]+i] == 2 : return None
            temp_map[location[0]-i][location[1]+i] = 1

        if location[0]+i < N  and location[1]-i >= 0 :
            if map[location[0]+i][location[1]-i] == 2 : return None
            temp_map[location[0]+i][location[1]-i] = 1

        if location[0]+i < N and location[1]+i < N :
            if map[location[0]+i][location[1]+i] == 2 : return None
            temp_map[location[0]+i][location[1]+i] = 1

    temp_map[location[0]][location[1]] = 2
    return temp_map

def printMap(map) :
    for i in range(N) :
        for j in range(N) :
            print(map[i][j], end = " ")
        print("")
    print("==========")


def DFS(map, cur_point, cur_queen) :

    if cur_queen >= N :
        # print("HIT!")
        # printMap(map)
        return 1
    
    success = 0

    for j in range(cur_point[1], N) :
        if map[cur_point[0]][j] == 0 :
            temp_map = put_queen(map, [cur_point[0],j])
            if temp_map != None :
                success += DFS(temp_map, [cur_point[0],j], cur_queen+1)

    for i in range(cur_point[0]+1, N) :
        for j in range(N) :
            if map[i][j] == 0 :
                temp_map = put_queen(map, [i,j])
                if temp_map != None :
                    success += DFS(temp_map, [i,j], cur_queen+1)

    return success

result = DFS(map, [0,0], 0)
print(result)