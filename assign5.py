# Q5.Write a Python program to read a file line by line and store it into a list. 

def file_read(fname):
      with open(fname) as fo:
               #Content_list is the list that contains the read lines.     
                content_list = fo.readlines()
                print(content_list)
file_read('pc.txt')

'''Output'''

