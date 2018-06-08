import sys

def remember(thing):
    # 'a' open for writing, appending to the end of the file
    with open('database.txt', 'a') as file:
        file.write(thing+"\n")


def show():
    with open('database.txt') as file:
        for line in file:
            print(line)


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    # sys.argv lists all arguments
    if sys.argv[1].lower() == '--list':
        show()
    else:
        remember(' '.join(sys.argv[1:]))