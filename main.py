def Merge():
    with open("test1", "rb") as e:
         file1 = e.read()

    with open("test2", "rb") as b:
         file2 = b.read()

    with open("done", "wb") as df:
         merged = file1 + file2
         df.write(merged)

Merge()
