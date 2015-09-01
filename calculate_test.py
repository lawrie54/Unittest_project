import unittest 
from calculate import Calculate


class TestCalculate(unittest.TestCase):

    def setUp(self):
         self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
         self.assertEqual(4, self.calc.add(2,2))

    def test_add_method_raises_typeerror_if_not_ints(self):
         self.assertRaises(TypeError, self.calc.add, "Hello", "World")

    def test_assert_equal(self):
        self.assertEqual(1, 1)

    def test_assert_almost_equal_delta_0_5(self):
        self.assertAlmostEqual(1, 1.2, delta=0.5)

    def test_assert_almost_equal_places(self):
        self.assertAlmostEqual(1, 1.00001, places=4)


    def test_assert_true(self):
        self.assertTrue(1)
        self.assetTrue("Hello, World")        

if __name__ == '__main__':
     unittest.main()

