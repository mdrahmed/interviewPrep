
def maxsqarea(m,n,h,v):
    M = 10 ** 9 + 7
    def getSides(fences, L):
        sides = set()
        fences.append(1)
        fences.append(L)

        fences.sort()
        N = len(fences)
        for i in range(N):
            for j in range(i+1, N):
                sides.add(fences[j] - fences[i])

        return sides

    h = getSides(h, m)
    v = getSides(v, n)

    o = h & v

    if len(o) == 0:
        return -1

    return (max(o) ** 2) % M
