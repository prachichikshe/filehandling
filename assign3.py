# Write a Python program to append text to a file and display the text. 
import io
fo=open("pc.txt","w+")
fo.write("\nHii..!!\nprachi\nhere")
fo.close()
fo=open("pc.txt","a")
fo.write("appended file content\nbye")
fo=open("pc.txt","r")
str=fo.read()
print str
fo.close()


'''Output'''
