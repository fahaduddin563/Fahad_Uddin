def fibonacci_iterative(n, filename):
    a, b = 0, 1

    with open(filename, "w") as f:
        for _ in range(n):
            f.write(str(a) + "\n")
            a, b = b, a + b


fibonacci_iterative(25, "output/fibonacci_iterative.txt")

