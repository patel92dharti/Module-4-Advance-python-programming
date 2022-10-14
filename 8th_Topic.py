#Write a python program to find the longest words.
def Longest_Word(file):
    with open(file,"r") as data:
        words=data.read().split()
        Max_len_word=max(words,key=len)
        Max_len=len(max(words,key=len))
        print("Max Lenth is",Max_len)
        print("Max Lenth word in file:",Max_len_word)

print(Longest_Word("data2.txt"))