# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_entire_file():
    '''Read the contents of a file all at once.'''
    filename = 'credits.txt'
    with open(filename) as f_obj:
        contents = f_obj.read()
    print(contents)
    print(type(contents))
    print(type(f_obj))

def read_entire_file_wrong():
    '''Read the contents of a file all at once.'''
    filename = 'siddhartha.txt'
    with open(filename) as f_obj:
        contents = f_obj.read()
    print(contents)
    print(type(contents))
    print(type(f_obj))

def read_with_exception_handling(filename):
    '''Read the contents of a file all at once.'''
    #filename = input("What is the name of the input file? ")
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)
            print(type(contents))
            print(type(f_obj))
    except FileNotFoundError:
        print(f"Can't find file {filename}.")

def read_line_by_line():
    '''Read the contents of a file line-by-line.
    Print each line with the newline character stripped from the end of the line.'''
    filename = 'grade_info.txt'
    with open(filename) as f_obj:
        for line in f_obj:
            print(line.rstrip())


def read_booleans():
    '''Make an attempt to read text as booleans.
    Convert strings to booleans.'''
    filename = 'boolean_info'
    with open(filename) as f_obj:
        for b_string in f_obj:
            # As outlined in:
            # https://www.geeksforgeeks.org/python-convert-string-truth-values-to-boolean/#:~:text=Method%201%3A%20Convert%20String%20to,by%20default%20it%20returns%20False.
            b = b_string.rstrip() == 'True'
            print(b)


def store_lines_in_list():
    '''Read the lines from the file grade_info.txt and store them in a list.'''
    filename = 'grade_info.txt'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
        print(line.rstrip())
    print(lines)


def read_and_write_credits():
    '''Read credits into a list.'''
    filename = 'credits.txt'
    with open(filename) as f_obj:
        credit_strings = f_obj.readlines()
    # Passing the 'w' argument to open()
    # tells Python you want to write to a file.
    output_file = 'credits_results.txt'
    credit_string = ""
    for credits in credit_strings:
        credit_string += credits.rstrip() + ','
    with open(output_file, 'w') as f:
        f.write(credit_string[0:9])

def write_total_credits_with_append():
    '''Read credits into a list.'''
    filename = 'credits.txt'
    with open(filename) as f_obj:
        credit_strings = f_obj.readlines()
    # Passing the 'w' argument to open()
    # tells Python you want to write to a file.
    credit_integers = []
    for credits in credit_strings:
        credit_integers.append(int(credits.rstrip()))
    output_file = 'credits_results.txt'
    credit_string = ""
    for credits in credit_strings:
        credit_string += credits.rstrip() + ','
    with open(output_file, 'a') as f:
        f.write(credit_string[0:9] + '\n')
        f.write(f'Total credits: {str(sum(credit_integers))}\n')

def exception_practice():
    print(5/0)

def exception_practice2():
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("You can't divide by zero!")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # read_entire_file()
    # read_line_by_line()
    # read_booleans()
    # store_lines_in_list()
    # read_and_write_credits()
    # write_total_credits_with_append()
    # exception_practice2()
    # read_entire_file_wrong()
    read_with_exception_handling('siddhartha.txt')
    read_with_exception_handling('boolean_info')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
