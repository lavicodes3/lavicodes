# method first  
# with open("names.csv") as file:
#     for name in file:
#        sept = name.rstrip().split(",")
#        print(f"{sept[0]} is in house{sept[1]}")
 
# method second
with open("names.csv") as file:
    for names in sorted(file):
       name,house = names.rstrip().split(",")
       print(f"{name} is in house{house}")