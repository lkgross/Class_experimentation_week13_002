# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_entire_file():
    '''Read the contents of a file all at once.'''
    filename = 'grade_info.txt'
    with open(filename) as f_obj:
        contents = f_obj.read()
    print(contents)
    print(type(contents))
    print(type(f_obj))

def read_line_by_line():
    '''Read the contents of a file line-by-line.'''
    filename = 'grade_info.txt'
    with open(filename) as f_obj:
        for line in f_obj:
            print(line.rstrip())

def read_booleans():
    '''Make an attempt to read text as booleans.
    It does not work!'''
    filename = 'boolean_info'
    with open(filename) as f_obj:
        for b_string in f_obj:
            # As outlined in:
            # https://www.geeksforgeeks.org/python-convert-string-truth-values-to-boolean/#:~:text=Method%201%3A%20Convert%20String%20to,by%20default%20it%20returns%20False.
            b = b_string.rstrip().title() == 'True'
            print(b)

def store_lines_in_list():
    filename = 'grade_info.txt'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
        print(line.rstrip())
    print(lines)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # read_entire_file()
    # read_line_by_line()
    read_booleans()
    # store_lines_in_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
