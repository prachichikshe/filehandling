#1. Write a Python program to read an entire text file and print its contents.

f=open("file1.txt","w+")
f.write("Hello..!! Zensarians...!!")
f.seek(0,0)
print (f.read())
f.close()

#------------------
'''Output'''
