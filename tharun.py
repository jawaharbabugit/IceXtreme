def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            s = len(l[i])
            z = s-10
            l[i] = '+91 ' + l[i][z:z+5] + ' ' + l[i][z+5:]
        print(*sorted(l), sep='\n')
        return l
    return fun


