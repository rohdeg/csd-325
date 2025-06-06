#Garrett Rohde Assignment 1.3

numBottles = int(input("How many bottles of beer are on the wall? "))
while numBottles == 0 or numBottles < 0:
    print("Where is the beer?")
    numBottles = int(input("How many bottles of beer are on the wall? "))

def countdown(bottles):
    while bottles > 0:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n")
        bottles -= 1
        if bottles == 0:
            print("Take one down, pass it around, no more bottles of beer on the wall.\n")
        else:
            print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall!")

countdown(numBottles)