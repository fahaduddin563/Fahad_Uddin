def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def write_fibonacci_recursive(count, filename):
    with open(filename, "w") as f:
        for i in range(count):
            f.write(str(fibonacci_recursive(i)) + "\n")


write_fibonacci_recursive(25, "output/fibonacci_recursive.txt")

