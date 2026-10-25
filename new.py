# name = []
# for _ in range(3):
#     name.append(input("whats ur name "))
# for i in sorted(name):  
#     print(f"hello {i}")

name = input("whats your name ")

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()