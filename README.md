# DumbCoin
Project 3 in COSC 274. Proof of concept for a cryptocurrency.

This project was made by Seth Rasmussen, Megan Orlando, and Sarah Thorp for COSC 274. 
This project This program was made for COSC 274: Intro to AppliedCryptography, project 3.
This program is used to demonstrate the use of protocol number 4, described in
[SCHN96], p.142 to implement an electronic cash system.
CREDIT: The perl script used in this program was found on github and can be
found at https://github.com/bsquille/Digital_Cash/blob/master/Files/LargeNumberCalc.pl

To use the project it requires perl and python. You must ensure that both are install and up-to-date on your
system. This program uses python 2.7 NOT python 3. In this program there are five portions. The first generates 
3 different money orders for the user. It asks for the user to input the ammount they would like to order, as 
well as their user ID. (In this senario it can be what ever you want as the program isnt checking against any sort 
of database in the backend.) The next portion allows the user to "blind" or encrypt their money orders to remain secret.
Portion three then has the user send their orders to the bank, where the bank randomly selects 2 of the three money orders and 
"unblinds" and signs the remaining anonymous order. The fourth portion of this program then has the user send their signed money order
to a merchant who verifies the users identity and ensure that the order is legitamte. The last portion allows the user 
to see the merchant sending the money order to the bank for deposit, where the bank will also verify that it has not been
used previously. 
