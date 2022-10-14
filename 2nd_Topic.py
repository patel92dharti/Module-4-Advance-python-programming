#Write a Python program to read an entire text file.

data=open("data2.txt","r")
print("*"*60)
print(data.read())
print("*"*60)
data.close()