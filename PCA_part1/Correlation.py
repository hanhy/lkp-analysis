#coding=utf-8
#create time : 2016-05-23
#commit time : 2016-05-23
#author : Huiyang.Han

import csv

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
			if not cmp(line[i].split(".")[0], benchmark):
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

#def cal_corr(kpi_data):
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

if __name__ == "__main__":
	kpi_data, pan_kpi = get_kpi_data("ebizzy", "ebizzy.csv")
	print len(kpi_data["ebizzy.throughput"])
	empty_num(kpi_data, pan_kpi)