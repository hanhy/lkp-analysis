#coding=utf-8
#create time : 2016-03-25
#modify time : 2016-03-25
#author : Huiyang.Han

#After PCA, we use this script to extract pc
#A dimensionality reduced csv file will be given

import sys
import os
import csv
import re

MISSINGCALUE = -1

def mean(l):
	length = len(l)
	sum = 0.0
	for i in l:
		sum += i
	return sum / float(length)

#spin one csv matrix
def spin(ll):
	length = len(ll[0])

	newll = []
	for i in range(length):
		tmpl = []
		newll.append(tmpl)

	for l in ll:
		for i in range(length):
			newll[i].append(l[i])
	return newll

#combine the csv files
def combine(total):
	totalll = {}
	totallen = 0
	for matrix in total:
		#right-up
		for l in matrix:
			#print type(l[0])
			#print totalll
			if totalll.has_key(l[0]):
				#print totalll[l[0]]
				totalll[l[0]].extend(l[1:])
			else:
				mm = mean(l[1:])
				tmpl = ([mm] * totallen)
				tmpl.extend(l[1:])
				totalll[l[0]] = tmpl
				#print "nononononono"
				#print totalll
				#raw_input( )
		totallen += len(l) - 1
		
		#left-down
		for k, v in totalll.items():
			if len(v) < totallen:
				v.extend([mean(v[1:]) * (totallen - len(v))])
				totalll[k] = v
	return totalll

def dict2ll(total):
	ll = []
	size = 0
	for k,v in total.items():
		size += 1
		tmpl = [k]
		tmpl.extend(v)
		ll.append(tmpl)
	return ll, size

def isnumber(s):
	pattern = re.compile(r'^[-]?[\d]*[\.]?[\d]*$')
	match = pattern.match(s) 
	if match:
		return True
	else:
		return False

#Obtain the file list
print "Obtain the file list"
csv_list = []
for filename in os.listdir("ori_data"):
    csv_list.append("ori_data/" + filename)

#combine the csv files
#we can obtain a spined ll from each csv
total = []
for each_csv in csv_list:
	ll = []#a list of list
	#print each_csv
	row_cnt = 0
	colcnt = 0

	rcsvfile = file('data.csv', 'rb')
	reader = csv.reader(rcsvfile)

	flag = False
	for row in reader:
		#print line
		#print type(line) #list
		
		tmpl = []
		if not flag:
			tmpl = row
			flag = True
		else:
			for ii in row:
				if not isnumber(ii):
					print type(ii)
					print "woc"
					print ii
					raw_input()
					tmpl.append(0)
				else:
					tmpl.append(float(ii))
		ll.append(tmpl)

	rcsvfile.close()

	#print ll
	print "spin"
	#raw_input()
	spinedll = spin(ll)
	total.append(spinedll)
print "combine"
combined_csv = combine(total)

#write to a new csv file
ll, col = dict2ll(combined_csv)

print "col"
print col

wcsvfile = file('washeddata.csv', 'wb')
writer = csv.writer(wcsvfile)

for i in range(len(ll[0])):
	line = []
	for j in range(col):
		line.append(ll[j][i])
	writer.writerow(line)

wcsvfile.close()
#end
