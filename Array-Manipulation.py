def arrayManipulation(n, queries):
    ans = [0]*n  # define array size beforehand
    for i in range (len(queries)):  # since number of rows = iteraions required
        for j in range (queries[i][0], queries[i][1]+1):
            ans[j-1] += queries[i][2]  # j-1 required to match the index of the queries
    return max(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
