# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Get user input.  It should be in the format x + y or x - y
operators = "+-x/%"
equation = input("Input your equation in the format x +/- y: ")
equation = equation.split(" ")
while not equation[0].isnumeric() or equation[1] not in operators or not equation[2].isnumeric():
    equation = input("Please make sure to input a valid equaltion: x =/- y: " )
    equation = equation.split(" ")

#Get the max length
longestOperand = max(len(equation[0]), len(equation[2])) + 2
#top line
#add spaces to equal max length + 2
topOperand = ""
for i in range(longestOperand - len(equation[0])):
    topOperand += " "
topOperand += equation[0]
print(topOperand)
#print bottom operand
bottomOperand = "+ "
for i in range(longestOperand - len(equation[2]) - 2):
    bottomOperand += " "
bottomOperand += equation[2]
print(bottomOperand)
equalsLine = ""
for i in range(longestOperand):
    equalsLine += "_"
print(equalsLine)
answer = 0
if equation[1] == "+":
    answer = int(equation[0]) + int(equation[2])
elif equation[1] == "-":
    answer = int(equation[0]) - int(equation[2])
answer = str(answer)
answerSpaces = ""
for i in range(longestOperand - len(answer)):
    answerSpaces += " "
answer = answerSpaces + answer
print(answer)