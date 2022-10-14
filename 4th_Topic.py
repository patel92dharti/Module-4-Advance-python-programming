#Write a Python program to read first n lines of a file.

with open("firstline_read.txt","r") as data:
    fileread=list(map(str,data.read().splitlines()))[0]
    print(fileread)