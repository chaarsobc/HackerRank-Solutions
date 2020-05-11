#code written in python

def hourglassSum(arr):
  maxval = -63 #since minimum value of element is -9, minimum summation value = -9 X 7 = -63
  for i in range(4):
    for j in range(4):
        sumval1 = sum(arr[i][j:j+3])
        sumval2 = sum(arr[i+2][j:j+3])
        sumval = sumval1 + sumval2 + arr[i+1][j+1]
        if sumval>maxval:
            maxval = sumval
 return maxval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
