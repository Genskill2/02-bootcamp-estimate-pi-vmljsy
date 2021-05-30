import math
import unittest
import random


def wallis(n):
	ans=1
	for i in range(1,n+1):
		ans *= ((4*(i**2))/(4*(i**2)-1))
	return ans*2
	

def monte_carlo(n):
	in_circle=0
	total=0
	for i in range(n):
		x= random.random()
		y= random.random()
		dist =((x**2)+(y**2))**0.5
		if dist<=1:
			in_circle+=1
			total+=1
		else:
			total+=1
	return (4*in_circle/total);
	
	
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")

