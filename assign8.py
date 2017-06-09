# Write a python program to find the longest words. 

text = "I love dancing than singing"
longest = 0
for word in text.split():
    if len(word) > longest:
       longest = len(word)
       longest_word = word
print( "The longest word is %s" % longest_word )

'''Output'''

