f = open("test.log", "r") 
while 1:
    char = f.read(1)
    if not char:
        break
    if char.isupper():
        print(char)

f.close()