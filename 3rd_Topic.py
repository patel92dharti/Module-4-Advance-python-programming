#Write a Python program to append text to a file and display the text.

data=open("append_data.txt","a")
data.write("\nIts design philosophy emphasizes code readability with the use of significant indentation.")
data.close()
with open("append_data.txt","r") as data:
    print("*"*90)
    print(data.read())
    data.close()
    print("*"*90)
