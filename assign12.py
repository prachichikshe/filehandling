#Write a Python program to copy the contents of a file to another file . 

from shutil import copyfile
import os
os.system('touch ab.txt')  
copyfile('pc.txt', 'ab.txt')  

'''Output
Paris is the capital and most populous city of France.
By the 17th century, Paris was one of Europe's major centres of finance, commerce, fashion, science, and the arts.
It is the second largest metropolitan area in the European Union. 
Paris is the fifth most expensive city in the world for luxury housing.
'''

