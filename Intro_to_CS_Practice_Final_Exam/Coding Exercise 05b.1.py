def feb(n):
    if n <= 1:
        return n
    return feb(n - 1) + feb(n - 2)

print(feb(5))