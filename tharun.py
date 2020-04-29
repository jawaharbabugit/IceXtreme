def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            s = len(l[i])
            z = s-10
            l[i] = '+91 ' + l[i][z:z+5] + ' ' + l[i][z+5:]
        print(*sorted(l), sep='\n')
        return l
    return fun


import operator
def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key = operator.itemgetter(2))
        for i in range(len(people)):
            yield ' '.join(people[i])
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

    10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M
