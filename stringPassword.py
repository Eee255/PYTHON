
def assigning_a_value(n):
    remaining = list(range(2, n))
    return list(range(1, n+1)) + remaining[::-1]
    
def patter_print(pattern, string, n):
    repeations = len(string) // len(pattern)
    extra = len(string) % len(pattern)
    total_pattern = pattern*repeations + pattern[:extra]
    word = ""
    for i in range(1,n+1):
        for j in range(len(string)):
            if total_pattern[j] == i:
                word += string[j]
    return word
    
    


def main():
    string = input()
    columns = int(input())
    print(patter_print(assigning_a_value(columns), string, columns))
main()
    