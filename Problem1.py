class linear_express():
    def __init__(self, coeff):
        self._coeff = coeff

    def __len__(self):
        return len(self._coeff)

    def __repr__(self):
        result = ''
        for i in range (0,len(self._coeff)):
            if self._coeff[i] != 0:
                result += ' + %gx%d' %(self._coeff[i], i+1)
        result = result.replace('1x','x')
        result = result.replace('0x','')
        if result[1] == '+':
            result = result[3:]
        return result

    def __add__(self, other):
        for j in range(0,len(self._coeff)):
            self._coeff[j] = self._coeff[j] + other[j]
        return linear_express(self._coeff)

    def __mul__(self, c):
        for j in range(0,len(self._coeff)):
            self._coeff[j] = self._coeff[j] * c
        return linear_express(self._coeff)

n = linear_express([3,5,5])
print(n)
v = [5,1,2]
add = n + v
print(add)
print(n*4)

