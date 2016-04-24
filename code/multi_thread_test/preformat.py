#coding=utf-8
#create time : 2016-04-24
#commit time : 2016-04-24
#author : Huiyang.Han

import os
import sys

aim7 = []
ebizzy = []

for i in open("newpathsbackup.txt"):
	print i
	if not cmp(i.split("/")[1], "aim7"):
		aim7.append("i")
	if not cmp(i.split("/")[1], "ebizzy"):
		ebizzy.append("i")

aim7out = open("aim7_path.txt", "w")
s = ""
for path in aim7:
	s += path
aim7out.write(s)
aim7out.close()

ebizzyout = open("ebizzy_path.txt", "w")
s = ""
for path in ebizzy:
	s += path
ebizzyout.write(s)
ebizzyout.close()
