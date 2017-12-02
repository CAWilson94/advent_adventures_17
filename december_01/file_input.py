def file_input_to_int_list(file_name):
    file = open(file_name, "r")
    input_list_int = list(map(int, file.read()))
    file.close()
    return input_list_int

