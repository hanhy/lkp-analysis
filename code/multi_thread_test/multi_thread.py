# -*- coding: utf-8 -*-
#create time : 2016-04-23
#modify time : 2016-04-24
#author : Huiyang.Han

#2016-04-24: achieve

"""import datetime   

starttime = datetime.datetime.now()   
for i in range(10):
	print ""
endtime = datetime.datetime.now()   
print (endtime - starttime).seconds  
"""

import threading  
import datetime  

class reader(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self):  
        threading.Thread.__init__(self)  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        sum = 0
        for i in range(10000000):
            sum += i
        print sum
   
def test():    
    reader1 = reader()  
    reader2 = reader()  
    reader3 = reader()  
    reader4 = reader() 
    reader5 = reader()  
    reader6 = reader() 
    reader7 = reader()  
    reader8 = reader() 
    reader9 = reader()  
    reader10 = reader() 

    reader1.start()
    reader2.start()
    reader3.start()
    reader4.start()
    reader5.start()
    reader6.start()
    reader7.start()
    reader8.start()
    reader9.start()
    reader10.start()

    reader1.join()
    reader2.join()
    reader3.join()
    reader4.join()
    reader5.join()
    reader6.join()
    reader7.join()
    reader8.join()
    reader9.join()
    reader10.join()
    
if __name__ == '__main__':  
    starttime = datetime.datetime.now() 
    test()
    endtime = datetime.datetime.now()   
    print (endtime - starttime).seconds 

    starttime = datetime.datetime.now()
    for i in range(10):
        sum = 0
        for i in range(10000000):
            sum += i
        print sum

    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds
