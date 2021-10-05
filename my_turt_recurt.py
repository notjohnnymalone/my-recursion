###################################
#--My Own Recursion
#--Reid A. Martin
###################################

import turtle

##-----Functions-----##

def zigzag(branchLen, turt):
    if branchLen > 1: #exit case; when no longer true program will shut down
        turt.forward(branchLen) #moving turt forward the length of the branch
        turt.right(90)#turning turt right 90deg
        turt.forward(branchLen)#moving turt forward branch length
        turt.left(90)#turt turns left 90 deg
        zigzag(branchLen-10, turt) #calls again but takes 10 off the branch length
        
def stuff():
    turt = turtle.Turtle() 
    myWin = turtle.Screen() 
    turt.speed(100)      #moving
    turt.backward(450)   #turt
    turt.clear()         #in
    turt.speed(20)       #to
    turt.color("green")  #his
    turt.left(45)        #position
    zigzag(109, turt)    # :)
    myWin.exitonclick()
 
##--Main Code--##
stuff()