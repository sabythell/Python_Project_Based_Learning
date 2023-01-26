#Your first task is to code the Fibonacci sequence without a helper method. That is, to be specific, 
#you should write fib(n) so that it calls itself, and all function calls send only one argument.

#def fib(n):
#    if n <= 1:
#        return n
#    else:
#        return fib(n-1) + fib(n-2)

#print(fib(6))

#def fib_helper(n, prev, cur):
#    if n == 0:
#        return cur
#    else:
#        return fib_helper(n-1, cur, cur + prev)

#def fib(n):
#    return fib_helper(n, 0, 1)

#print(fib(6))

#You now have several functions for finding the nth Fibonacci number. Now, modify one of those
#  functions to write a function is_fib(n) that takes in any positive integer and checks if it is in the Fibonacci sequence.
global mylist
mylist = [0]
global fibcount
fibcount = 0


def fib_helper(n, prev, cur):
    global fibcount
    global mylist
    fibcount = fibcount + 1
    if n == 0:
        fibcount -= 1
        mylist.append(cur)
        print(mylist)
        if fibcount in mylist:
            return str(fibcount) + " is in the Fibonacci sequence."
        if fibcount not in mylist:
            return str(fibcount) + " is not in the Fibonacci sequence."
        else:
            return fibcount
    else:
        mylist.append(cur)
        helper = fib_helper(n-1, cur, cur + prev)
        return helper

def is_fib(n):
    return fib_helper(n, 0, 1)

print(is_fib(6))

