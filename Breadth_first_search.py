def getGrid():
    # [0,0,0]
    # [1,1,0]
    # [0,0,0]
    # [0,1,1]
    # [0,0,0]
    grid = []
    for i in range(5):
        grid.append([0 for _ in range(3)])
        if i == 1:
            grid[i][:2] = [1,1]
        if i == 3:
            grid[i][1:3] = [1,1]
    return grid

def printGrid(grid):
    for rows in grid:
        print (rows)

def getGridVal(grid, index):
    return grid[index[0]][index[1]]

from queue import Queue
def BFS(grid, start, end):
    if start == end:
        return start

    R = len(grid)
    C = len(grid[0])
    visited = []
    q = Queue()
    q.put([start])
    while not q.empty():
        path = q.get()
        print(f"path: {path}")
        node = path[-1]
        print(f'node: {node}')
        if node not in visited:
            visited.append(node)
            print(f'visited: {visited}')
            neighbours = getNeighbours(grid, node, R, C, visited)
            for neighbour in neighbours:
                print(f'neighbour: {neighbour}')
                new_path = path
                new_path.append(neighbour)
                print(f'new_path: {new_path}')
                q.put(new_path)
                if neighbour == end:
                    print('#### END POINT REACHED ####')
                    return new_path
    print ('#### NO PATH FOUND ####')

    print(visited)

def getNeighbours(grid, node, R , C, visited):
    neighbours = []
    # move left
    if node[1] > 0:
        left = [node[0],node[1]-1]
        if getGridVal(grid, left) == 0 and left not in visited:
            neighbours.append(left)
    # move right
    if node[1] < C-1:
        right = [node[0],node[1]+1]
        if getGridVal(grid, right) == 0 and right not in visited:
            neighbours.append(right)
    # move up
    if node[0] > 0:
        up = [node[0]-1,node[1]]
        if getGridVal(grid, up) == 0 and up not in visited:
            neighbours.append(up)
    # move down
    if node[0] < R-1:
        down = [node[0]+1,node[1]]
        if getGridVal(grid, down) == 0 and down not in visited:
            neighbours.append(down)
    return(neighbours)

if __name__ == '__main__':
    grid = getGrid()
    printGrid(grid)
    start = [0,0]
    end = [4,2]
    print(f'Shortest path: {BFS(grid, start, end)}')

    