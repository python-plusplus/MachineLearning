n, k = map(int, input().split())
triangle = []
for a in range(n):
    triangle.append(list(map(int, input().split())))
total = 0
tLen = len(triangle)
lineCount = tLen - k + 1
for b in range(lineCount):
    for c in range(len(triangle[b])):
        maxN = 0
        count = 0
        for d in range(k):
            count += 1
            dab = max(triangle[b + d][c:c + d + 1])
            if dab > maxN:
                maxN= dab
            if count == k:
                total += maxN

print(total)