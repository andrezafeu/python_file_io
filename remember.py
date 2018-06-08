def remember(thing):
    # by default, open() opens a file for reading. ex: file = open('database.txt')
    # 'a' open for writing, appending to the end of the file
    file = open('database.txt', 'a')
    file.write(thing+"\n")
    # file.close() is being used just to be more explicit. When the function ends, things inside would've been garbage collected anyway.
    file.close()

remember(input("What should I remember? "))