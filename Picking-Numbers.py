# code written in python

def pickingNumbers(a):
    a.sort()
    count = [1]*len(a)  # to count 1 for the element itself
    for i in range(len(a)-1): 
        for j in range (i+1,len(a)):
            if ((a[i] == a[j]) or (a[i] == a[j]-1)):
                count[i] += 1  # to add 1 each time 
    return max(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
