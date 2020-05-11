#code written in python

def rotLeft(a, d):
    n = len(a)
    res = [0]*n
    for i in range (0,n):
        if i<d:
            res[n-d+i] = a[i] #begin iterations
        else:
            res[i-d] = a[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
