def hourglass_pattern(n):
    k = n -2
    for i in range(n, -1, -1): #increment by -1 from n to -1 which does not contain -1
        for j in range(k, 0, -1):
            print(end = " ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = 2 * n - 2
    for i in range(0, n + 1):
        for j in range(0, k):
            print(end=" ")
        k = k -1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def diamond_filled(n):
    k = n * 2 - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end = " ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def half_diamond_filled_1(n):
    k = 2 * n - 2
    for i in range(0, n - 1):
        for j in range(0, k):
            print(end = " ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = -1
    for i in range(n - 1, -1, -1):
        for j in range(k, -1, -1):
            print(end= " ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def half_diamond_filled_2(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def right_triangle_filled_1(n):
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def right_triangle_filled_2(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k -2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def congruent_triangle_filled_1(n):
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

def congruent_triangle_filled_2(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")