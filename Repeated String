#code written in python

def repeatedString(s, n):
    l = len(s)
    c = 0
    x = 0
    for i in range (0,l):
        if s[i] == 'a':
            c += 1    #increment of the counter
    for i in range (0,n%l):
        if s[i] == 'a':
            x += 1    #increment of the counter
    return n//l*c+x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
