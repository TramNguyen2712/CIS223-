from Stacks import ArrayStack

######################################################
# Reversing Data using a stack
# IDEA: push values on a stack and then pop elements one at a time

def reverse_file(filename, extension):
    S = ArrayStack()
    in_file = open(filename + "." + extension, "r")
    for line in in_file:
        S.push(line.rstrip('\n'))  # copy of the string with trailing empty characters removed
    in_file.close()

    out_file = open(filename + "_reverse." + extension, "w")

    while not S.is_empty():
        out_file.write(S.pop() + "\n")
    out_file.close()



######################################################
# Matching delimiters
# Parenthesis ()
# Braces {}
# Brackets []

# Algorithm: Using a stack, we assume we have a sequence of characters representing an expression
# for instance, an arithmetic expression. Scan the expression and when we encounter a delimiter
# such as (, {, [ push it into the stack
# When we encounter a closing delimiter, we pop the stack
# Problems:
# there is no matching opening delimiter at the top of the stack
# stack could be empty

def is_matched(expression):
    """Checks delimiter matching on arithmetic expressions"""
    opening = "({["
    closing = ")}]"
    S = ArrayStack()
    for c in expression:
        if c in opening:
            S.push(c)
        elif c in closing:
            if S.is_empty():
                return False
            if closing.index(c) != opening.index(S.pop()):
                return False

    return S.is_empty()

#print(is_matched("(5 + 6) / [7 * 9]"))

# Analysis:
# There are at most n push() calls if length of string is n
# All steps take O(1)
# Thus O(n)


######################################################
# Matching Tags in Markup language: HTML, XML

def html_tag_match(filename, extension="html"):
    file = open(filename + "." + extension)
    raw = "".join(filename.realines())        # read the entire contents at once
    file.close()

    S = ArrayStack()
    j = raw.find("<")       # find the first < you see
    while j != -1:
        # see .find() in http://docs.python.org/3/library/stdtypes.html
        k = raw.find(">", j+1)      # return lowest index of string raw[j+1:], return -1 if nothing is found
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith("/"):  # an opening tag
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k+1)
    return S.is_empty()


# Analysis:
# O(n)








if __name__ == "__main__":
    reverse_file("gettysburg", "txt")
