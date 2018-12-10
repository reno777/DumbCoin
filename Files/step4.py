#!/usr/bin/python2.7

"""
### AUTHORS: Seth Rasmussen, Megan Orlando, and Sarah Thorp
### DATE: November 2018 - December 2018
### VERSION: v1.0
### LICENSE: GNU-GPL v3.0
### DESCRIPTION: This program was made for COSC 274: Intro to AppliedCryptography, project 3.
### This program is used to demonstrate the use of protocol number 4, described in
### [SCHN96], p.142 to implement an electronic cash system.
"""

import pickle
import random
from subprocess import call

def unblind() :
    #bank vars 
    e = 29
    n = 571
    d = 59

    with open('Files/output/signed_money_order.txt','rb') as f :
        signed_money_order = pickle.load(f)

    k = signed_money_order[0]

    print " "
    print "[!!] - You unblind the money order!"
    print " "

    with open('Files/perl_input.txt','w') as f :
        print >> f, k
        print >> f, "-1"
        print >> f, n
        f.close()

    call(["perl","Files/LargeNumberCalc.pl"])

    with open('Files/perl_output.txt','rb') as f :
        invt = f.readline()
        f.close()

    with open('Files/perl_input.txt','w') as f :
        print >> f, invt
        print >> f, e
        print >> f, n
        f.close()

    call(["perl","Files/LargeNumberCalc.pl"])

    with open('Files/perl_output.txt','rb') as f :
        unblinding_factor = f.readline()
        f.close()
        
    money_order_signature1 = []    
    i = 1
    while i < 11 :
        money_order_signature1.append((int(signed_money_order[i]) * int(unblinding_factor)) % n)
        i += 1

    money_order_signature2 = []
    i = 11
    while i < 21 :
        money_order_signature2.append((int(signed_money_order[i]) * int(invt)) % n)
        i += 1

    money_order_signature = []
    money_order_signature += money_order_signature1
    money_order_signature += money_order_signature2

    print " "
    print "[!] - Unblinded Money Order"
    print "[*] - Amount:",money_order_signature[0]
    print "[*] - Uniqueness Number:",money_order_signature[1]
    print "[*] - I11:",money_order_signature[2],money_order_signature[3],money_order_signature[4],money_order_signature[5]
    print "[*] - I12:",money_order_signature[6],money_order_signature[7],money_order_signature[8],money_order_signature[9]
    print "[*] - Signature:",''.join(map(str,money_order_signature[10:]))
    print " "

    print " "
    print "[!!] - The merchant is unblinding the signature"
    print " "

    test_signature = []
    i = 10
    while i < 20 :
        with open('Files/perl_input.txt','w') as f :
            print >> f, money_order_signature[i]
            print >> f, e
            print >> f, n
            f.close()
        call(["perl","Files/LargeNumberCalc.pl"])
        with open('Files/perl_output.txt','rb') as f :
            temp = (f.readline())
            f.close()
        test_signature.append(temp)
        i += 1

    i = 0
    while i < 10 :
        print money_order_signature[i],"=",test_signature[i]
        if int(money_order_signature[i]) == int(test_signature[i]) :
            print "VERIFIED!"
            print " "
        else :
            print "FAILED!"
            print " "
        i +=1
        
    var1 = random.randrange(1,3)
    var2 = random.randrange(1,3)

    if var1 == 1 :
        id1 = money_order_signature[2:4]
    elif var1 == 2 :
        id1 = money_order_signature[4:6]
    else :
        print " "
        print "[!!!] - ERROR!"
        print " "

    if var2 == 1 :
        id2 = money_order_signature[6:8]
    elif var2 == 2 :
        id2 = money_order_signature[8:10]
    else :
        print " "
        print "[!!!] - ERROR!"
        print " "

    opened_money_order = []
    opened_money_order += money_order_signature[0:2]
    opened_money_order += id1
    opened_money_order += id2

    with open('Files/output/opened_money_order.txt','wb') as f :
        pickle.dump(opened_money_order, f)

def main4() :
    unblind()

if __name__ == "__main__" :
    main4()
