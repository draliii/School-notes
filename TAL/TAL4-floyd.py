def floyd(M):
    n = len(M)
    print(n)
    for k in range(0,n):
        print(M)
        for i in range(0,n):
            for j in range(0,n):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
    return M

if __name__ == "__main__":
    M = [[0, 3, 2, 10000, 4],
         [3, 0, 10000, 2, 10000],
         [2, 10000,0, 10000, 1],
         [10000, 2, 10000, 0, 10000],
         [4, 10000, 1, 10000, 0]]
    print(floyd(M))
    N = [[0, 3, 10000], [3, 0, 3], [10000, 3, 0]]
    print(floyd(N))
