#coding=utf-8
#create time : 2016-04-12
#commit time : 2016-04-12
#author : Huiyang.Han

import os
import sys
import csv
import random
import datetime

BINDEX = 1
KINDEX = 5
CINDEX = 6

def read(filename):
	l = []
	for line in open(filename):
		if not cmp("benchmarks.txt", filename):
			print line
		l.append(line)
	return l

def genkc(filename):
	kernel = []
	compiler = []

	for line in open(filename):
		pathsplit = line.split("/")
		kernel.append(pathsplit[KINDEX])
		compiler.append(pathsplit[CINDEX])
	kernel = set(kernel)
	compiler = set(compiler)

	output = open('kernels.txt', 'w')
	s = ""
	for k in kernel:
		s += (k + "\n")
	output.write(s)
	output.close()

	output = open('compilers.txt', 'w')
	s = ""
	for c in compiler:
		s += (c + "\n")
	output.write(s)
	output.close()


if __name__ == "__main__":
	genkc("newpaths.txt")

	metrics = read("metrics.txt")
	benchmarks = read("benchmarks.txt")
	kernels = read("kernels.txt")
	compilers = read("compilers.txt")

	mlen = len(metrics)
	blen = len(benchmarks)
	klen = len(kernels)
	clen = len(compilers)

	cols = mlen + 3
	rows = 1 + blen * klen * clen

	wcsvfile = file('washeddata.csv', 'wb')
	writer = csv.writer(wcsvfile)
	line = [0] * cols

	line[0] = "benchmark"
	line[1] = "kernel"
	line[2] = "compiler"
	for i in range(3, cols):
		line[i] = metrics[i - 3]
	writer.writerow(line)

	n = 0

	for b in range(blen):
		line[0] = benchmarks[b]
		for k in range(klen):
			line[1] = kernels[k]
			for c in range(clen):
				n += 1
				line[2] = compilers[c]
				for i in range(3, cols):
					time = datetime.datetime.now()
					random.seed(n + i)
					line[i] = random.random()
				writer.writerow(line)
