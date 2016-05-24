#coding=utf-8
#create time : 2016-05-23
#commit time : 2016-05-23
#author : Huiyang.Han

import csv
import numpy

KPI = "ebizzy.throughput"

def get_kpi_data(benchmark, csv_file):
	#read the csv file and return a dict whose keys are kpi and pan-kpi
	#and whose values are a list of numric

	pan_kpi = []
	kpi_data = dict()
	kpi_index = dict()

	csvfile = file(csv_file, "rb")
	reader = csv.reader(csvfile)

	for line in reader:
		length = len(line)
		for i in range(length):
			#if not cmp(line[i].split(".")[0], benchmark):
			str = line[i]
			if cmp(str, "benchmark") and cmp(str, "config1") and cmp(str, "config2") and cmp(str, "config3") and cmp(str, "kernel") and cmp(str, "compiler") and cmp(str, "commit"):
				pan_kpi.append(line[i])
				temp_list = []
				kpi_data[line[i]] = temp_list
				kpi_index[line[i]] = i
		break
	for line in reader:
		#print line
		for k, v in kpi_data.items():
			kpi_data[k].append(line[kpi_index[k]])
	csvfile.close()
	return kpi_data, pan_kpi

def empty_num(kpi_data, pan_kpi):
	for kpi in pan_kpi:
		print kpi
		kpi_list = kpi_data[KPI]
		pan_kpi_list = kpi_data[kpi]
		length = len(kpi_list)
		num = 0
		for i in range(length):
			if len(kpi_list[i]) == 0 or len(pan_kpi_list[i]) == 0:
				num += 1
		print num

def expect(l):
	N = len(l)
	narray = numpy.array(l)
	sum1 = narray.sum()
	exp = sum1 / N
	return exp

def sigma(l):
	N = len(l)
	narray = numpy.array(l)
	sum1 = narray.sum()
	narray2 = narray * narray
	sum2 = narray2.sum()
	mean = sum1 / N
	var = sum2 / N - mean ** 2
	if 
	sig = numpy.sqrt(var)
	return sig

def cov(l1, l2):
	u = expect(l1)
	v = expect(l2)

	newl = []
	N = len(l1)
	for i in range(N):
		newl.append((l1[i] - u) * (l2[i] - v))
	s = numpy.sum(newl)
	return s

def cal_pearson(l1, l2):
	return cov(l1, l2)/(sigma(l1) * sigma(l2))/(len(l1) - 1)

def filte(metric, kpi_data):
	pass

def cal_corr(kpi_data, pan_kpi):
	pearson = []
	print len(pan_kpi)
	for kpi in pan_kpi:
		print kpi
		#if not cmp(kpi, KPI):
		#	continue
		new_kpi_list = []
		new_pan_kpi_list = []
		length = len(kpi_data[kpi])
		for i in range(length):
			str1 = kpi_data[KPI][i]
			str2 = kpi_data[kpi][i]
			if len(str1) > 0 and len(str2) > 0: 
				#print "hahahahaha"
				new_kpi_list.append(float(str1))
				new_pan_kpi_list.append(float(str2))
		pearson.append(cal_pearson(new_kpi_list, new_pan_kpi_list))
	print pearson

if __name__ == "__main__":
	kpi_data, pan_kpi = get_kpi_data("ebizzy", "ebizzy.csv")
	print len(kpi_data["ebizzy.throughput"])
	#empty_num(kpi_data, pan_kpi)
	cal_corr(kpi_data, pan_kpi)