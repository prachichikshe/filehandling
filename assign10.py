#11. Write a Python program to write a list to a file.
import os
statinfo = os.stat('pc.txt')
print statinfo.st_size

'''Output
45'''
