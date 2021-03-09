#code written in python

def luckBalance(k, contests):
    j = 0
    suml = 0
    L = [0]*len(contests)
    for i in range (len(contests)):
        suml += contests[i][0]
        if contests[i][1] == 1:
            L[j] = contests[i][0]
            j += 1
    del L[j : len(contests)] #to avoid confusion when searching for minimum luck values
    while j - k > 0:
        mini = min(L)
        suml -= 2*mini
        L.remove(mini)
        j -= 1
    return suml
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
