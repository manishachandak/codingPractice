# write code to print largest of 3 nos.
a = int(input("enter 1st no."))
b = int(input("enter 2nd no."))
c = int(input("enter 3rd no."))
if a > b > c:
    print("a is largest")
else:
    if b > c:
        print("b is largest")
    else:
        print("c is largest")
