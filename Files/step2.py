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

def blind() :

    #bank vars
    e = 29
    n = 571
    d = 59

    with open('Files/output/k_variables.txt','rb') as f :
        k_values = pickle.load(f)

    #first money order.
    with open('Files/output/money_order1_output.txt','rb') as f :
        money_order1 = pickle.load(f)

    print " "
    print "[!] - Money Order 1"
    print "[*] - Amount:",money_order1[0]
    print "[*] - Uniqueness Number:",money_order1[1]
    print "[*] - I11:",money_order1[2],money_order1[3],money_order1[4],money_order1[5]
    print "[*] - I12:",money_order1[6],money_order1[7],money_order1[8],money_order1[9]
    print " "

    blind_money_order1 = []
    i = 0
    while i < len(money_order1) :
        blind_money_order1.append((money_order1[i] * (k_values[0] ** e)) % n)
        i += 1

    print " "
    print "[!] - Blinded Money Order 1"
    print "[*] - Amount:",blind_money_order1[0]
    print "[*] - Uniqueness Number:",blind_money_order1[1]
    print "[*] - I11:",blind_money_order1[2],blind_money_order1[3],blind_money_order1[4],blind_money_order1[5]
    print "[*] - I12:",blind_money_order1[6],blind_money_order1[7],blind_money_order1[8],blind_money_order1[9]
    print " "

    with open('Files/output/blind_money_order1.txt','wb') as f :
        pickle.dump(blind_money_order1, f)

    #second money order
    with open('Files/output/money_order2_output.txt','rb') as f :
        money_order2 = pickle.load(f)
    
    print " "
    print "[!] - Money Order 2"
    print "[*] - Amount:",money_order2[0]
    print "[*] - Uniqueness Number:",money_order2[1]
    print "[*] - I21:",money_order2[2],money_order2[3],money_order2[4],money_order2[5]
    print "[*] - I22:",money_order2[6],money_order2[7],money_order2[8],money_order2[9]
    print " "
    
    blind_money_order2 = []
    i = 0
    while i < len(money_order2) :
        blind_money_order2.append((money_order2[i] * (k_values[1] ** e)) % n)
        i += 1
    
    print " "
    print "[!] - Blinded Money Order 2"
    print "[*] - Amount:",blind_money_order2[0]
    print "[*] - Uniqueness Number:",blind_money_order2[1]
    print "[*] - I21:",blind_money_order2[2],blind_money_order2[3],blind_money_order2[4],blind_money_order2[5]
    print "[*] - I22:",blind_money_order2[6],blind_money_order2[7],blind_money_order2[8],blind_money_order2[9]
    print " "
    
    with open('Files/output/blind_money_order2.txt','wb') as f :
        pickle.dump(blind_money_order2, f)

    #third money order
    with open('Files/output/money_order3_output.txt','rb') as f :
        money_order3 = pickle.load(f)
    
    print " "
    print "[!] - Money Order 3"
    print "[*] - Amount:",money_order3[0]
    print "[*] - Uniqueness Number:",money_order3[1]
    print "[*] - I31:",money_order3[2],money_order3[3],money_order3[4],money_order3[5]
    print "[*] - I32:",money_order3[6],money_order3[7],money_order3[8],money_order3[9]
    print " "
    
    blind_money_order3 = []
    i = 0
    while i < len(money_order3) :
        blind_money_order3.append((money_order3[i] * (k_values[2] ** e)) % n)
        i += 1
    
    print " "
    print "[!] - Blinded Money Order 3"
    print "[*] - Amount:",blind_money_order3[0]
    print "[*] - Uniqueness Number:",blind_money_order3[1]
    print "[*] - I31:",blind_money_order3[2],blind_money_order3[3],blind_money_order3[4],blind_money_order3[5]
    print "[*] - I32:",blind_money_order3[6],blind_money_order3[7],blind_money_order3[8],blind_money_order3[9]
    print " "
    
    with open('Files/output/blind_money_order3.txt','wb') as f :
        pickle.dump(blind_money_order3, f)

    print " "
    print "[!!] - Money orders have been blinded!"
    print " "

def main2() :
    blind()

if __name__ == "__main__" :
    main2()
