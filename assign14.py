 #Q.14 Write a Python program to read a random line from a file. 
  
import random
lines = open('pc.txt').read().splitlines()
myline =random.choice(lines)
print(myline)

'''Output
It is the second largest metropolitan area in the European Union. 
'''
