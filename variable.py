# declare a global variable
f = 100
print(f)

def local_function():
    global f
    print(f)
    f = "local variable"

local_function()
print(f)
