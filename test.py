from PositionalLists import PositionalList

class Update_PositionalList(PositionalList):
    def __init__(self):
        super().__init__()
        self._node = None

    def find(self,e):
        m = self.first()
        while m.element() is not e:
            if self.after(m) is not None:
                m = self.after(m)
            else:
                return None
        return self._make_position(m)


if __name__ == '__main__':
    pl = Update_PositionalList()

    # Add A, B, C so that they are in the order A, C, B
    pA = pl.add_first("A")
    pB = pl.add_after(pA, "B")
    pC = pl.add_before(pB, "C")

    # iterate through the list
    for e in pl:
        print(e)

    pFirst = pl.first()
    print(pFirst == pA)
    print(pFirst.element())
    print(pA.element())

    pLast = pl.last()
    print(pLast == pB)
    print(pLast.element())
    print(pB.element())

    pD = pl.add_last("F")
    print([e for e in pl])

    element = pl.replace(pD, "D")
    print([e for e in pl])

    # elements = pl.delete(pA)
    # pFirst = pl.first()
    # print(pFirst.elements())
    # print([e for e in pl])

    pl2 = Update_PositionalList()
    for i in range(10):
        pl2.add_first(i)

    print([i for i in pl2])

    print(pl2.find(9))