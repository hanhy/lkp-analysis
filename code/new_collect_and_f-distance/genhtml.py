#coding=utf-8
#create time : 2016-04-11
#commit time : 2016-04-11
#author : Huiyang.Han

import os
import sys
import csv
from optparse import OptionParser
from json import *

def read_csv(filename):
	#input: a csv file
	#output: a dic metrics->value list
	#function: read and transfer

	csvfile = file(filename, 'rb')
	reader = csv.reader(csvfile)
	
	dic = {}
	keys = []

	for line in reader:
		keys = line
		for metric in line:
			dic[metric] = []
		break
	length = len(dic.keys())

	for line in reader:
		for i in range(length):
			dic[keys[i]].append(line[i])

	return dic

def rmrepeat(l):
	newl = []
	for item in l:
	    if item not in newl:
	        newl.append(item)
	return newl

def rmquotes(jsonstr):
	return jsonstr.replace("\"FLAG", "").replace("FLAG\"", "")	

def genhtml(dic, metric, xAxis, benchmark, kernel, compiler, output):
	#inputL parms
	#output: nothing
	#function: genhtml

	#Obtain series
	series = {}

	benchmarks = dic["benchmark"]
	kernels = dic["kernel"]
	compilers = dic["compiler"]

	length = len(benchmarks)

	values = dic[metric]
	#print values

	if not cmp("benchmark", xAxis):
		for i in range(length):
			if not cmp(kernel, kernels[i]) and not cmp(compiler, compilers[i]):
				series[benchmarks[i]] = float(values[i])
	elif not cmp("kernel", xAxis):
		for i in range(length):
			if not cmp(benchmark, benchmarks[i]) and not cmp(compiler, compilers[i]):
				print kernels[i]
				series[kernels[i]] = float(values[i])
	elif not cmp("compiler", xAxis):
		for i in range(length):
			if not cmp(benchmark, benchmarks[i]) and not cmp(kernel, kernels[i]):
				series[compilers[i]] = float(values[i])

	#generate html file
	head = ""
	tailer = ""

	for line in open("html/head.html"):
		head += line
	for line in open("html/tailer.html"):
		tailer += line

	htmldict = {}
	
	title = {}
	title["FLAGtextFLAG"] = "Metric " + metric + " trend along with the " + xAxis
	title["FLAGxFLAG"] = -20

	strx = xAxis
	xAxis = {}
	if not cmp("benchmark", strx):
		xAxis["FLAGcategoriesFLAG"] = benchmarks
	elif not cmp("kernel", strx):
		xAxis["FLAGcategoriesFLAG"] = kernels
	elif not cmp("compiler", strx):
		xAxis["FLAGcategoriesFLAG"] = compilers

	yAxis = {}
	ytitle = {}
	ytitle["FLAGtextFLAG"] = metric
	yplotLines = {}
	yplotLines["FLAGvalueFLAG"] = 0
	yplotLines["FLAGwidthFLAG"] = 1
	yplotLines["FLAGcolorFLAG"] = '#808080'
	yAxis["FLAGtitleFLAG"] = ytitle
	yAxis["FLAGyplotLinesFLAG"] = yplotLines

	legend = {}
	legend["FLAGlayoutFLAG"] = "vertical"
	legend["FLAGalignFLAG"] = "right"
	legend["FLAGverticalAlignFLAG"] = "middle"
	legend["FLAGborderWidthFLAG"] = 0

	newseries = []
	tmpdic = {}
	tmpdic["FLAGnameFLAG"] = metric
	tmpdic["FLAGdataFLAG"] = series.values()
	newseries.append(tmpdic)

	htmldict["FLAGseriesFLAG"] = newseries
	htmldict["FLAGlegendFLAG"] = legend
	htmldict["FLAGyAxisFLAG"] = yAxis
	htmldict["FLAGxAxisFLAG"] = xAxis	
	htmldict["FLAGtitleFLAG"] = title


	jsonstr = JSONEncoder().encode(htmldict)


	jsonstr = rmquotes(jsonstr)
	#print jsonstr

	html = head + jsonstr + tailer

	output = open(output, 'w')
	output.write(html)
	output.close()

if __name__ == "__main__":
	parser = OptionParser(usage="%prog [optinos] filename")

	parser.add_option("-i", "--input",
	                action = "store",
	                dest = "input",
	                type = "string",
	                default = ".",
	                help = "Which file will you read information from"
	                )
	parser.add_option("-o", "--output",
	                action = "store",
	                dest = "output",
	                type = "string",
	                default = ".",
	                help = "Which file will you want save your information in"
	                )

	parser.add_option("-m", "--metric",
	                action = "store",
	                dest = "metric",
	                type = "string",
	                default = ".",
	                help = "Which metric do you want to show in this image"
	                )

	parser.add_option("-b", "--benchmark",
	                action = "store",
	                dest = "benchmark",
	                type = "string",
	                default = ".",
	                help = "Which benchmark do you want to show in this image"
	                )

	parser.add_option("-k", "--kernel",
	                action = "store",
	                dest = "kernel",
	                type = "string",
	                default = ".",
	                help = "Which kernel do you want to show in this image"
	                )
	parser.add_option("-c", "--compiler",
	                action = "store",
	                dest = "compiler",
	                type = "string",
	                default = ".",
	                help = "Which compiler do you want to show in this image"
	                )
	parser.add_option("-x", "--xAxis",
	                action = "store",
	                dest = "xAxis",
	                type = "string",
	                default = ".",
	                help = "Which dimension do you want to set as the xAxis"
	                )

	(options, args) = parser.parse_args()

	dic = read_csv(options.input)

	output = options.output
	metric = options.metric
	benchmark = options.benchmark
	kernel = options.kernel
	compiler = options.compiler
	xAxis = options.xAxis

	genhtml(dic, metric, xAxis, benchmark, kernel, compiler, output)