#code written in python

def minimumBribes(q):
    n = len(q)
    bribes = 0
    res = [0]*n
    for i in range(n):
        res[i] = q[i]-(i+1)   #computes the individual bribes to check for threshold of 2 bribes per person
    for i in range(n):
        for j in range (n-i-1):
            if q[j]>q[j+1]:    #simple bubble sort algo used
                bribes += 1     #computes the total number of bribes
                q[j],q[j+1] = q[j+1],q[j]
    if max(res)>2:
        print("Too chaotic")
    else:
        print(bribes)
