import csv
import random

myfile = open("data.csv","wb")
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

mylist = []
feature = ["100", "jump", "ball", "high", "sibai", "yibaiyi", "tiebing"]
x1 = [11.25, 7.43, 15.48, 2.27, 48.90, 15.13, 49.28]
x2 = [10.87, 7.45, 14.97, 1.97, 47.71, 14.46, 44.36]
x3 = [11.18, 7.44, 14.20, 1.97, 48.29, 14.81, 43.66]
x4 = [10.62, 7.38, 15.02, 2.03, 49.06, 14.72, 44.80]
x5 = [11.02, 7.43, 12.92, 1.97, 47.44, 14.40, 41.20]
x6 = [10.83, 7.72, 13.58, 2.12, 48.34, 14.18, 43.06]
x7 = [11.18, 7.05, 14.12, 2.06, 49.34, 14.39, 41.68]
mylist.append(feature)
mylist.append(x1)
mylist.append(x2)
mylist.append(x3)
mylist.append(x4)
mylist.append(x5)
mylist.append(x6)
mylist.append(x7)

wr.writerow(mylist)

