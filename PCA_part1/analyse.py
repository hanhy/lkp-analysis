#coding=utf-8
#create time : 2016-05-24
#commit time : 2016-05-24
#author : Huiyang.Han
#Analyse the result of Pearson correlation

import math
import csv

metrics = []
for line in open("result.txt"):
	metrics.append(line[0:len(line) - 1])
l = len(metrics)
rs = metrics[l - 1]
rs = rs.replace("[", "").replace("]", "").replace(" ", "")
rs = rs.split(",")
l = len(rs)
for i in range(l):
	rs[i] = float(rs[i])
pearson = dict()
for i in range(l):
	if not math.isnan(rs[i]):
		pearson[metrics[i]] = rs[i]

metrics = pearson.keys()
r = []
for m in metrics:
	r.append(pearson[m])
	if pearson[m] >= 1 or pearson[m] <= -1:
		print m, pearson[m]

#write to a csv file

csvfile = file('correlation.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(metrics)
writer.writerow(r)
csvfile.close()