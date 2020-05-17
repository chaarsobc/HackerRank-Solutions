#code written in python

def getMoneySpent(keyboards, drives, b):
    total = -1
    for i in range (len(drives)):
        for j in range (len(keyboards)):
            if drives[i]+keyboards[j] > tot and drives[i]+keyboards[j] <= b:
                total = drives[i]+keyboards[j]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
