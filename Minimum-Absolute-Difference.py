#code written in python

def minimumAbsoluteDifference(arr):
    arr.sort()
    mini = abs(arr[0]-arr[1])
    dif = 'Uninitiated'
    for i in range (len(arr)-1):
        dif = abs(arr[i]-arr[i+1])
        if dif < mini:
            mini = dif
    return mini
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
