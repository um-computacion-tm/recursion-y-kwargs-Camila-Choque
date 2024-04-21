import unittest
def fibonacci(value):
    if value < 2:
        return value
    values = [0, 1]
    for _ in range(value -1):
        values.append(values [-1] + values [-2])
    print(values)
    return values[value]

resultado = fibonacci(8)
print (resultado)





class TestFibonacci(unittest.TestCase):
   
    def test_1(self):
        self.assertEqual(1, fibonacci(1))

    def test_2(self):
        self.assertEqual(1, fibonacci(2))
    
    def test_3(self):
        self.assertEqual(2, fibonacci(3))

    def test_4(self):
        self.assertEqual(3, fibonacci(4))
    
    def test_5(self):
        self.assertEqual(5,fibonacci(5))

    def test_6(self):
        self.assertEqual(8,fibonacci(6))

   
unittest.main()
