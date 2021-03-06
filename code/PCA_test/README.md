#A implement of Principal Components Analysis
##预处理
在进行主成分分析之前，我们需要先做以下处理：
路径补全、数据抽取和整合、数据清理和补全，然后再进行主成分分析
###路径补全
由于数据基数比较大，直接读取硬盘数据速度太慢，所以建立一个索引表，将有效文件路径统一写进**/lkp/paths**文件夹下
使用以下命令可以得到索引表：
```
find result -mindepth 7 -maxdepth 7 | while read l; do echo /$l/0/; done >paths
```
得到的路径文件大小有66M+，总计45w+结果文件
###数据抽取与整合
按照路径文件指示，更改数据抽取脚本，运行即可将数据导出为一个csv文件，便于访问。

此处有一个问题，少数数据（目前遇到了四个benchmark的数据）还有不完整的，会导致整个程序崩溃，而且按benchmark顺序逐步抽取会被大文件的抽取过程影响整体速度，
因此，按照benchmark（即-c testcase=benchmark）分别同时抽取。此举可以保证数据的完整性，但是需要多一步整合的问题。

目前尚有20个benchmark的数据抽取没有完成（总共77个），我使用了最初的30个csv文件（大小总计5.2M，目前数据总计60M+）。
使用combine.py脚本进行数据的整合，处理完的数据在washeddata.csv中。

###数据清理和补全
抽取完的数据中有一部分坏的数据（不完整，不符合格式等等），还有大量的空数据（来自矩阵合并）。
首先坏的数据需要替换，空数据需要补全。
选择补全的值最好是使整个向量的均值方差都不变，给后续PCA带来的误差也最小，但是运算量比较大，运行太慢，所以暂时使用均值代替
补全的数据有33列（完整的数据有上千列，因为跑得比较快的都是小文件，所以测试的feature也不多）

##主成分分析
使用washeddata进行主成分分析，分析的步骤如下
###1. 数据归一化
因为数字的大小相差较大，所以直接进行分析对小数值的数据不利，首先对每一组数字进行归一化处理。归一化方法很多，这里使用**最值归一化**方法。
###2. 主成分个数判断
经判断，目前的数据中主成分需要提取10个以上，才能保证方差的保留率大于95%，但是考虑到运算开销（10个实在太慢），我们先提取5个主成分，经过后面的计算我们知道方差的保留率超过72%。
###3. 主成分提取
按照上面的预测我们提取2个主成分，将主成分分析输出结果如下（输出信息比较多，详见[这里](./5_pc.txt)）：


	                       			PC1  PC2  PC3  PC5  PC4
	SS loadings              	6.43 6.20 4.55 3.55 3.01
	Proportion Var         	0.19 0.19 0.14 0.11 0.09
	Cumulative Var       	0.19 0.38 0.52 0.63 0.72
	Proportion Explained  	0.27 0.26 0.19 0.15 0.13
	Cumulative Proportion 	0.27 0.53 0.72 0.87 1.00

在[结果文件](./5_pc.txt)中我们可以看各个主成分包含的旋转成分载荷(component loadings)，成分载荷是观观测变量与主成分的相关系数。成分载荷可用于解释主成分的含义。

比如在本例中，第一主成分(PC1)与time.elapsed_time、aim7.real、aim7.time.elapsed_time、time.system_time、aim7.time.elapsed_time.max、aim7.cpu、aim7.time.system_time
几个指标相关性比较大，都在0.8以上，说明第一主成分主要反应的是时间量度。


h2栏是成分公因子方差，是主成分对每个变量的方差解释度。
U2栏是成分唯一性，是主成分无法解释变量方差的比例，其值=1-h2。

比如本例中，五个主成分对kmsg.ERST.Can_not_request.mem....for_ERST 指标的方差解释为99.3%，0.7%不能解释，基本上已经涵盖了这个指标。

SS loadings包含了与主成分相关联的特征值，其含义是与特定主成分相关联的标准化后的方差值。比如，本例中，第一主成分的值为6.43。
接下来的proportion  var和cumulative var分别为主成分对整个数据集的方差解释度和累积解释度。
本例中，第一主成分解释了33个指标19%的方差，第二主成分解释了19%的方差等等，累计方差的解释度为72%。

##4. 获取主成分的得分
获取主成分得分信息比较多，详见[这里](./5_pc.txt)
根据上述的结果，即可写出五个主成分的方程。根据方程，可以简化数据文件，将五个主成分作为指标，再应用其他的perf bug分析方法。

目前来看，五个主成分分别与system time、warning和bug、吞吐率、user time、自主性（voluntary）主要相关。