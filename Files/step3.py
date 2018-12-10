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
from subprocess import call

def unblind() :
    #bank vars
    e = 29
    n = 571
    d = 59

    with open('Files/output/k_variables.txt','rb') as f :
        k_values = pickle.load(f)

    blindmo1(e, n, k_values[0])

def large_num(e, n, k_value) :
    with open('Files/perl_input.txt','w') as f :
        print >> f, k_value
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

    return unblinding_factor

def blindmo1(e, n, k1) :
    #testing unblind for moneyorder1
    with open('Files/output/blind_money_order1.txt','rb') as f :
        blind_money_order1 = pickle.load(f)

    print " "
    print "[!] - Blinded Money Order 1"
    print "[*] - Amount:",blind_money_order1[0]
    print "[*] - Uniqueness Number:",blind_money_order1[1]
    print "[*] - I11:",blind_money_order1[2],blind_money_order1[3],blind_money_order1[4],blind_money_order1[5]
    print "[*] - I12:",blind_money_order1[6],blind_money_order1[7],blind_money_order1[8],blind_money_order1[9]
    print " "

    unblinding_factor = large_num(e, n, k1)

    unblind_money_order1 = []
    i = 0
    while i < len(blind_money_order1) :
        unblind_money_order1.append((blind_money_order1[i] * int(unblinding_factor)) % n)
        i += 1

    print " "
    print "[!] - Unblinded Money Order 1"
    print "[*] - Amount:",unblind_money_order1[0]
    print "[*] - Uniqueness Number:",unblind_money_order1[1]
    print "[*} - I11:",unblind_money_order1[2],unblind_money_order1[3],unblind_money_order1[4],unblind_money_order1[5]
    print "[*} - I12:",unblind_money_order1[6],unblind_money_order1[7],unblind_money_order1[8],unblind_money_order1[9]
    print " "

    with open('Files/output/unblind_money_order2.txt','wb') as f :
        pickle.dump(unblind_money_order1, f)

def main3() :
    unblind()

if __name__ == "__main__" :
    main3()
