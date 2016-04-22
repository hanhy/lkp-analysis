#coding=utf-8
#create time : 2016-04-11
#commit time : 2016-04-11
#author : Huiyang.Han

import os
import sys

def read_paths(path_file):
	paths = []
	for path in open(path_file):
		print path
		length = len(path)
		if  length > 7:
			paths.append(path[1:length - 3] + "matrix.json\n")
		else:
			continue
	return paths

if __name__ == "__main__":
	paths = read_paths("paths.txt")
	output = open('newpaths.txt', 'w')
	s = ""
	for path in paths:
		s += path
	output.write(s)
	output.close()