# FOR READING THE FILES.... 
# method 1.  
# with open("names.csv") as file:
#     for name in sorted(file):
#        sept = name.rstrip().split(",")
#        print(f"{sept[0]} is in house{sept[1]}")
 
# method 2.
with open("names.csv") as file:
    for names in sorted(file):
       name,house = names.rstrip().split(",")
       print(f"{name} is in house{house}")