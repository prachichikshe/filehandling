#Write a Python program to read a file line by line store it into a variable. 

with open ("pc.txt", "r") as myfile:
    data=myfile.readlines()
    print(data)
    

'''Output
['Paris is the capital and most populous city of France.\n',
"By the 17th century, Paris was one of Europe's major centres of finance, commerce, fashion, science, and the arts.\n",
'It is the second largest metropolitan area in the European Union. \n', 
'Paris is the fifth most expensive city in the world for luxury housing.\n']'''
