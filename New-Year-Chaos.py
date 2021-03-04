#code written in python

def minimumBribes(q):
    n = len(q)
    bribes = 0
    for i in range(n-1,-1,-1):
        if q[i] - i > 3:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)        
                
                
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
