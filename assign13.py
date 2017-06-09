#Write a Python program to combine each line from first file with the corresponding line in second file.

with open('abc.txt') as fh1, open('pc.txt') as fh2:  
           for line1, line2 in zip(fh1, fh2):  
               # line1 from abc.txt, line2 from pc.txtg  
                 print(line1+line2)  
                 
  '''Output
  Paris is the capital and most populous city of France.
  Paris is the capital and most populous city of France.
  
  By the 17th century, Paris was one of Europe's major centres of finance, commerce, fashion, science, and the arts.
  By the 17th century, Paris was one of Europe's major centres of finance, commerce, fashion, science, and the arts.
  
  It is the second largest metropolitan area in the European Union.
  It is the second largest metropolitan area in the European Union. 
  
  Paris is the fifth most expensive city in the world for luxury housing.
  Paris is the fifth most expensive city in the world for luxury housing.
  '''
