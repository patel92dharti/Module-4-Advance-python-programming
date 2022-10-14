#Write a Python program to copy the contents of a file to another file.

def copyfile(file):
    with open(file,'r') as d:
        da=open("Copyfile.txt",'w+')
        da.write(d.read())
        da.seek(0)
        print(da.read())
copyfile("data2.txt")
