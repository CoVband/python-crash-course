# Learning to use \t,\n, and removing those white spaces

# First, use the tab function and remove the white spaces
name = "\tKevin    "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Now, use the new-line function and remove the white spaces
name= "\n\nKevin     "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())