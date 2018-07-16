# file=open("string.txt","w")
# file.write("This is first line ")
# file.write("This is second line ")
# file.close()

new=open("string.txt","r+")
# print(new.readlines())
print(new.read().split())
new.close()

