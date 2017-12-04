def input_from_file(file_name): 
    """ getting output from file input """
    with open(file_name) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def print_items(puzzle_input):
    for item in puzzle_input:
        print(item)

if __name__ == "__main__":
    input_items = input_from_file("passphrases.txt")
    print_items(input_items)
    print(len(input_items))
