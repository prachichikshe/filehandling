#Write a Python program to count the frequency of words in a file. 

file=open("pc.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for a in wordcount.items():
    print a

'''
output:
('and', 2)('major', 1)('metropolitan', 1)('Paris', 3)('is', 3)('one', 1)('second', 1)('in', 2)('fifth', 1)('European', 1)('city', 2)('century,', 1)('for', 1)('area', 1)('fashion,', 1)('expensive', 1)('capital', 1)('populous', 1)('was', 1)('By', 1)('luxury', 1)("Europe's", 1)('largest', 1)('Union.', 1)('most', 2)('arts.', 1)('commerce,', 1)('housing.', 1)('finance,', 1)('17th', 1)('world', 1)('of', 3)('It', 1)('science,', 1)('France.', 1)('centres', 1)('the', 7)
'''
