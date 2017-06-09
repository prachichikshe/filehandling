#Write a Python program to count the frequency of words in a file. 
 from collections import Counter
    with open("pc.txt","r") as f:  
                return Counter(f.read().split())  
 print("Number of words in the file :",word_count("pc.txt"))  
 
 '''Output'''
