class ImaginaryNumber:
    def __init__(self, x, y):
        self.real = x
        self.imag = y


def multiply_imag(n1, n2):
    f = n1.real * n2.real
    o = n1.real * n2.imag
    i = n1.imag * n2.real
    l = (n1.imag * n2.imag) * -1

    result = ImaginaryNumber(f + l, o + i)
    return result


def add_imag(n1, n2):
    real = n1.real + n2.real
    imag = n1.imag + n2.imag

    result = ImaginaryNumber(real, imag)
    return result
