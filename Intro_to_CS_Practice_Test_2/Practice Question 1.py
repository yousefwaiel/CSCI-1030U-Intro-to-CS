def reverse_rec(str):
    if len(str) < 1:
        return str
    return reverse_rec(str[1:0]) + str[0]