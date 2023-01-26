#Write a recursive function sum_n that will add together the first n positive integers greater than 0.#

#def sum_n(n):
#  if n == 0:
#    return 0
#  else:
#    return n + sum_n(n - 1)
#print(sum_n(5))

#Your goal now is to write a recursive function to add together consecutive perfect squares.#
#def sum_squares(n):
#  if n == 0:
#    return 0
#  else:
#    return n**2 + sum_squares(n-1)
#print(sum_squares(5))

#Now, your goal is to write a function sum_even(n) that will
# take any integer n, and add together all the even numbers greater than 0 and less than or equal to n. 

#def sum_even(n):
#    if n == 0:
#        return 0
#    else:
#        if n % 2 == 0:
#            return n + sum_even(n-2)
#        else:
#            if n % 2 == 1:
#                return sum_even(n-1)
#print(sum_even(10))

#Your goal is to write a recursive function that figures out how many 3s could fit inside a number
#count_threes(11)
#1 + count_threes(8)
#1 + 1 + count_threes(5)
#1 + 1 + 1 + count_threes(2)
#1 + 1 + 1 + 0
#1 + 1 + 1
#1 + 2
#3

#def count_threes(n):
#    x = 0
#    if n < 3:
#        return 0
#    else:
#        return (x+1) + count_threes(n-3)
#print("No. of times the number 3 occurs: " + str(count_threes(3)))

#Your goal is to write a function sum_m_to_n(m, n) to sum the integers between n and m, including n and m. For example:

#sum_m_to_n(0, 5) should return 0 + 1 + 2 + 3 + 4 + 5 = 15
#sum_m_to_n(3, 5) should return 3 + 4 + 5 = 12

#def sum_m_to_n(m,n):
#    if n == m:
#        return n
#    else:
#        return n + sum_m_to_n(m,n-1)
#print(sum_m_to_n(3,5))