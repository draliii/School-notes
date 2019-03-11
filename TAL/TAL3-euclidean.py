def euclidean_nonrecursive(a, b):
    x = []
    y = []
    x.append(a)
    y.append(b)
    
    i = 0
    while y[i] != 0:
        x.append(y[i])
        y.append(x[i] % y[i])
        i += 1
    
    return x[i]


def euclidean_recursive(a, b):
    if b == 0:
        return a
    else:
        return euclidean_recursive(b, a % b)


if __name__ == "__main__":
    numbers = [132, 32]
    a = max(numbers)
    b = min(numbers)
    print(euclidean_nonrecursive(a, b))
    print(euclidean_recursive(a, b))
