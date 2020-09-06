import sys

def is_vaid(i, j, n, m):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def min_index(alist, indexs):
    min_num = 1000
    min_index_list = [0, 0]

    for i, a in enumerate(alist):
        if a < min_num:
            min_index_list = indexs[i]

    return min_index_list

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    grid = []
    for i in range(n):
        grid.append(list(map(int, sys.stdin.readline().split(' '))))

    m = len(grid[0])

    dp = [[0] * m for _ in range(n)]

    move_tos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pathes = []
    def backtrack(track, i, j):
        if i == n - 1 and j == m - 1:
            pathes.append(track[:])

        for move_to in move_tos:
            if is_vaid(i + move_to[0], j + move_to[1], n, m):
                if [i + move_to[0], j + move_to[1]] in track:
                    continue
                track.append([i + move_to[0], j + move_to[1]])
                backtrack(track, i + move_to[0], j + move_to[1])
                track.pop()

    backtrack([[0, 0]], 0, 0)

    res = []
    for path in pathes:
        i = 0
        current_res = 0
        while i < len(path) - 1:
            current_res += abs(grid[path[i][0]][path[i][1]] - grid[path[i + 1][0]][path[i + 1][1]])
            i += 1
        res.append(current_res)

    print(min(res))

