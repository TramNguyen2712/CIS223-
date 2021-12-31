# R-2.4
"""Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent
the name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes each variable to an approciate
value, and your class should include methods for setting the value of each type, and retrieving the value of each type """
import math


class Flower:
    def __init__(self, name, number, price):
        """Create Flower instance"""
        self._name = name  # name of flower
        self._number = number  # number of petals
        self._price = price  # its price

    def set_name(self, name):
        """Set the name of flower"""
        self._name = str(name)

    def set_number(self, number):
        """Set the number of petals"""
        self._number = number

    def set_price(self, price):
        """Set the price"""
        self._price = price

    def get_name(self):
        """Return the name of flower"""
        return self._name

    def get_number(self):
        """Return the number of petals"""
        return self._number

    def get_price(self):
        """Return the price"""
        return self._price

    def print_flower(self):
        """Show the output"""
        """%s for string, %d for number, %.2f for float"""
        print(
            '%s contains %d number of petals and costs $%.2f.' % (self.get_name(), self.get_number(), self.get_price()))


if __name__ == '__main__':
    n = Flower('Tulip', 3, 9.2)
    n.print_flower()
    print()

# R-2.13
"""Exercise R-2.12 asks for an implementation of __mul__, for th Vector class of Section 2.3.3, 
to provide support for the syntax v*3. Implement the __rmul__ method, to provide additional support for syntax 3*v"""


class Vector:
    """Represent a vector in a multidimensional space"""

    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension fo the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value"""
        self._coords[j] = val

    def __mul__(self, other):
        """Return the multiply for the syntax v*3"""
        if len(self) != len(other):  # 2 vectors must have the same length
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # set result have same length to vector
        for j in range(len(self)):
            result[j] = self[j] * other[j]  # v * 3
        return result

    def __rmul__(self, other):
        """Return the right multiply for the syntax 3 * v"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] * self[j]  # 3 * v
        return result

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'

    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vectors differ from each other"""
        return not self == other  # relies on existing __eq__method


if __name__ == '__main__':
    n = Vector(3)
    n[0] = 1
    n[1] = 2
    n[2] = 3
    print('Vector n is', n)
    u = n * [3, 4, 5]
    print(u)
    u = [3, 4, 5] * n
    print(u)
    print()
# R-2.14
"""Implement the mul method for the Vector class of Section 2.3.3, 
so that the expression u v returns a scalar that represents the dot product of the vectors."""


class Vector2(Vector):
    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        """dot product equation = a · b = ax × bx + ay × by"""
        result = 0
        for j in range(len(self)):
            result += self[j] * other[j]
        return result


if __name__ == '__main__':
    n = Vector2(3)
    n[0] = 1
    n[1] = 2
    n[2] = 3
    u = n * [3, 4, 5]
    print("Dot product of n and v vector is %d " % (u))
    print()

# R-2.16
"""Our Range class, from Section 2.3.5, relies on formula
max(0,(stop - start + step -1) // step) to compute the number of elements in range. 
It is not immediately evident why this formula provides the correct calculation,
even if assuming  a positive step size. Justify this formula, in your own words"""

"""Explain:
1. (stop - start + step -1) 
stop - start : distance from stop to start
stop - start + step: to make sure the last element is outputted.
stop - start + step -1: the stop is not inclusive

2. (stop - start + step -1) // step
Dividing by step account for the range's splitting by an equal number (step).
Using the floor division because the range should only have the countable number of length
 
3. max(0,(stop - start + step -1) // step)
Use max to make sure this is an output."""

# R-2.19
"""Given a short fragment of Python code that uses the progression classes from Section 2.4.2 to find the 8th value
of a Fibonacci progression that starts with 2 and 2 as its first two values"""


class Progression:
    """Iterator producing a generic progression
    Default iterator produces the whole number 0,1,2,..."""
    def __init__(self, start=0):
        """Initialize current to the first value of the progression"""
        self._current = start

    def _advance(self):
        """Update self._current to a new value"""
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      # record current value to return
            self._advance()             # advance to prepare for the next time
            return answer               # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def print_progression(self, n):
        """Print next n values of the progression"""
        print(",".join(str(next(self)) for j in range(n)))


class FibonacciProgress(Progression):
    """Iterator producing a generalized Fibonacci progression"""
    def __init__(self, first=1, second=1):
        """Create a new Fibonacci progression"""
        super().__init__(first)  # start progression at first
        self._prev = second - first  # fictitious value preceding the first
        self.list = [first, second]  # create a list contains already the first and second number

    def _advance(self):
        """Update current value by taking sum of previous two"""
        self._prev, self._current = self._current, (self._prev + self._current)
        self.list.append(self._current)  # add new current value to the list

    def value(self, i):
        """Get value by given index"""
        if isinstance(i, int) and i >= 0:  # index must be integer and positive number
            return self.list[i]  # print value from list


if __name__ == '__main__':
    n = FibonacciProgress(first=2, second=2)
    n.print_progression(10)
    print('The 8th value of a Fibonacci progression is', n.value(8))
    print()
# C-2.28
"""The PredatoryCreditCard class of Section 2.4.1 provides a process month
method that models the completion of a monthly cycle. Modify the class
so that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge."""


class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance. The initial balance is zero."""
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        self._charge_count = 0

    def get_customer(self):
        """Return the name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically a str)"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def get_charge_count(self):
        """Return current balance"""
        return self._charge_count

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit. Return True if charge was processed,
        False if charge was denied"""

        if not isinstance(price, (float, int)):
            raise ValueError('price must be a number.')
        if price + self._balance > self._limit:
            print(f"Credit card with account number {self._account} denied. Accrued balance over limit.")
            return False
        else:
            self._balance += price
            self._charge_count += 1
            if self._charge_count > 10:
                self._balance += 1  # $1 surcharge for additional calls after 10 calls
            return True

    def make_payment(self, amount):
        # if not isinstance(amount, (int, float)):
        #     raise ValueError('payment must be a number')
        # elif amount < 0:
        #     raise ValueError('payment must be positive')
        """Process customer payment that reduces the balance"""
        self._balance -= amount


if __name__ == "__main__":
    wallet = [CreditCard('liz', 'bofa', '123 123 123 123', 2500)]

    for val in range(1, 13):
        wallet[0].charge(val)
        if val >= 10:
            print(f'{wallet[0].get_charge_count()} call to charge:', wallet[0].get_balance())

    print('Customer =', wallet[0].get_customer())
    print('Bank = ', wallet[0].get_bank())
    print('Account = ', wallet[0].get_account())
    print('Limit = ', wallet[0].get_limit())
    print('Balance =', wallet[0].get_balance())
    while wallet[0].get_balance() > 100:
        wallet[0].make_payment(100)
        print('New balance =', wallet[0].get_balance())
    print()
# C-2.31
"""Write a Python class that extends the Progression class so that each value
in the progression is the absolute value of the difference between the previous two values. 
You should include a constructor that accepts a pair of
numbers as the first two values, using 2 and 200 as the defaults."""


class DiffAbsVal(Progression):  # extends the Progression
    """Iterator producing a generalized new progression"""
    def __init__(self, first=2, second=200):
        """"Create a new progression"""""
        super().__init__(second)    # initialize base case
        self._prev = first

    def _advance(self):    # override inherited version
        """Update current value by taking the difference between the previous two."""
        temp = self._prev
        self._prev = self._current
        self._current = abs(self._prev - temp)  # result must be a absolute value

    def __next__(self):    # override inherited version
        """Return the next element, or else raise StopIteration error"""
        if self._prev is None:
            raise StopIteration()
        else:
            answer = self._prev   # record the previous value to return
            self._advance()       # advance to prepare for next time
        return answer             # return answer


if __name__ == "__main__":
    n = DiffAbsVal()
    print('The Different Absolute Value Progression with 2 and 200 as first two values ')
    n.print_progression(7)
    print()

# C-2.32
"""Write a Python class that extends the Progression class so that each value
in the progression is the square root of the previous value. (Note that
you can no longer represent each value with an integer.) Your constructor should 
accept an optional parameter specifying the start value, using 65,536 as a default."""


class SqrtRoot(Progression):
    """Iterator producing a generalized Square Root progression"""
    def __init__(self, start=65536):
        """"Create a new Square Root progression"""""
        super().__init__(start)     # initialize base case

    def _advance(self):     # override inherited version
        """Update the current value"""
        self._current = self._current ** 1 / 2    # the each value is the square root of the previous value


if __name__ == "__main__":
    n = SqrtRoot()
    print('The Square Root Progression with 65536 as a start value ')
    n.print_progression(7)
    print()

# P-2.33
"""Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the first derivative of that polynomial."""
"""[HINT: Represent the polynomial ax1n1+bx2n2+. . .as a list of tuples [(a, x1, n1),(b, x2, n2), ...]"""
"""Assume: Input 2*x^3 + 3*x^2 + 4x + 1
           Output 6*x^2 + 6*x + 4"""
"""c*x^p
 c: coefficient
 p: power"""
import re

def coefficient(c):   #set coefficient for polynomial
    if c > 1:
        return str(c)
    else:
        return ''     # for case c = 0

def power(p):     #set power for polynomial
    if p == 0:
        return ''
    elif p == 1:
        return '*x'
    else:
        return '*x^%d' %(p,)

def polynomial(poly):
    n = poly.split('+')
    poly_eq = [re.split('\*x\^?',i) for i in n] # split  on x^
    list = []  # create the new list
    for j in poly_eq:
        """j = [c,p]"""
        try:
            coeff = int(j[0])
        except ValueError:
            coeff = 1
        try:
            power_ = int(j[1])
        except ValueError:
            power_ = 1
        except IndexError:
            power_ = 0
        list.append((coeff,power_))
    return list

def print_polynomial(list):
    result = [(coefficient(c)+power(p)) for c,p in list if c!=0]
    return '+'.join(result)

def first_derivative(poly):
    list = polynomial(poly)
    derivative =[(p*c,p-1) for c,p in list]
    return print_polynomial(derivative)


if __name__ == "__main__":
    print(first_derivative('2*x^3+4*x^2+4*x'))
    print()

# P-2.39
"""Develop an inheritance hierarchy based upon a Polygon class that has
abstract methods area( ) and perimeter( ). Implement classes Triangle,
Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
class, with the obvious meanings for the area( ) and perimeter( ) methods.
Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle, and Square, 
that have the appropriate inheritance relationships. Finally, write a simple program that allows users 
to create polygons of the various types and input their geometric dimensions, and the program then
outputs their area and perimeter."""

from abc import ABCMeta, abstractmethod, ABC


class Polygon(metaclass=ABCMeta):
    """Polygon abstract base class"""
    def __init__(self, n):
        """number of sides that depends on the types of the polynomial"""
        self._number_sides = n

    def get_number_sides(self):
        """Return the number of sides"""
        return self._number_sides

    @abstractmethod
    def perimeter(self):
        """Return the perimeter for each polygon"""

    @abstractmethod
    def area(self):
        """Return the area for each polygon"""


class Triangle(Polygon):    # inherit from Polygon
    def __init__(self, x, y, z):
        """Create a new triangle"""
        super().__init__(3)
        self._x = x
        self._y = y
        self._z = z

    def perimeter(self):
        """Return the perimeter of triangle"""
        return self._x + self._y + self._z

    def area(self):
        """Return the area of triangle"""
        s = (self._x + self._y + self._z) / 2
        return math.sqrt(s * (s - self._x) * (s - self._y) * (s - self._z))


class Quadrilateral(Polygon):  # inherit from Polygon
    def __init__(self, x, y, z, h):
        """Create the new Quadrilateral"""
        super().__init__(4)
        self._x = x
        self._y = y
        self._z = z
        self._h = h

    def perimeter(self):
        """Return the perimeter of quadrilateral"""
        return self._x + self._y + self._z + self._h

    def area(self):
        """Return the area of quadrilateral"""
        """The area of quadrilateral is based on its type"""
        pass


class Pentagon(Polygon):    # inherit from Polygon
    def __init__(self, x):
        super().__init__(5)
        self._x = x

    def perimeter(self):
        """Return the perimeter of pentagon"""
        return self._number_sides * self._x

    def area(self):
        """Return the area of pentagon"""
        return 1 / 4 * math.sqrt(5 * (5 + math.sqrt(5))) * math.pow(self._x, 2)


class Hexagon(Polygon):   # inherit from Polygon
    def __init__(self, x):
        super().__init__(6)   # call super constructor
        self._x = x

    def perimeter(self):
        """Return the perimeter of hexagon"""
        return self._number_sides * self._x

    def area(self):
        """Return the area of hexagon"""
        return 2 * (1 + math.sqrt(2)) * self._x ** 2


class Octagon(Polygon):  # inherit from Polygon
    def __init__(self, x):
        super().__init__(8)   # initialize base class
        self._x = x

    def perimeter(self):
        """Return the perimeter of octagon"""
        return self._number_sides * self._x

    def area(self):
        """Return the area of octagon"""
        return 2 * (1 + math.sqrt(2)) * self._x ** 2


class Equilateral_Triangle(Triangle):   # inherit from Triangle
    def __init__(self, x):
        Triangle.__init__(self, x, x, x)   # initialize Triangle class

    """The perimeter formula of equilateral triangle likes triangle """
    def area(self):
        """Return the area of equilateral triangle"""
        return (math.sqrt(3) / 4) * math.pow(self._x, 2)


class Square(Quadrilateral):    # inherit from Quadrilateral
    def __init__(self, x):
        super().__init__(x, x, x, x)  # call super constructor

    """The perimeter formula of square likes quadrilateral """
    def area(self):  # override inherited version
        """Return the area of square"""
        return self._x ** 2


class Rectangle(Quadrilateral): # inherit from Quadrilateral
    def __init__(self, x, y):
        super().__init__(x, y, x, y)

    """The perimeter formula of rectangle likes quadrilateral """

    def area(self):
        """Return the area of rectangle """
        return self._x * self._y


class IsoscelesTriangle(Triangle): # inherit from Triangle
    def __init__(self, x, y):
        Triangle.__init__(self, x, x, y)   # initialize Triangle class

    """The perimeter formula of Isosceles Triangle likes triangle """

    def area(self):   # override
        """Return the area of isosceles triangle"""
        attitude = math.sqrt(math.pow(self._x, 2) + math.pow(self._z / 2, 2))
        return (attitude * self._z) / 2


if __name__ == "__main__":
    triangle = Triangle(4, 5, 3)
    print("Triangle perimeter:", triangle.perimeter())
    print("Triangle area:", triangle.area())
    print()

    hexagon = Hexagon(3)
    print("Hexagon perimeter:", hexagon.perimeter())
    print("Hexagon area:", format(hexagon.area(),'.2f'))
    print()

    square = Square(5)
    print("Square perimeter:", square.perimeter())
    print("Square area:", square.area())
    print()

    pentagon = Pentagon(20)
    print("Pentagon perimeter:", hexagon.perimeter())
    print("Pentagon area:", format(hexagon.area(), '.2f'))
    print()

    isosceles = IsoscelesTriangle(5,7)
    print("Isosceles Triangle perimeter:", isosceles.perimeter())
    print("Isosceles Triangle area:", format(isosceles.area(), '.2f'))
    print()

    equil = Equilateral_Triangle(3)
    print("Equilateral Triangle perimeter:", equil.perimeter())
    print("Equilateral Triangle area:", format(equil.area(), '.2f'))
    print()

    octagon = Octagon(4)
    print("Octagon perimeter:", octagon.perimeter())
    print("Octagon area:", format(octagon.area(), '.2f'))
    print()


