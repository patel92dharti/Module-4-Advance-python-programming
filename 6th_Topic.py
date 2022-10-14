#Write a Python program to read a file line by line and store it into a list

def fileread(file):
    with open(file) as data:
        List=data.readlines()
        print(List)
print(fileread("append_data.txt"))
