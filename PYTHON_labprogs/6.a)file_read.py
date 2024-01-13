import os.path
import sys

fname = input("Enter a file name :\n")
if not os.path.isfile(fname):
    print("File doesn't exists\n")
    sys.exit()
read = open(fname, 'r')
lines = read.readlines()
for i in range(len(lines)):
    print(i + 1, ':', lines[i],end="")
word = input("\nEnter a word to search : \n")
cnt = 0
for i in lines:
    cnt += i.count(word)
print(word, "appears", cnt, "times")
