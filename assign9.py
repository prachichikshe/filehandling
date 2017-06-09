#Write a Python program to count the frequency of words in a file. 

file=open("text.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for a in wordcount.items():
    print a
 
 
 '''Output'''
