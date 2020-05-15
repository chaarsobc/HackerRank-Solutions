#code written in python

def birthday(s, d, m):
    c = 0
    for i in range (len(s)-m+1):
        a = s[i:i+m:1]
        if sum(a) == d:
            c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
