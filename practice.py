def fact():
    n = int(input("whats the no "))
    i = 1
    fac = 1
    while i <= n:
        fac *= i
        i += 1
    print(fac)
fact()