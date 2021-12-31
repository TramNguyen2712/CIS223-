# Encrypting strings by converting them into other strings depending on a key
# A key is a re-arrangement of the alphabet

# given a message
# message   = "the eagle has landed"
# alphabet  = "abcdefghijklmnopqrstuvwxyz"
# key       = "mnopqrstuvwxyzabcdefghijkl"
# encrypted = "ftq qms...

# create a list of characters from a string
message = "the eagle has landed"
characters = [i for i in message]
print(characters)

characters = list(message)
print(characters)


