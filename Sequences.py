# Numeric progressions or sequences

# Fundamental principle of sequences is that they are subsets of the integers with a minimum element

# Thus, we begin by defining the most basic subset of integers which is the set of natural numbers
# {0, 1, 2, 3 ...}


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
        self._prev, self._current = self._a*self._current, self._b*(self._prev + self._current)



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

    GS1 = GeometricSequence(1/2, 20)
    GS1.print_sequence(10)

    GS2 = GeometricSequence(2, 1)
    GS2.print_sequence(20)

    FS1 = FibonacciSequence()
    FS1.print_sequence(10)

    FS2 = FibonacciSequence(4, 7, 2, 3)
    FS2.print_sequence(10)