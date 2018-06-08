def remember(thing):
    # by default, open() opens a file for reading. ex: file = open('database.txt')
    # 'a' open for writing, appending to the end of the file
    with open('database.txt', 'a') as file:
        file.write(thing+"\n")


remember(input("What should I remember? "))