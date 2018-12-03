#!/usr/bin/python2.7

"""
### AUTHORS: Seth Rasmussen, Megan Orlando, and Sarah Thorp
### DATE: November 2018 - December 2018
### VERSION: v1.0
### LICENSE: GNU-GPL v3.0
### DESCRIPTION: This program was made for COSC 274: Intro to Applied Cryptography, project 3.
### This program is used to demonstrate the use of protocol number 4, described in
### [SCHN96], p.142 to implement an electronic cash system.
"""

import random
import pickle

def generate() :
    amount = input("[*] - Please enter the amount of money for the money order: ")
    identity = input("[*] - Please enter your ID: ")

    k1 = random.randrange(1,1000)
    k2 = random.randrange(1,1000)
    num1_1 = random.randrange(1,1000)
    num1_2 = random.randrange(1,1000)
    num2_1 = random.randrange(1,1000)
    num2_2 = random.randrange(1,1000)
    num3_1 = random.randrange(1,1000)
    num3_2 = random.randrange(1,1000)
    num1_1_1 = random.randrange(1,1000)
    sec1_1_1 = random.randrange(1,1000)
    num1_1_2 = random.randrange(1,1000)
    sec1_1_2 = random.randrange(1,1000)
    num1_2_1 = random.randrange(1,1000)
    sec1_2_1 = random.randrange(1,1000)
    num1_2_2 = random.randrange(1,1000)
    sec1_2_2 = random.randrange(1,1000)
    num2_1_1 = random.randrange(1,1000)
    sec2_1_1 = random.randrange(1,1000)
    num2_1_2 = random.randrange(1,1000)
    sec2_1_2 = random.randrange(1,1000)
    num2_2_1 = random.randrange(1,1000)
    sec2_2_1 = random.randrange(1,1000)
    num2_2_2 = random.randrange(1,1000)
    sec2_2_2 = random.randrange(1,1000)
    num3_1_1 = random.randrange(1,1000)
    sec3_1_1 = random.randrange(1,1000)
    num3_1_2 = random.randrange(1,1000)
    sec3_1_2 = random.randrange(1,1000)
    num3_2_1 = random.randrange(1,1000)
    sec3_2_1 = random.randrange(1,1000)
    num3_2_2 = random.randrange(1,1000)
    sec3_2_2 = random.randrange(1,1000)

    #split numbers from above
    sec1_1 = num1_1^identity
    sec1_2 = num1_2^identity
    sec2_1 = num2_1^identity
    sec2_2 = num2_2^identity
    sec3_1 = num3_1^identity
    sec3_2 = num3_2^identity

    print " "
    print "[*] - Splitting finished:",sec1_1,sec1_2,sec2_1,sec2_2,sec3_1,sec3_2
    print " "

    #bits and stuffs
    i1_1l = [(num1_1^num1_1_1^num1_1_2),num1_1_1]
    i1_1r = [(sec1_1^sec1_1_1^sec1_1_2),sec1_1_1]
    i1_2l = [(num1_2^num1_2_1^num1_2_2),num1_2_1]
    i1_2r = [(sec1_2^sec1_2_1^sec1_2_2),sec1_2_1]
    i2_1l = [(num2_1^num2_1_1^num2_1_2),num2_1_1]
    i2_1r = [(sec2_1^sec2_1_1^sec2_1_2),sec2_1_1]
    i2_2l = [(num2_2^num2_2_1^num2_2_2),num2_2_1]
    i2_2r = [(sec2_2^sec2_2_1^sec2_2_2),sec2_2_1]
    i3_1l = [(num3_1^num3_1_1^num3_1_2),num3_1_1]
    i3_1r = [(sec3_1^sec3_1_1^sec3_1_2),sec3_1_1]
    i3_2l = [(num3_2^num3_2_1^num3_2_2),num3_2_1]
    i3_2r = [(sec3_2^sec3_2_1^sec3_2_2),sec3_2_1]

    i1_1 = i1_1l + i1_1r
    i1_2 = i1_2l + i1_2r
    i2_1 = i2_1l + i2_1r
    i2_2 = i2_2l + i2_2r
    i3_1 = i3_1l + i3_1r
    i3_2 = i3_2l + i3_2r

    print " "
    print "[*] - Finished bit commitment."
    print i1_1l,i1_1r,i1_2l,i1_2r,i2_1l,i2_1r,i2_2l,i2_2r,i3_1l,i3_1r,i3_2l,i3_2r,i3_2r
    print " "

    #first money order
    #generates a large number for uniqe identifier
    unique = [random.randrange(10000,1000000)]

    money_order1 = [amount]
    money_order1 += unique
    money_order1 += i1_1
    money_order1 += i1_2
    
    with open('output/money_order1_output.txt', 'wb') as f :
        pickle.dump(money_order1, f)

    #second money order
    #generates a large number for uniqe identifier
    unique = [random.randrange(10000,1000000)]

    money_order2 = [amount]
    money_order2 += unique
    money_order2 += i2_1
    money_order2 += i2_2

    with open('output/money_order2_output.txt', 'wb') as f :
        pickle.dump(money_order2, f)

    #third money order
    #generates a large number for uniqe identifier
    unique = [random.randrange(10000,1000000)]

    money_order3 = [amount]
    money_order3 += unique
    money_order3 += i3_1
    money_order3 += i3_2

    with open('output/money_order3_output.txt', 'wb') as f :
        pickle.dump(money_order3, f)

    with open('output/k_variables.txt', 'wb') as f:
        print >> f, k1
        print >> f, k2

    print " "
    print "[*] - Your money order has been generated!"
    print " "

def main1() :
    generate()

if __name__ == "__main__" :
    main1()


