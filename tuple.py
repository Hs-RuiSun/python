#declare
tuple = ('Monday', 'Tuesday', 'Wednesday')
empty_tuple = ()
number_tuple = (1, 2, 3, 4)

#slice
print(number_tuple[1])
print(number_tuple[1:3])

#using tuples as keys
a={'x':100, 'y':200}
b=list(a.items())
print(b)

#packing and unpacking
(company, emp, profile) = ("Guru99", 20, "Education")
print(company)
print(emp)
print(profile)

#comparing
a = (5, 1)
b = (1, 2)
if( a > b ):
    print("a is bigger")
else:
    print("b is bigger")