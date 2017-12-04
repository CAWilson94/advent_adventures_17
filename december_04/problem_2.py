def sort_items_in_list(list_input):
    other_list = []
    for item in list_input:
        some_list = []
        for word in item:
            other_word = ''.join(sorted(word.upper()))
            some_list.append(other_word)
        other_list.append(some_list)
    return other_list







