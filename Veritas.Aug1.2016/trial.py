from __future__ import division
import numpy as np
import sklearn

a = 1
b = 2
print a+b

import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1, matrix2)

print product

sess = tf.Session()
result = sess.run(product)
print(result)

sess.close()

def compress_string(string):
    if string is None or len(string) == 0:
        return string
    result = ''
    prev_char = string[0]
    count = 0
    for char in string:
        if char == prev_char:
            count += 1
        else:
            result += prev_char + (str(count) if count > 1 else '')
            prev_char = char
            count = 1
    result += prev_char + (str(count) if count > 1 else '')
    return result if len(result) < len(string) else string

print compress_string("aaabbc")

a = [[] for _ in range(4)]
print a

print 1/2
print 1//2

def reverse_string(chars):
    if chars is None:
        return None
    size = len(chars)
    for i in range(size//2):
        chars[i], chars[size-1-i] = \
            chars[size-1-i], chars[i]
    return chars

a = list("hello")
print a
print reverse_string(a)


def is_substring(s1, s2):
    return s1 in s2

print is_substring('ab','abc')
