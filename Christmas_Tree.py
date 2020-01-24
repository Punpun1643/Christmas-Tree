height = int(input("Enter the height of the tree, greater than 9:"))

if height <= 9:
    print("Enter a number greater than 9")
else:

#let s represents the space
#let a represents the asterisk
    for i in range(1, height - 4):
        s = height - 5 - i 
        a = i * 2 - 1
        print(" " * s,"*" * a," " * s)

#code for the last 5 asterisks for the tree's base 
    for i in range(5):
        print(" " * (height - 6),"*"," " * (height - 6))
        



