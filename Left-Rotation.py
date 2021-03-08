#code written in python

def rotateLeft(d, arr):
    n = len(arr)
    arr1 = [0]*n
    for i in range (n):
        if (n+i-d) < n:
            arr1[n+i-d] = arr[i]
        else:
            arr1[i-d] = arr[i]
    return arr1         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
