def Merge():
    a = input("FILE1: ") #input your first file name
    
    with open(f"{a}", "rb") as e:
         file1 = e.read()

    b = input("FILE2: ") #input your second file 
    
    with open(f"{b}", "rb") as b:
         file2 = b.read()

    c = input("OUTPUT FILE: ") 
    
    with open(f"{c}", "wb") as df:
         merged = file1 + file2
         df.write(merged)

Merge()
