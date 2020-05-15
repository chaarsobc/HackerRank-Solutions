#code written in python

def getTotalX(a, b):
    lcm1 = a[0]
    gcd2 = b[0]
    c = 0
    for i in range(1,len(a)):
        lcm1 = lcm1*a[i]//math.gcd(lcm1, a[i])
    for i in range (1,len(b)):
        gcd2 = math.gcd(gcd2, b[i])
    for i in range (lcm1,gcd2+1):
        if i%lcm1 == 0 and gcd2%i == 0:
            c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
