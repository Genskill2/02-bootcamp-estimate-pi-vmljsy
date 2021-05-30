import math
import unittest
import random
def wallis(n):
    pi = 0.0   
    for i in range(1, n):
        x = 4 * (i ** 2)
        y = x - 1
        z = x / y
        if (i == 1):
            pi = z
        else:
            pi *= z
    pi *= 2
    print(f"wallis {pi}")
    return pi

def monte_carlo(n):
    pi=0.0
    cp=0
    sp=0
    for i in range(n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        dist=(x**2+y**2)
        
    pi *= 2
    return pi

def monte_carlo(n):
    cp=0.0
    sp=0.0
    for i in range(n):
        x=random.random()
        y=random.random()
        dist=((x**2) +(y**2))**0.5
    if dist<=1:
        cp+=1
    sp+=1
    pi =4*cp/sp
    return pi

    if dist<=1:
        cp+=1
    sp+=1
    pi =4*cp/sp

    print(f"monte {pi}")
    return pi




class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(700, 800):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()

