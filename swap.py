#def swap(a, b):
#    return b, a

#a=int(input("Enter a: "))
#b=int(input("Enter b: "))

#print("Swapped numbers are" + swap(a, b))


#C approach to swap

def swap(a, b):
    temp=a
    a=b
    b=temp
    return a, b

a=int(input("Enter a: "))
b=int(input("Enter b: "))

a, b = swap(a, b)

print("Swapped numbers are: ", a, b)