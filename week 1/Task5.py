import itertools

n = int(input())
letters = input().split()
k = int(input())

nb, tot = 0, 0
for t in itertools.combinations([i for i in range(n)], k):
    tot += 1
    for i in t:
        if letters[i] == 'a':
            nb += 1
            break
print(round(nb / tot, 3))