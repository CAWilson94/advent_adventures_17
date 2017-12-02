from december_1 import file_input as fi
from itertools import cycle

def non_human_captcha(puzzle_input):
    """ this does something """
    sum_array = []
    for index in range(len(puzzle_input)-1):
        if puzzle_input[index + 1] == puzzle_input[index]:
            sum_array.append(puzzle_input[index])
    if puzzle_input[0] == puzzle_input[-1]: # Such a hack ...
        sum_array.append(puzzle_input[0])
    captcha_answer = sum(sum_array)
    return captcha_answer

def boop():
    boop = [1, 2, 3, 4]
    for x in range(len(boop) *2):
        print(boop[x % len(boop)])

    #for p in cycle([1, 2, 3]):
        #print(p)

if __name__ == "__main__":

    print(non_human_captcha(fi.file_input_to_int_list("input.txt")))
    boop()
