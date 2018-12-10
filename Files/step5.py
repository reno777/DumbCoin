#!/usr/bin/python2.7

"""
### AUTHORS: Seth Rasmussen, Megan Orlando, and Sarah Thorp
### DATE: November 2018 - December 2018
### VERSION: v1.0
### LICENSE: GNU-GPL v3.0
### DESCRIPTION: This program was made for COSC 274: Intro to AppliedCryptography, project 3.
### This program is used to demonstrate the use of protocol number 4, described in
### [SCHN96], p.142 to implement an electronic cash system.
### CREDIT: The perl script used in this program was found on github and can be
### found at https://github.com/bsquille/Digital_Cash/blob/master/Files/LargeNumberCalc.pl
"""

import pickle

def bank() :
    with open('Files/output/opened_money_order.txt','rb') as f :
        opened_money_order = pickle.load(f)

    with open('Files/output/spent.txt','rb') as f :
        spent = f.readline()
        f.close()

    if spent != opened_money_order[1] :
        with open('Files/output/spent.txt','wb') as f :
            print >> f, opened_money_order[1]
            f.close()
        print " "
        print "[!] - Your money has been deposited!"
        print " "
    elif spent == opened_money_order[1] :
        print " "
        print "[!!!] - This order has already been used!"
        print " "
    else :
        print " "
        print "[!!!] - ERROR!"
        print " "

def main5() :
    bank()

if __name__ == "__main__" :
    main5()
