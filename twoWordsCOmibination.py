def twoCombination(n, m):
    sorted_list = sorted(n)
    range1 = list(range(len(n)))
    
    new_combination = []
    for i in range1:
        new_combination.append([i])
        
    for j in range(m-1):
        new_combination2 = []
        for item in new_combination:
            for i in range1:
                if item[-1] < i:
                    new_combination2.append(item + [i])
        new_combination = new_combination2
        
    word_combination = []
    for i in new_combination:
        new_word = []
        for j in i:
            new_word.append(sorted_list[j])
        word_combination.append(tuple(new_word))
    return sorted(set(word_combination))
    
n = input().split()
m = int(input())
a = twoCombination(n, m)
for i in a:
    print(*i)
