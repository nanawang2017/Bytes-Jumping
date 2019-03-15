'''
输入N, 打印 N*N 螺旋矩阵
比如 N = 3，打印：
1 2 3
8 9 4
7 6 5
N = 4，打印：
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
'''
n = int(input('请输入数n:'))
# 初始化数组
arr = [[0] * n for i in range(n)]


# 递归解决
def dfs(arr, x, y, start, n):
    if n <= 0: return 0
    if n == 1:
        arr[x][y] = start
        return 0
    # up
    for i in range(n):
        arr[x][y + i] = start
        start += 1
    # right
    for i in range(n - 1):
        arr[x + 1 + i][y + n - 1] = start
        start += 1
    # down
    for i in range(n - 1):
        arr[x + n - 1][y + n - 2 - i] = start
        start += 1
    # left
    for i in range(n - 2):
        arr[x + n - 2 - i][y] = start
        start += 1
    dfs(arr, x + 1, y + 1, start, n - 2)


a = dfs(arr, 0, 0, 1, n)
# 格式化输出print
l = len(str(n * n)) + 1
format = ('%' + str(l) + 'd') * n
for tmp in arr:
    print(format % tuple(tmp))

