# counting even nos in file numbers.txt

count = 0
with open("numbers.txt") as file:
    num = file.read().split(",")
    for newnum in num:
        if int(newnum) % 2 == 0:
            count += 1
                     
print(count)   