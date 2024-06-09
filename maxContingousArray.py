def maxContingousArray(n):
    dictionary = {}
    for i in range(len(n)):
        for j in range(i+1, len(n)+1):
            addition = sum(n[i:j])
            dictionary[tuple(n[i:j])] = addition
    return dictionary

n = list(map(int, input().split()))
fun = maxContingousArray(n)
keys = list(fun.keys())
values = list(fun.values())
x = values.index(max(values))
print(*keys[x])