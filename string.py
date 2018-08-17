name = "ruby"
#slice
print(name[1])

#range slice
print(name[0:3])
print(name[:3])

#membership
print('u' in name)
print('a' not in name)

#formatted output
message = "hello"
print('%s, %s' % (name, message))

#concatenate
print(name + "," + message)

#repeat
print(name*2)

#replace
old_string = "oldString"
new_string = old_string.replace("old", "new")
print(new_string)
#immutable string
print(old_string)

#upper and lower case
print(name.upper())
print(name.capitalize())
print(name.lower())

#join
print(":".join(name))

#reverse
#the reversed() returns the reversed iterator of the given string
reversed_name = reversed(name)
print(reversed_name)
print("".join(reversed(name)))

#split
information="hello python you are so interesting"
print(information.split(' '))



