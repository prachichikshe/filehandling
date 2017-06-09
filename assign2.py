#Q2 Write a Python program to read first n lines of a file and print these lines.

def file_read_from_head(fname, nlines):  
     from itertools import islice  
     with open(fname) as f:  
               for line in islice(f, nlines):  
                      print(line)  
file_read_from_head('pc.txt',2)  


#----------------------------------
'''Output'''
