#Write a Python program to count the frequency of words in a file.

from collections import Counter
def Frequency(file):
    with open(file,"r") as data:
        return Counter(data.read().split())

print(Frequency("word_frequency.txt"))

