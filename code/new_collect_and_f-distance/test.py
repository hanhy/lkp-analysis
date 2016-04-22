#coding=utf-8
#create time : 2016-04-11
#commit time : 2016-04-11
#author : Huiyang.Han

import os
import sys
import json
import csv

FULLFILL = "x"
BINDEX = 1
KINDEX = 5
CINDEX = 6

if __name__ == "__main__":
	ebizzy = []
	for line in open("newpaths.txt"):
		if not cmp("ebizzy", line.split("/")[1]):
			ebizzy.append(line)
	output = open('ebizzypaths.txt', 'w')
	s = ""
	for path in ebizzy:
		s += path
	output.write(s)
	output.close()
