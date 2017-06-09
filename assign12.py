#Write a Python program to copy the contents of a file to another file . 

from shutil import copyfile
import os
os.system('touch ab.txt')  
copyfile('pc.txt', 'ab.txt')  

'''Output
'''

