# Learning about lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Learning to access an element in a list
print(bicycles[0])

# Using .title() and .upper()
print(bicycles[0].title()) 
print(bicycles[1].upper())

# Learning to select any element in a list
print(bicycles[2])
print(bicycles[3])

# Learning to select items with respect to the last item on a list
print(bicycles[-1])

# Using individual values from a list and creating a message
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)