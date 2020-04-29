def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            s = len(l[i])
            z = s-10
            l[i] = '+91 ' + l[i][z:z+5] + ' ' + l[i][z+5:]
        print(*sorted(l), sep='\n')
        return l
    return fun

def wrapper(f):
    def fun(l):
    
        for i in range(len(l)):
            no=str(l[i])
            if no.startswith('+91'):
                no.replace('+91','')

            elif (no.startswith('91') and len(no)>10):

                no.replace('91','')

            elif no.startswith('0'):
                no.replace('0','')

            first='+91'
            sec=no[:5]
            third=no[5:]
            no=first+' '+sec+' '+third
            l[i]=no
        


    return f



number = list()
N = int(raw_input())
for i in range(N):
    number.append(str(raw_input()))

def mobile(function):
    def input(number):
            return sorted([function(i) for i in number])
    return input

@mobile
def standardize(number):
	return "+91" + " " + number[-10:-5] + " " + number[-5:]

print '\n'.join(standardize(number))
