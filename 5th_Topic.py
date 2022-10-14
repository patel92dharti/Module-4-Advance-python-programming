#Write a Python program to read last n lines of a file.
with open("firstline_read.txt","r") as data:
    fileread=list(map(str,data.read().splitlines()))[-1]
    print(fileread)