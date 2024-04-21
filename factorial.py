import unittest

def factorial(valor):
    if valor > 0:
        return valor * factorial(valor - 1)
    return 1
result = factorial(5)
print(result)

class TestFactorial(unittest.TestCase):

    def test_factorial_con_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado,1)

    def test_factoial_con_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado,2)

    def test_factoial_con_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado,6)

    def test_factoial_con_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado,24)

    def test_factoial_con_5(self):
        resultado = factorial(5)
        self.assertEqual(resultado,120)
    
    def test_factoial_con_6(self):
        resultado = factorial(6)
        self.assertEqual(resultado,720)




    


unittest.main()
