def postion_of_item(item):
    new_list = []
    for index, val in enumerate(item):
        if val == 1:
            new_list.append(index)
    return new_list
def get_max_distance(x, cols, row):
    for item in x:
        if item.count(1) != 0:
            return postion_of_item(item)
    return list(range(1, cols+1))

def main():
    col, row = map(int, input().split())
    x = []
    for i in range(col):
        each_row = list(map(int, input().split()))
        x.append(each_row)
    result = get_max_distance(x, col, row)
    print(sorted(result))
main()