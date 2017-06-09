# Q5.Write a Python program to read a file line by line and store it into a list. 
 with open("pc.txt","r") as fo:
           #Content_list is the list that contains the read lines.     
            content_list = fo.readlines()
            print(content_list)


'''Output
['Paris is the capital and most populous city of France.\n', 
"By the 17th century, Paris was one of Europe's major centres of finance, commerce, fashion, science, and the arts.\n",
'It is the second largest metropolitan area in the European Union. \n', 
'Paris is the fifth most expensive city in the world for luxury housing.\n']'''

