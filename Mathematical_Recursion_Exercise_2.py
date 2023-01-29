import math

def mystery1(x):
#Input	Return
#-2	      6
#5	     -15
#0.5	-1.5
#-0.1	0.3
    return  -x * 3
print(mystery1(-2))
print(mystery1(5))
print(mystery1(0.5))
print(mystery1(-0.1))
print("")

def mystery2(x):
#Input	Return
#4	     11
#-2	      5
#-11	-4
#2.1	9.1
  return x + 7
print(mystery2(4))
print(mystery2(-2))
print(mystery2(-11))
print(mystery2(2.1))
print("")


def mystery3(x):
#Input	Return
#3	      5
#10	      19
#0	      -1
#0.5	   0
  return (2*x) - 1
print(mystery3(3))
print(mystery3(10))
print(mystery3(0))
print(mystery3(0.5))
print("")

def mystery4(x, y):
#Input	Return
#2, 3	     -1
#10, 6	      4
#5, 7	     -2
#0.3, 0.5	-0.2
  return x - y
print(mystery4(2,3))
print(mystery4(10,6))
print(mystery4(5,7))
print(mystery4(0.3,0.5))
print("")

def mystery5(x):
#Input	Return
#-2	     -4
#-1	     -2
#0	     1000
#1	     1000
#2	     1000
#3	     1000
#0.3	     1000
#-0.3	 -0.6
  if x<0:
    return x * 2
  else:
    return 1000
print(mystery5(-2))
print(mystery5(-1))
print(mystery5(0))
print(mystery5(1))
print(mystery5(2))
print(mystery5(3))
print(mystery5(0.3))
print(mystery5(-0.3))
print("")
def mystery6(x):
#Input	Return
#10	     98
#5	     23
#0	     -2
#0.1	-1.99
#-7	     47
  return (x*x) - 2
print(mystery6(10))
print(mystery6(5))
print(mystery6(0))
print(mystery6(0.1))
print(mystery6(-7))
print("")
def mystery7(x, y):
#Input	Return
#2,3	     2
#-2,3	     3
#7,-21	   7
#-7,-21	- 21
#0.5,0.2	0.5
#-0.5,0.2	0.2
#0,0	     0
#0,12	    12
#0.1,12	  0.1
  if x>0:
    return x
  else:
    return y
print(mystery7(2,3))
print(mystery7(-2,3))
print(mystery7(7,-21))
print(mystery7(-7,-21))
print(mystery7(0.5,0.2))
print(mystery7(-0.5,0.2))
print(mystery7(0,0))
print(mystery7(0,12))
print(mystery7(0.1,12))
print("")

def mystery8(x):
#Input	Return
#-2	       0
#-1	      19
#0	       0
#1	      19
#2	       0
#3	      19
#4	       0
#5	       19
#6	       0
  if x%2 == 1:
    return 19
  else:
    return 0
print(mystery8(-2))
print(mystery8(-1))
print(mystery8(0))
print(mystery8(1))
print(mystery8(2))
print(mystery8(3))
print(mystery8(4))
print(mystery8(5))
print(mystery8(6))
print("")

def mystery9(x):
#Input	Return
#-2	     -4
#-1	     -1
#0	      0
#1	     -1
#2	      4
#3	     -1
#4	      8
#5	     -1
#6	     12
  if x%2 == 1:
    return -1
  else:
    return x * 2
print(mystery9(-2))
print(mystery9(-1))
print(mystery9(0))
print(mystery9(1))
print(mystery9(2))
print(mystery9(3))
print(mystery9(4))
print(mystery9(5))
print(mystery9(6))
print("")
def mystery10(x, y):
#Input	Return
#2,6	   30
#6,2	   30
#-1,7	   35
#-1,-2	 -5
#0.6,0.8	4
#-10,0.1	0.5
#-10,-11	-50
  if x > y:
    return x*5
  if x < y:
    return y*5
  else:
    return x*5
print(mystery10(2,6))
print(mystery10(6,2))
print(mystery10(-1,7))
print(mystery10(-1,-2))
print(mystery10(0.6,0.8))
print(mystery10(-10,0.1))
print(mystery10(-10,-11))
print("")

def mystery11(x):
#Input	Return
#0	      0
#1	      4
#2	      1
#3	     10
#4	      2
#5	     16
#6	      3
#7	     22
  if x%2 == 1:
    return int((x*3) + 1)
  else:
    return int(x/2)

print(mystery11(0))
print(mystery11(1))
print(mystery11(2))
print(mystery11(3))
print(mystery11(4))
print(mystery11(5))
print(mystery11(6))
print(mystery11(7))
print("")

def mystery12(x):
#Input	Return
#0	      0
#1	      0
#2	      0
#3	      1
#4	      1
#5	      1
#6	      2
#7	      2
  if x<3:
    return 0
  else:
    return math.floor(x/3)

print(mystery12(0))
print(mystery12(1))
print(mystery12(2))
print(mystery12(3))
print(mystery12(4))
print(mystery12(5))
print(mystery12(6))
print(mystery12(7))
print("")

