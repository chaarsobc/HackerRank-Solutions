#this code is written in python

def getMinimumCost(k, c):
    n = len(c)
    cost = 0
    d = 0
    for i in range (n-1, -1,-1):
        if (n-1-i)%k == 0:
          d += 1
        cost += d*max(c)
        c.remove(max(c))
    return cost
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
