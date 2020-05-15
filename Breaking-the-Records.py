#code written in python

def breakingRecords(scores):
    mini = maxi = scores[0]
    minic = maxic = 0
    for i in range (len(scores)):
        if mini > scores[i]:
            mini = scores[i]
            minic += 1
        elif maxi < scores[i]:
            maxi = scores[i]
            maxic += 1
    return maxic,minic
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
