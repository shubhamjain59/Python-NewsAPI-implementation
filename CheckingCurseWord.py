def read_text():
    readingfile = open(r'C:\Users\DELL\Desktop\IMP.txt')
    contents = readingfile.read()
    print(contents)
    readingfile.close()

read_text()