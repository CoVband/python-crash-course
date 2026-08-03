guest_list = ['mary', 'jesus', 'joseph']
print(guest_list)

# Dinner invite to Mary
print("Hi " + guest_list[0].title() + ", would you like to have dinner with us this evening?")

# Dinner invite to Jesus
print("Hi " + guest_list[1].title() + ", would you like to have dinner with us this evening?")

# Dinner invite to Joseph
print("Hi " + guest_list[2].title() + ", would you like to have dinner with us this evening?")

# Changing Guest List Exercise 3-5
# One of the guests can't make it
cannot_make_it = guest_list[1]
print("Hi, unfortunately " + cannot_make_it + " can't make it.")

# Modifying list with new person and removing the person that can't make it
# Removing person with remove()
guest_list = ['mary', 'jesus', 'joseph']
guest_list.remove('jesus')
print(guest_list)

# Removing person with del
guest_list = ['mary', 'jesus', 'joseph']
del guest_list[1]
print(guest_list)

# Inserting the new guest to the list
guest_list.insert(1,'gabriel')
print(guest_list)

# New set of invitations with new guest list
print("Hi " + guest_list[0].title() + ", we're having dinner tonight; would you like to come?")
print("Hi " + guest_list[1].title() + ", we're having dinner tonight; would you like to come?")
print("Hi " + guest_list[2].title() + ", we're having dinner tonight; would you like to come?")

# More Guests Exercise 3-6

# Found bigger dinner table statement
print("Great news folks! We've found a bigger dinner table!")

# Adding new guests to the list
guest_list.insert(0, 'sean')
guest_list.insert(2, 'damian')
guest_list.append('chris')
print(guest_list)

# Sending new set of invitations
print("\tHi " + guest_list[0].title() + ", we're having dinner tonight; would you like to come?")
print("\tHi " + guest_list[1].title() + ", we're having dinner tonight; would you like to come?")
print("\tHi " + guest_list[2].title() + ", we're having dinner tonight; would you like to come?")
print("\tHi " + guest_list[3].title() + ", we're having dinner tonight; would you like to come?")
print("\tHi " + guest_list[4].title() + ", we're having dinner tonight; would you like to come?")
print("\tHi " + guest_list[5].title() + ", we're having dinner tonight; would you like to come?")


# Shrinking Guest List Exercise 3-7

# Message letting people know that there will be only two invitations
print("Hey folks! I'm sorry to say that the new dinner table will not be arriving on time, and we'll be able to invite only two people.")

# Using pop() to remove people from the list

# Removing and uninviting Chris
print(guest_list)
uninvited_1 = guest_list.pop()
print("Hi " + uninvited_1.title() + ", We're sorry to say that we will be unable to accomadate you for this dinner.")
# Removing and uninviting Damian
uninvited_2 = guest_list.pop(2)
print(guest_list)
print("Hi " + uninvited_2.title() + ", We're sorry to say that we will be unable to accomadate you for this dinner.")
# Removing and uninviting Sean
uninvited_3 = guest_list.pop(0)
print(guest_list)
print("Hi " + uninvited_3.title() + ", We're sorry to say that we will be unable to accomadate you for this dinner.")
# Removing and uninviting Gabriel
uninvited_4 = guest_list.pop(2)
print(guest_list)
print("Hi " + uninvited_4.title() + ", We're sorry to say that we will be unable to accomadate you for this dinner.")

# Sending new invitations to people still on the list
print("\tHi " + guest_list[0].title() + ", we're having dinner tonight; would you like to come?")
print("\tHi " + guest_list[1].title() + ", we're having dinner tonight; would you like to come?")

# Using del to delete the guest on the list

# Deleting Gabriel
del guest_list[1]
print(guest_list)
# Deleting Mary
del guest_list[0]
print(guest_list)