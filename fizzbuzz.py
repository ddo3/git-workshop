#!/usr/bin/env python

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 5 == 0:
            print "buzz"
        elif i % 7 == 0:
            print "bizz"
        elif i % 10 == 0:
            print "duh"
        elif i % 2 == 0:
            print "i added this after a branch!"
        else:
            print i
