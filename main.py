#openfile = open("story.txt", "r")
def readfile(filename):
    #reading the files
    with open("story.txt", "r") as openfile:
        read_file = openfile.read()
    return read_file

def countwords():
    text = readfile("story.txt")
    split_text = text.split()
    #print(split_text)
    count ={}
    for line in split_text:
        if line in count:
            count[line] += 1
        else:
            count[line] =1
    return count
     

print(countwords())