#Write a Python program to count the number of lines in a text file.

def count_lines(file):
    with open(file,'r') as data:
        for i ,k in enumerate(data):
            pass
    return i+1
print(count_lines("append_data.txt"))