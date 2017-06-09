file_array = []
with open('pc.txt',"r") as my_file:
    for line in my_file:
        file_array.append(line)
    print(file_array)
