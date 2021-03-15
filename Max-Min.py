#this code is written in python

def maxMin(k, arr):
    arr.sort()    #setting in ascending order for ease
    diff = [0]*(len(arr)+1-k)   #array to note the differences
    for i in range (len(diff)):
        diff[i] = arr[i+k-1] - arr[i]
    return min(diff)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
