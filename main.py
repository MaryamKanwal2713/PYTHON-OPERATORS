#  ******************** ARITHMETIC OPERATORS ******************** 

# ============== 1-ADDITION (+) ============== 
x = 2
y = 3
print(x + y)  # Output: 5

# ============== 2-SUBTRACTION (-) ============== 
x = 5
y = 2
print(x - y)  # Output: 3

# ============== 3-MULTIPLICATION (*) ==============
x = 5
y = 3
print(x * y)  # Output: 15

# ============== 4-DIVISION (/) ==============
x = 15
y = 3
print(x / y)  # Output: 5.0

# ============== 5-Modulus (%) ============== 
x = 9
y = 4
print(x % y)  # Output: 1

# ============== 6-Exponentiation (**) ==============
x = 3
y = 4
print(x ** y)  # Output: 81

# ============== 7-Floor Division (//) ==============
x = 15
y = 3
print(x // y)  # Output: 5

# ******************** ASSIGNMENT OPERATORS ********************

# ============== 1-Assignment (=) ==============
x = 5
print(x)  # Output: 5

# ============== 2-Additional Assignment (+=) ==============
x = 5
print(x)  # Output: 5
x += 3
print(x)  # Output: 8

# ============== 3-Subtraction  Assignment (-=) ==============
x = 8
print(x)  # Output: 8
x -= 3
print(x)  # Output: 5

# ============== 4-Multiplication Assignment (*=) ============== 
x = 5
print(x)  # Output: 5
x *= 3
print(x)  # Output: 15

# ============== 5-Division Assignment (/=) ==============
x = 10
print(x)  # Output: 10
x /= 3
print(x)  # Output: 3.3333333333333335

#  ============== 6- Floor Division Assignment (//=) ==============
x = 10
print(x)  # Output: 10
x //= 3
print(x)  # Output: 3

# ============== 7-Exponentiation Assignment (**=) ==============
x = 2
x **= 3  # equivalent to x = x ** 3
print(x)  # Output: 8

# ============== 8-Bitwise AND Assignment (&=) ==============
x = 5   # binary: 101
x &= 3  # binary: 011
print(x)  # Output: 1 (binary: 001)

# ============== 9-Bitwise XOR Assignment(^=) ==============
x = 5   # binary: 101
x ^= 3  # binary: 011
print(x)  # Output: 6 (binary: 110)

# ============== 10-Right shift Assignment (>>=) ==============
x = 16  # binary: 10000
x >>= 2  # binary: 01000
print(x)  # Output: 4

# ============== 11-Left shift Assignment (<<=) ==============
x = 4   # binary: 0100
x <<= 2  # binary: 1000
print(x)  # Output: 16

#  ******************** COMPARISION OPERATOR ********************

# ============== 1-Equal to (==) ==============
x = 5
print(x == 5)  # Output: True
print(x == 3)  # Output: False

# ============== 2-Not Equal to (!=) ==============
x = 5
print(x != 5)  # Output: False
print(x != 3)  # Output: True

# ============== 3-Greater than (>) ==============
x = 15
print(x > 3)  # Output: True
print(x > 20)  # Output: False

# ============== 4-Less than (<) ==============
x = 7
print(x < 4)  # Output: False
print(x < 9)  # Output: True

# ============== 5-Greater than or equal to (>=) ==============
x = 12
print(x >= 10)  # Output: True
print(x >= 15)  # Output: False

# ============== 6-Less than or equal to (<=) ==============
x = 6
print(x <= 10)  # Output: True
print(x <= 2)  # Output: False

# ******************** LOGICAL OPERATOR ********************

# ============== 1-AND (and) ==============
x = 9
print(x > 3 and x < 10)  # Output: True
print(x > 10 and x < 5)  # Output: False

# ============== 2-OR (or) ==============
x = 5
print(x > 3 or x < 10)  # Output: True
print(x > 10 or x < 5)  # Output: False

# ============== 3-NOT (not) ==============
x = 15
print(not x > 3)  # Output: False
print(not x < 10)  # Output: True

# ******************** IDENTITY OPERATOR ********************

# ============== 1-Is (is) ==============
x = 10
print(x is 10)  # Output: True
print(x is 3)  # Output: False

# ============== 2-Is not (is not) ==============
x = 9
print(x is not 9)  # Output: False
print(x is not 3)  # Output: True

# ******************** MEMBERSHIP OPERATOR ********************

# ============== 1-In (in) ==============
x = [1, 2, 3, 4, 5]
print(2 in x)  # Output: True
print(6 in x)  # Output: False

# ============== 2-Not in (not in) ==============
x = [1, 2, 3, 4, 5]
print(2 not in x)  # Output: False
print(6 not in x)  # Output: True

# ******************** BITWISE OPERATOR ********************

# ============== 1-AND (&) ==============
x = 5
y = 3
print(x & y)  # Output: 1
# ============== 2-OR (|) ==============
x = 5
y = 3
print(x | y)  # Output: 7

# ============== 3-XOR (^) ==============
x = 5
y = 3
print(x ^ y)  # Output: 6

# ============== 4-NOT (~) ==============
x = 5
print(~x)  # Output: -6

# ============== 5-Left Shift (<<) ==============
x = 5
print(x << 2)  # Output: 20

# ============== 6-Right Shift (>>) ==============
x = 20
print(x >> 2)  # Output: 5
