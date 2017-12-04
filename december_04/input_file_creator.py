def input_from_file(file_name): 
    """ getting output from file input """
    with open(file_name) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content



