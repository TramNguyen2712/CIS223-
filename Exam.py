"""
1. Python 3.x basics control structures:for, while, if-elif-else
2. Basic types: int,float, and boolean
3. Collection types: string, list, dictionary, tuple, set
4. How to make functions with a def -return statement
5. Object-oriented programming with Python 3.x basics: encapsulation, inheritance,
polymorphism

Bonus topics:
6. How to make generators with a def -yield statement
7. How to make generator classes: use of next()
8. Sequences: arithmetic, geometric, fibonacci.
9. Comprehensions to build lists and generators.

"""

# 1. Python 3.x basics control structures:for, while, if-elif-else
print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
# map from letter grade to point value
points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
          'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()  # read line from user
    if grade == '':  # empty line was entered
        done = True
    elif grade not in points:  # unrecognized grade entered
        print("Unknown grade {0} being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
    if num_courses > 0:  # avoid division by zero
        print('Your GPA is {0:.3}'.format(total_points / num_courses))
print()

# while
"""while condition:
        body"""
"""
j= 0
while j < len(data) and data[j] != X :
    j += 1"""
# if...else
"""if first condition:
        first body
    elif second condition:
        second body
    elif third condition:
        third body
    else:
        fourth body"""

# for
"""
for element in iterable:
    body"""
"""
total = 0
for val in data:
total += val"""

# 2. Basic types: int, float, and boolean
"""Boolean"""
"""Numbers evaluate to False if zero, and True if nonzero. 
Sequences and other container types, such as strings and lists, evaluate to False if empty and True if nonempty"""

"""int"""
"""The int class is designed to represent integer values with arbitrary magnitude
For example, both int(3.14) and int(3.99) produce the value 3, 
while int(−3.9) produces the value −3."""

print(int(3.14))

"""If s represents a string, then int(s) produces the integral value that string represents. 
For example, the expression int('137') produces the integer value 137. 
If an invalid string is given as a parameter, as in int('hello'), a ValueError is raised"""

"""By default, the string must use base 10. If conversion from a different base is desired, that
base can be indicated as a second, optional, parameter.

int("12",5) => 1*(5 ^ 1) + 2*(5 ^ 0) = 7
int("0",5) => 0*(5 ^ 0) = 0
int("10", 2) => 1*(2 ^ 1) + 0*(2 ^ 0) = 2"""

print(int('12', 5))

"""The constructor form of float( ) returns 0.0. When given a parameter, the constructor attempts to return the equivalent floating-point value. For example, the call
float(2) returns the floating-point value 2.0. If the parameter to the constructor is
a string, as with float('3.14'), it attempts to parse that string as a floating-point
value, raising a ValueError as an exception"""

print(float('3.14'))

# 3. Collection types: string, list, dictionary, tuple, set
"""Lists are array-based sequences and are zero-indexed, thus a list of length n has elements
indexed from 0 to n−1 inclusive."""
"""For example:"""
l = ['red', 'green', 'blue']
n = list('hello')  # ['h', 'e', 'l', 'l', 'o']
print(n)

"""The tuple class provides an immutable version of a sequence, and therefore its
instances have an internal representation that may be more streamlined than that of
a list."""
"""For example:"""
tuple1 = (1, 2, 3, 4)
print(tuple1[1:3])  # print start at element with index 1, stop at element with index 3
# Output: (2,3)

"""String literals can be enclosed in single quotes, as in hello , or double
quotes, as in "hello"."""
"""the quote delimiter can be designated using a backslash as a so-called escape character, as in Don\ t worry . 
Because the backslash has this purpose, the backslash must itself be escaped to occur as a natural character of the string literal, 
as in C:\\Python\\ , for a string that would be displayed as C:\Python\."""
"""Other commonly escaped characters are \n for newline
and \t for tab. Unicode characters can be included, such as 20\u20AC for the
string 20 """
print('20\u20AC')  # 20€

"""Python’s dict class represents a dictionary, or mapping, from a set of distinct keys
to associated values"""
"""For example, the dictionary { 'ga' : 'Irish' , 'de' : 'German' } maps
'ga' to 'Irish' and 'de' to 'German' ."""
""" pairs = [( ga , Irish ), ( de , German )]"""
pairs = [('ga', 'Irish'), ('de', 'German')]
print(dict(pairs))

# 4. How to make functions with a def -return statement
"""a return statement will be the final command within the
body of the function, as was the case in our earlier example of a count function"""


def contains(data, target):
    for item in target:
        if item == target:  # found a match
            return True
    return False


# 5. Object-oriented programming with Python 3.x basics: encapsulation, inheritance, polymorphism
"""Encapsulation"""
"""One of the main advantages of encapsulation is that it
gives one programmer freedom to implement the details of a component, without
concern that other programmers will be writing code that intricately depends on
those internal decisions"""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age

    def display(self):
        print(self.name)
        print(self._age)


"""Inheritance"""
"""A derived/subclass class usually derives/inherits/extends the base/super class."""
"""
class SuperClassName:
  Body of Super class
 
class DerivedClass_Name(SuperClass):
  Body of derived class"""


class Father:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def printname(self):
        print(self.name, self.lastname)


class Son(Father):
    def __init__(self, name, lastname):
        super().__init__(name, lastname)


"""Polymorphism"""
"""The codes and classes written once can be reused and implemented multiple times."""


class Animal:
    def type(self):
        print("Various types of animals")

    def age(self):
        print("Age of the animal.")


class Rabbit(Animal):
    def age(self):
        print("Age of rabbit.")


class Horse(Animal):
    def age(self):
        print("Age of horse.")
    # 6. How to make generators with a def -yield statement


"""A generator is implemented with a syntax that is very similar to a function, 
but instead of returning values, a yield statement is executed to indicate each element of the series"""
"""For each iteration of the loop, Python executes our procedure
until a yield statement indicates the next value"""


def factors(n):  # generator that computes factors
    k = 1
    while k * k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
        if k * k == n:  # special case if n is perfect square
            yield k


n = factors(10)
print(list(n))


# output: [1,10,2,5]

# while k * k < n: #while k < sqrt(n)
#       if n % k == 0:
#           yield k
#       k += 1
#   if k*k == n: #specical case if n is perfect quare
#       yield k
#  #after yield k
#   k -= 1 #go back to yield n // k
#   while k > 0: #in case k = 0
#       if n % k == 0:
#           yield n // k
#       k -= 1

# output: [1,2,5,10]

def fibonacci():
    a = 0
    b = 1
    while True:  # keep going...
        yield a  # report value, a, during this pass
        future = a + b
        a = b  # this will be next value report
        b = future


# output: 0,1,1,2,3,5,8,13

# 7. How to make generator classes: use of next()
"""It supports a special method named __next__ that returns the next element of the collection
,if any, or raise a StopIteration exception to indicate that there are no further elements"""

"""Each time __next__ is called, the index is incremented, until reaching the end of the sequence """


class SequenceIterator:
    "An iterator for any of Python s sequence types."

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # keep a reference to the underlying data
        self._k = -1  # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1  # advance to next index
        if self._k < len(self._seq):
            return self._seq[self._k]  # return the data element
        else:
            raise StopIteration()  # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


class Range:
    """A class that mimic s the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:  # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0,n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support getitem
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step


# 8. Sequences: arithmetic, geometric, fibonacci.
class Sequence(object):
    """Produces a generic sequence, by default 0, 1, 2, ..."""

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        """Update self._current to a new value
            Override in sub_class
            If current is set to None, indicates end of a finite sequence
        """
        self._current += 1

    def __next__(self):
        # Python iterators are objects that manage values with built-in function next(i)
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def print_sequence(self, n):
        """Print next n values of the sequence"""
        print(",".join(str(next(self)) for j in range(n)))


# USING INHERITANCE DEFINE CLASSES FOR ArithmeticSequence and GeometricSequence
class ArithmeticSequence(Sequence):
    """Iterator producing an arithmetic sequence."""

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricSequence(Sequence):
    """Iterator producing a geometric sequence."""

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciSequence(Sequence):
    """Generalized Fibonacci sequence iterator."""

    def __init__(self, first=1, second=1, a=1, b=1):
        super().__init__(first)
        self._prev = second - first
        self._a = a
        self._b = b

    def _advance(self):
        self._prev, self._current = self._a * self._current, self._b * (self._prev + self._current)


if __name__ == "__main__":
    S1 = Sequence()
    S1.print_sequence(15)

    # Example generators using comprehension syntax
    # Build a generator for the first 100 even numbers
    evens_100 = (i for i in range(2, 201) if i % 2 == 0)
    print(evens_100)
    for i in range(100):
        print(next(evens_100))

    AS1 = ArithmeticSequence(2, -5)
    AS1.print_sequence(10)

    AS2 = ArithmeticSequence(7, 100)
    AS2.print_sequence(10)

    GS1 = GeometricSequence(1 / 2, 20)
    GS1.print_sequence(10)

    GS2 = GeometricSequence(2, 1)
    GS2.print_sequence(20)

    FS1 = FibonacciSequence()
    FS1.print_sequence(10)

    FS2 = FibonacciSequence(4, 7, 2, 3)
    FS2.print_sequence(10)

# 9. Comprehensions to build lists and generators.
""" A generator is implemented with a syntax that
is very similar to a function, but instead of returning values, a yield statement is
executed to indicate each element of the series"""


def fibonacci():
    a = 0
    b = 1
    while True:  # keep going...
        yield a  # report value, a, during this pass
        future = a + b
        a = b  # this will be next value reported
        b = future  # and subsequently this

"""Bult-in"""