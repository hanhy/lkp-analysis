#coding=utf-8
#create time : 2016-04-11
#modify time : 2016-04-24
#author : Huiyang.Han

#2016-04-24:multiple thread and only collect

import os
import sys
import json
import csv
import pp

def collect(pathfile):
	#input: a path file
	#output: nothing
	#function: collect and save to csv

	#Indicators

	FULLFILL = ""
	BINDEX = 1
	CONFIG1 = 2
	CONFIG2 = 3
	CONFIG3 = 4
	KINDEX = 5
	CINDEX = 6
	COMMIT = 7

	print "Collect"
	table = []
	#print pathfile
	for path in open(pathfile):
		#print path
		path = path.replace("\n", "")
		if os.path.exists(path):
			#print path
			jsontext = open(path).read()
			if len(jsontext) > 2:#{}
				dic = json.loads(jsontext)
				del dic["stats_source"]

				def mean(vdic):
					#input: a dict whose value is a list
					#output: a dict whose value is the mean value of the former value
					#function: obtain the mean value of the list
					newdic = {}
					for key, value in vdic.items():
						#print key
						sum = 0.0
						for num in value:
							#print num, sum
							sum += float(num)
						if len(value) != 0:
							print value
							value = sum / float(len(value))
						else:
							value = sum
						newdic[key] = value
					return newdic

				dic = mean(dic)
				#print dic
				pathsplit = path.split("/")

				dic["benchmark"] = pathsplit[BINDEX]
				dic["config1"] = pathsplit[CONFIG1]
				dic["config2"] = pathsplit[CONFIG2]
				dic["config3"] = pathsplit[CONFIG3]
				dic["kernel"] = pathsplit[KINDEX]
				dic["compiler"] = pathsplit[CINDEX]
				dic["commit"] = pathsplit[COMMIT]

				table.append(dic)
			else:
				continue
		else:
			#print os.getcwd(), path, os.path.exists(path)
			continue
		
	#print table

	print "Collect finished"

	print "Combine"

	full = {}
	length = 0
	for dic in table:
		length += 1;
		for k,v in dic.items():
			if full.has_key(k):
				full[k].append(v)
			else:
				full[k] = [v]
		for k,v in full.items():
			while len(v) < length:
				full[k].append(FULLFILL)
	print "Combine finished"

	"""
	#get rid of boolean metrics
	for key, value in full.items():
		#print key
		sum = 0.0
		notbool = False
		for num in value:
			#print num, sum
			sum += float(num)
			if num != 0.0 and num != 1.0:
				notbool = True
		if notbool or True:
			#print value
			value = sum / len(value)
			newdic[key] = value
	"""

	print "Savetocsv"

	keylist = full.keys()
	special = ["benchmark", "config1", "config2", "config3", "kernel", "compiler", "commit"]
	orderlist = []#first three
	orderlist[0:6] = special
	for key in keylist:
		if not key in special:
			orderlist.append(key)

	wcsvfile = file("csv/" + pathfile.split("/")[1].split(".")[0] + '.csv', 'wb')
	writer = csv.writer(wcsvfile)
	
	writer.writerow(orderlist)#write the first row : metrics
	
	row = len(full["benchmark"])
	col = len(keylist)
	
	for i in range(row):
		line = []
		for key in orderlist:
			#print i
			line.append(full[key][i])
		writer.writerow(line)
	wcsvfile.close()

	return table

if __name__ == "__main__": 
	ppservers=()

	if len(sys.argv) > 1:
		ncpus = int(sys.argv[1])
		# Creates jobserver with ncpus workers
		job_server = pp.Server(ncpus, ppservers=ppservers)
	else:
		# Creates jobserver with automatically detected number of workers
		job_server = pp.Server(ppservers=ppservers)
	print "pp Server start with", job_server.get_ncpus(), "workers"

	benchmark_path_list = os.listdir("path")

	jobs = [(input, job_server.submit(collect, ("path/" + input,), (), ("csv","os","sys","json"))) for input in benchmark_path_list]

	for benchmark_path, job in jobs:
		job()
	job_server.print_stats()