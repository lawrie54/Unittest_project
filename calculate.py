class Calculate(object):
    def add(self, x, y):
         """Takes two integers and adds them together to produce   
         the result."""
         return x + y

if __name__ == '__main__':
    import doctest  
    doctest.testmod()
    calc = Calculate()
    result = calc.add(2, 2) 

    print result



