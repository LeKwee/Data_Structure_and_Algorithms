
def solution(w,h,grid):
    for row in grid:
        print(row)
        print()
    print()
    
    # DFS
    island_count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '*':
                dfs(grid, i ,j)
                island_count +=1
                print(f'island count: {island_count}')
    return island_count

def dfs(grid, i ,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]!='*':
        return
    grid[i][j]='#'

    for row in grid:
        print(row)
        print()
    print()

    dfs(grid,i-1,j)
    dfs(grid,i+1,j)
    dfs(grid,i,j-1)
    dfs(grid,i,j+1)
    


if __name__ == '__main__':
    # input 1  = 7 6
    # input 2 = '##########*########*#####**######*###*####'

    dim = input().split()
    w,h = int(dim[0]),int(dim[1])
    grid_string = input()

    grid = []
    row = []

    for i in range(0,len(grid_string)):
        row.append(grid_string[i])
        if (i+1) % w == 0:
            grid.append(row)
            row=[]

    output = solution(w,h,grid)

    print(output)
