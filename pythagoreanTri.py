#!/usr/bin/python
# Program to validate if the user has entered a pythogorean triplet

import sys

def getInput():
# Function to get the input values of the triangle sides

	_input = []
	if len(sys.argv) == 4:
		_input.extend(sys.argv[1:4])
		return _input

	_input = raw_input("Enter the sides of the pythagoras triangle seperated by ','\n")
	_input = _input.split(',')

	return _input

def wantToContinue():
# Function to get the input values of the triangle sides
	_input = raw_input("Do you want to continue?\n")
	print ""
	if _input == 'Y' or _input == 'y' or _input == 'yes' or _input == 'Yes':
		return True

	return False

while True:
	aPlusB = 0
	_sides = getInput()

	c = pow(int(max(_sides)),2)

	for i in _sides:
		if i == max(_sides):
			continue
		aPlusB += pow(int(i),2)

	if c == aPlusB:
		print "The triplet ",_sides," is pythogorean\n"
	else:
		print "The triplet ",_sides," is not pythogorean\n"
	if not wantToContinue():
		break
