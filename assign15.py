#Q.15 Write a Python program to assess if a file is closed or not. 

f = open('pc.txt','r')  
print(f.closed)  
f.close()  
print(f.closed)  

'''Output 
False
True
'''
