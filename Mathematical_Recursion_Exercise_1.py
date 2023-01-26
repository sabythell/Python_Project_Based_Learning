def malcolm(x):
  return (2*x) + 1


def elaisa(x, y):
#Elaisa’s Function:
#  Take two inputs, x and y
#  Calculate 2x - y
#  Return the result
  return (2 * x) - y
print("elaisa")
print(elaisa(5,-11))
print("")

def akash(a):
#Akash’s Function:
#  Take one input a
#  If a is positive:
#    Return 1
#  Otherwise:
#    Return -1
  if a>0:
    return 1
  if a<0:
    return -1
print("akash")
print(akash(3))
print("")


def rosa(x):
#Rosa’s Function:
#  Take one input x
#  Send x - 1 to Malcolm’s function
#  Multiply the returned value by -1
#  Return the result
  result = malcolm(x-1) * -1
  return result
print("rosa")
print(rosa(6))
print("")


def aashni(q):
#Aashni’s Function:
#  Take one input q
#  Send q to Akash’s function
#  Multiply q by Akash’s output
#  Return the result
  output = akash(q) * q
  return output
print("aashni")
print(aashni(5))
print("")


def dion(n):
    #Dion’s Function:
#  Take one input n
#  If n is greater than 10:
#    Send n to Malcolm’s function
#  Otherwise:
#    Send n to Rosa’s function
#  Return the returned value
  if n>10:
    malc = malcolm(n)
    return malc
  else:
    ros = rosa(n)
    return ros
print("dion")
print(dion(9))
print("")



def zhixing(a, b):
    #Zhixing’s Function:
#  Take two inputs, a and b 
#  Send a to Aashni’s function
#  Send b to Rosa’s function
#  Send the two returned values to Elaisa’s function
#  Multiply the returned value by 2
#  Return the result
  aas = aashni(a)
  ros = rosa(b)
  ela = elaisa(aas,ros)
  result = ela * 2
  return result
print("zhixing")
print(zhixing(5,6))