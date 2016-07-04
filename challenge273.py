#!/usr/bin/python

# Challenge #273 [Easy] Getting a degree
# https://www.reddit.com/r/dailyprogrammer/comments/4q35ip/20160627_challenge_273_easy_getting_a_degree/?ref=share&ref_source=link

import sys

args = iter(sys.argv)
next(args)

for arg in args:
	print arg[0:-1], "->",
	if arg[-2:] == "rd":
		output = str(float(arg[0:-2]) / 3.1416 * 180) + 'd'
	elif arg[-2:] == "dr":
		output = str(float(arg[0:-2]) / 180 * 3.1416) + 'r'
	elif arg[-2:] == "cf":
		output = str(float(arg[0:-2]) * 9 / 5 + 32) + 'f'
	elif arg[-2:] == "ck":
		output = str(float(arg[0:-2]) + 273.15) + 'k'
	elif arg[-2:] == "fc":
		output = str((float(arg[0:-2]) - 32) * 5 / 9) + 'c'
	elif arg[-2:] == "fk":
		output = str((float(arg[0:-2]) + 459.67) * 5 / 9) + 'k'
	elif arg[-2:] == "kc":
		output = str(float(arg[0:-2]) -273.15) + 'c'
	elif arg[-2:] == "kf":
		output = str(float(arg[0:-2]) * 9 / 5 - 459.67) + 'f'
	else:
		print "No candidate for conversion"
		continue
	print output