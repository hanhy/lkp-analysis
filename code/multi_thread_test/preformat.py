#coding=utf-8
#create time : 2016-04-24
#commit time : 2016-04-24
#author : Huiyang.Han

import os
import sys

bl = {}#benchmark to a list
for i in open("benchmarks.txt"):
	bl[i[0:len(i) - 1]] = []

for i in open("newpathsbackup.txt"):
	print i
	bl[i.split("/")[1]].append(i)

for k, v in bl.items():
	print k
	out = open("path/" + k + ".txt", "w")
	s = ""
	for path in v:
		s += path
	out.write(s)
	out.close()