def contador(n):

    if n == 1:
        return 1

    else:
        return n + contador(n - 1)

print(contador(7))
