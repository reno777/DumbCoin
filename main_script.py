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

#The following block is where any modules are imported to be used in the script
import time
import sys
sys.path.insert(0, '/home/reno/git/DumbCoin/Files')
from step1 import main1
from step2 import main2
from step3 import main3
from step4 import main4
from step5 import main5

#Functions
def input_loop() :
    i = -1
    while i != 0 :
        print "[1] - Generate your 3 money orders."
        print "[2] - Blind your money orders."
        print "[3] - Bank unblinds a money orders and signs them."
        print "[4] - Give your signed money orders to a merchant."
        print "[5] - Merchant verifies and deposits your money order."
        print "[0] - Exit the program."
        print " "

        user_input = input("[*] - Please select an option from above: ")

        if user_input == 1 :
            main1()
        elif user_input == 2 :
            main2()
        elif user_input == 3 :
            main3()
        elif user_input == 4 :
            main4()
        elif user_input == 5 :
            main5()
        elif user_input == 0 :
            exit()
        else :
            print " "
            print "Your selection is invlaid! Please select an option from above!"
            print " "
            time.sleep(3)

#Main Function. Calls the other functions as needed. 
if __name__ == "__main__" :
    input_loop()
