capitalletters = "ABCDEFGHIJKLMNOPQRSRTUVWXYZ"
def words_checked(input_str):
    return len(input_str.split("_"))
def check_the_real(is_true):
    real = True
    for each_bool in is_true:
        real = real and each_bool
    return real
def check_is_true(input_str):
    is_true = []
    for item in input_str:
        is_true.append((item in capitalletters) or (item == "_"))
    return check_the_real(is_true)

def main():
    input_str = input()
    is_true = check_is_true(input_str)
    if is_true:
        print("True " + str(words_checked(input_str)))
    else:
        print(False)
main()