# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python
print("Hello, World!")

# Exercise 2 - Introduction - Python If-Else
import math
import os
import random
import re
import sys

N = int(input().strip())
if N % 2 != 0:
    print ("Weird")
else:
    if N >= 2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    elif N > 20:
        print ("Not Weird")

# Exercise 3 - Introduction - Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a + b)
    print (a - b)
    print (a * b)

# Exercise 4 - Introduction - Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Exercise 5 - Introduction - Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)

# Exercise 6 - Introduction - Write a function
def is_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input())
print(is_leap(year))

# Exercise 7 - Introduction - Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end = '')

# Exercise 8 - Basic data types - List Comprehensions
if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    
    ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
    print (ans)

# Exercise 9 - Basic data types - Find the Runner-Up Score!
if __name__ == '__main__':
    N = int(input())
    O = input().split(' ')
    P = list(map(int, O))
    Q = set(P)
    R = sorted(list(Q))
    print (R[-2])

# Exercise 10 - Basic data types - Nested Lists
if __name__ == '__main__':
    N = int(input())
    
    students = []
    for i in range(2*N):
        students.append(input().split())
    grades = {}
    for j in range(0, len(students), 2):
        grades[students[j][0]] = float(students[j + 1][0])
    result = []
    num_to_match = sorted(set(grades.values()))[1]
    for pupil in grades.keys():
        if grades[pupil] == num_to_match:
            result.append(pupil)
    for k in sorted(result):
        print (k)

# Exercise 11 - Basic data types - Finding the percentage
if __name__ == '__main__':
    N = int(input())
    results = {}
    for i in range(N):
        a = input().split(' ')
        results[a[0]] = [float(x) for x in a[1:]]
    student = input()
    print ("%.2f" %(sum(results[student])/len(results[student])))

# Exercise 12 - Basic data types - Lists
if __name__ == '__main__':
    list = []
    n = int(input())
    for i in range(n):
        a = input().split()
        if len(a) == 3:
            eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
        elif len(a) == 2:
            eval("list." + a[0] + "(" + a[1] + ")")
        elif a[0] == "print":
            print (list)
        else:
            eval("list." + a[0] + "()")

# Exercise 13 - Basic data types - Tuples
if __name__ == '__main__':
    tuple_len = int(input())
    a = tuple(map(int, input().split(' ')))
    print (hash(a))

# Exercise 14 - Strings - sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Exercise 15 - Strings - String Split and Join
def split_and_join(line):
    # write your code here
    T = line.split(" ")
    return "-".join(T)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Exercise 16 - Strings - What's Your Name?
def print_full_name(a, b):
    print("Hello " +a +" " +b +"!" +" You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Exercise 17 - Strings - Mutations
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Exercise 18 - Strings - Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)-len(sub_string)+1):
        if sub_string == string[i:i+len(sub_string)]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Exercise 19 - Strings - String Validators
if __name__ == '__main__':
    S = input()
    print(any(c.isalnum() for c in S))
    print(any(c.isalpha() for c in S))
    print(any(c.isdigit() for c in S))
    print(any(c.islower() for c in S))
    print(any(c.isupper() for c in S))

# Exercise 20 - Strings - Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Exercise 21 - Strings - Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Exercise 22 - Strings - Designer Door Mat
N, M = map(int, input().split())
for i in range(1, N, 2):
    print (str('.|.' * i).center(M, '-'))
print ('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print (str('.|.' * i).center(M, '-'))

# Exercise 23 - Strings - String Formatting
def print_formatted(number):
    width = len(bin(n)[2:])
    for i in range(1, n + 1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Exercise 24 - Strings - Alphabet Rangoli
import string
def print_rangoli(size):
    mid = n - 1
    
    for i in range(n - 1, 0, -1):
        row = ['-'] * (2 * n - 1)
        for j in range(n - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))
    
    for i in range(0, n):
        row = ['-'] * (2 * n - 1)
        for j in range(0, n - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Exercise 25 - Strings - Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

# Exercise 26 - Strings - The Minion Game
def minion_game(string):
    n = len(s)
    stuart = 0
    kevin = 0
    
    for i in range(n):
        if s[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i

if kevin > stuart:
    print ('Kevin', kevin)
    elif stuart > kevin:
        print ('Stuart', stuart)
else:
    print ('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Exercise 27 - Strings - Merge the Tools!
def merge_the_tools(string, k):
    for i in range(int(len(string) / k)):
        t = ''
        for c in string[i * k : (i + 1) * k]:
            if c in t:
                continue
            t += c
        print (t)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Exercise 28 - Sets - Introduction to Sets
def average(array):
    setA = set(map(int, array))
    return float(sum(setA))/len(setA)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Exercise 29 - Sets - No Idea!
num = input().split()
num = map(int, num)
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

counter = 0
for i in n:
    if i in A:
        counter += 1
    elif i in B:
        counter -= 1
print (counter)

# Exercise 30 - Sets - Symmetric Difference
M=int(input())
list1=map(int,input().strip().split(" "))
N=int(input())
list2=map(int,input().strip().split(" "))
set1=set(list1)
set2=set(list2)
l1=(set1.difference(set2))
l2=(set2.difference(set1))
l3=sorted(l1.union(l2))
for i in l3:
    print (i)

# Exercise 31 - Sets - Set .add()
N = int(input())
s = set(input() for i in range(N))
print (len(s))

# Exercise 32 - Sets - Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    whatToDo = input().split()
    
    if whatToDo[0] == 'pop':
        s.pop()
    elif whatToDo[0] == 'remove':
        s.remove(int(whatToDo[1]))
    elif whatToDo[0] == 'discard':
        s.discard(int(whatToDo[1]))
    else:
        assert False

print (sum(s))

# Exercise 33 - Sets - Set .union() Operation
n = int(input())
l = input().split()
s = set(map(int, l))
num = int(input())
stud_list = input().split()
stud_set = set(map(int, stud_list))
print (len(s.union(stud_set)))

# Exercise 34 - Sets - Set .intersection() Operation
n = int(input())
l = input().split()
s = set(map(int, l))
num = int(input())
stud_list = input().split()
stud_set = set(map(int, stud_list))
print (len(s.intersection(stud_set)))

# Exercise 35 - Sets - Set .difference() Operation
n = int(input())
s = set(map(int, input().split()))
stud_num = int(input())
stud_set = set(map(int, input().split()))
print (len(s.difference(stud_set)))

# Exercise 36 - Sets - Set .symmetric_difference() Operation
n1=input()
s1=set(input().split(" "))
n2=input()
s2=set(input().split(" "))
s3=s1.union(s2).difference(s1.intersection(s2))
print (len(s3))

# Exercise 37 - Sets - Set Mutations
length = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    (whatToDo, other_set_length) = input().split()
    other_set = set(map(int, input().split()))
    
    if whatToDo == 'intersection_update':
        A.intersection_update(other_set)
    elif whatToDo == 'update':
        A.update(other_set)
    elif whatToDo == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
    elif whatToDo == 'difference_update':
        A.difference_update(other_set)
    else:
        assert False

print (sum(A))

# Exercise 38 - Sets - The Captain's Room
n=int(input())
nums=map(int,input().split(" "))
nums=sorted(nums)
for i in range(1,len(nums)):
    if i!=len(nums)-1:
        if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
            print (nums[i])
            break
    else:
        print (nums[i])

# Exercise 39 - Sets - Check Subset
for i in range(int(input())):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    if B.intersection(A)==A:
        print("True")
    else:
        print("False")

# Exercise 40 - Sets - Check Strict Superset
A = set(map(int, input().split()))
N = int(input())

is_strict_superset = True
for i in range(N):
    s = set(map(int, input().split()))
    if not s.issubset(A):
        is_strict_superset = False
    if len(s) >= len(A):
        is_strict_superset = False

print (is_strict_superset)
