import os


def auto_make_package(day):
    package_name = "december_" + str(day)
    if not os.path.exists(package_name):
        os.mkdir(package_name)
        create_all_december_packages(package_name)
        create_init_file(package_name)
        create_input_file_creator(package_name)
        print(package_name)
    else:
        print("that exists already")
        pass


def create_problem_file(path, problem_number):
    space = " "
    file = open(path + "/problem_" + str(problem_number) + ".py", "w")
    file.write("def problem_" + str(problem_number) + "(puzzle_input):\n")
    file.write(4*space + '""" problem description """ ')
    file.close()


def create_init_file(path):
    file = open(path + "/__init__.py", "w")
    file.close()


def create_all_december_packages(path):
    create_problem_file(path, 1)
    create_problem_file(path, 2)
    print("this should create all directories")


def create_input_file_creator(path):
    space = " "
    file = open(path + "/input_file_creator.py", "w")
    file.write("def input_from_file(file_name): \n")
    file.write(4 * space + '""" getting output from file input """\n')
    file.write(4 * space + 'file = open(file_name, "r")\n')
    file.write(4 * space + 'output = None # use input as needed ...\n')
    file.write(4 * space + 'file.close()\n')
    file.write(4 * space + 'return output\n')
    file.close()


def single_digit_num(num):
    if num < 10:
        num = "0" + str(num)
    return num


def create_december_directories():
    for val in range(2, 32):
        auto_make_package(single_digit_num(val))


if __name__ == "__main__":
    create_december_directories()
