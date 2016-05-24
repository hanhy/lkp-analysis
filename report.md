#进展报告
##12-26
    阅读论文Impact of Triage: a Study of Mozilla and Gnome，论文报告已经写进了paper-reading-report/paper1_impactoftriage.md中
    这篇论文主要讲述了triage（分流）在整个项目中的作用，并对其进行了量化，找出影响triage效果的两个重要的因素：报告过滤和补全报告信息
    详细内容见阅读报告
##12-27
预计跑R实验程序和读另外两篇paper
##12-29
	论文2太长了。。英语太差读得慢，刚刚读完，论文总结放在了reading-report/paper2_mozilla.md	晚上把gitlog下了过来，做了一些初步的处理（中间有个perl脚本中有一句报错，已经解决不知道对不对，问题放在repo的issue里）：
    git-repo------>log.linux------>linux.l1
    使用linux.l1测试了一下R的样句，跑到画图那一步挂掉了。。提示格式有问题，检查了几遍目前还没有发发现。
##12-30
	完成了初版的开题报告PPT，./thesis_proposal.md
##1-3
	改了一下开题报告，然后利用gitstats做了一些处理结果在./gitstats/res
    其中index.html比较有意思，里面内容很多，包含了一些图表等，用浏览器打开（Chrome或fiefox）可以看到效果。
##3-6
** 本周总结 **

- 论文阅读：已经上传了阅读报告
- 运行、理解北大同学代码，与其交流，请教不明白的地方
- 尝试参照北大同学的工作重现分析框架

** 下周规划 **

- 重现linux-kernel的分析程序
- 寻找相关研究工作的论文，阅读并写出报告（注意报告的完整性，对以后的论文写作有复查的作用）
- 根据linux-kernel的分析总结主要工作，规划aosp的分析过程

##3-10
正在跑lkp-tests
lkp install jobs/hackbench.yaml需要安装一系列依赖

其中ruby-git没法装，报错/usr/lib/ruby/2.1.0/rubygems/core_ext/kernel_require.rb:55:in `require': cannot load such file -- git (LoadError)

gem install git

可能需要更换包源，不然没法下载

同时要安装以下依赖，不然gem无法运行

ruby-devel
libsqlite3x-devel
rpm-build
zlib-devel
##3-11
解决了ruby-git不能安装的问题，原因是安装过程中没有安装ruby-dev，而很多gems都是依赖ruby-dev的库编译运行的，缺少ruby-dev，gem安装时经常或报错： 
```
ERROR: Faild to build gem native extension 
```
所以之前提到的四个依赖包只需要安装一个ruby-dev

按照lkp install（安装）->lkp split（分解job）->lkp run（运行）的顺序运行一个原子job，lkp split结果为（...为/media/hanhy/Howie.Han/Documents/Career/Graduation/WORKING_DIRECTORY/aosp-working-analysis/lkp-tests/jobs）：
```
.../hackbench.yaml => ./hackbench-1600%-process-pipe.yaml
.../hackbench.yaml => ./hackbench-1600%-process-socket.yaml
.../jobs/hackbench.yaml => ./hackbench-1600%-threads-pipe.yaml
.../hackbench.yaml => ./hackbench-1600%-threads-socket.yaml
.../hackbench.yaml => ./hackbench-50%-process-pipe.yaml
.../hackbench.yaml => ./hackbench-50%-process-socket.yaml
.../hackbench.yaml => ./hackbench-50%-threads-pipe.yaml
.../hackbench.yaml => ./hackbench-50%-threads-socket.yaml
```
与官方文档一致
在运行lkp run之后出现错误：
```
/media/hanhy/Howie.Han/Documents/Career/Graduation/WORKING_DIRECTORY/aosp-working-analysis/lkp-tests/bin/cmd: 7: exec: /usr/bin/hackbench: not found
```
即不能找到/usr/bin/hackbench文件（或文件夹，经查看确实不存在）
参考之前陈振寰的工作他是使用了intel工程师的hackbench.c（还没拿到）

##3-14
完成了论文列表，进行了一些粗读，筛选出了11篇与我的工作比较相近的论文，详见[paperindex.md](./paperindex.md)
##3-15
上午上课，下午参与了陈老师的会议，确定本周目标，与茅俊杰学长交流，接受他的工作，在远程服务器上跑通lkp-test，然后参考学长的方法完成数据采集，下周汇报的时候需要具体讲述数据提取的情况，以及采集到的主要feature。
##3-18
与茅俊杰学长交流之后目前形成的大致思路：
1. 首先运行lkp-compare（即intel目前在用的性能检测方法）
2. 了解性能指标的意义，补全index，使用之前的脚本程序（处理不完整的数据和格式出错的数据）将其整合为一整个csv文件
3. 挑选合适的降维算法（当前提出了两个应用比较广泛的PCA和FA）完成降维
4. 后续的处理分析（To be continued...）
##3-20
完成了PCA（主成分分析）的测试，代码及分析报告点击[这里](./code/PCA_test)
##3-24
完成了csv的提取。
修改了茅俊杰学长的脚本，可以实现所有数据的提取（之前的只能提取Mresult_root）
关键修改：result_root.rb文件中的Mresult_root check行为需要去掉，直接将所有的文件按照Mresult_root的格式写入csv
第二点：识别文件路径中的关键字，比如
```
result/aim7/400-brk_test/lkp-a04/debian-x86_64-2015-02-07.cgz/x86_64-rhel/gcc-4.9/d8cc3972b2178f9fe532306330f76bf51cb0d8bd/0/
```
中依次是根目录、benchmark等，但是不同文件目录导致识别错误，所以，建立文件链接表
```
 sudo ln -s /media/hanhy/Howie.Han/Documents/result result
```
直接映射到数据存储的位置。

此时生成了一个path文件，存储了所有测试样例的路径，共计45万余条，文件大小66M+
遍历path中的路径可以得到一个初步的csv文件。

csv抽取、补全->降维->分析

下午和晚上：
由于部分testcase所做的测试比较多，抽取数据花费时间比较场，所以按照testcase划分，每一个testcase生成一个csv文件，可以先拿到一部分可用的数据。

运行了一个晚上，共有77个testcase，完全抽取的是30个，三个程序中断，44个尚未跑完。

写了两个脚本整合、筛选完全抽取的30个csv文件，得到了一个稀疏矩阵，下面是补全的工作，预计明天上午能做完补全和降维，下午着手分析。

##3-28
上午参与了高性能所的中期检查，老师提出的问题是关于题目更改上的，确认AOSP的预测应该不做了，主要集中在linux-kernel的性能分析上

##3-31
论文
Zhen Jia1,, Jianfeng Zhan , Lei Wang，etc, [*Characterizing and Subsetting Big Data Workloads*](http://prof.ict.ac.cn/BigDataBench/wp-content/uploads/2014/04/IISWC_jz.pdf),2014
的[slides](paper-reading-report/publish/paper_index0.htm)以及[markdown文件](paper-reading-report/paper_index0.md)
##4-01
论文阅读报告pdf版本的slides在[这里](paper-reading-report/pdf/index0.pdf)，也已经上传bitbucket
##4-06
根据昨天在向勇老师处的交流以及上周与黄工的会议，接下来的一个月大致三块
- 本周（第七周）
	完成lkp-test结果降维后的指标的提取和可视化，包括分内核版本、编译器版本等，要求使用html图表的形式，同时评价提取指标的代表性水平
	开始撰写毕业论文的框架
	根据研究目标的调整，本周论文阅读需要完成[列表](paper-index.md)中的2、4、5三篇
- 第八周
	完成benchmark的降维处理，研究曲线的相关性特点，同样要求可视化并评价降维效果（鉴于降维之后benchmark肯定会变少，所以主要考虑保留度）
	阅读论文列表[列表](paper-index.md)中的7、8、10三篇
	撰写毕业论文的课题研究背景、目的、内容部分

- 不同linux kernel版本之间的pattern变化模式（跳变、线性等）
	阅读论文列表[列表](paper-index.md)中的15、18、19、21
	更新毕业论文中背景、目的、内容的部分，并开始写主要研究工作部分
##4-24
	使用parallel python对之前的程序进行了加速，提取的过程从20+小时降到一个小时之内
##4-27
按照黄工之前给的邮件内容：
	
	之前我们说对每一个benchmark，有多组test parameter，每一组test parameter对应一次测试，我们的一个目标是通过发现测试之间结果的相关性，发现冗余的测试。但对于每次测试，也会有多组性能指标，这使得比较测试结果间的相关性变得更复杂。所以我建议这里可以分两阶段进行。阶段1比较同一次测试，不同性能指标间的相关性。这个对于我们分析，理解性能指标也很有价值，本身可以作为我们工作的成果之一。阶段2比较不同测试间的性能指标，可以以KPI (Key Performance Index关键性能指标)为主，也就是看不同测试间KPI的相关性。
	这个工作感觉不需要降维，因为维度体现在test parameter里。
今天准备以aim7为例，进行单个测试内部的指标相关性分析
##5-18
选定皮尔森相关系数作为指标相关性分析的衡量标准，以ebizzy为例，分别分析每个指标和ebizzy.throughput的相关性，给出解释
尚需确定空缺数据的处理方法
##5-20
先不管空缺数据，看看能有多少缺少的，如果不影响比较（两个向量有交集）的话就没关系。

在分析我先找到了ebizzy的KPI：ebizzy.throughput和17个准
KPI:
ebizzy.throughput.per_thread.min
ebizzy.time.minor_page_faults
ebizzy.time.user_time
ebizzy.time.page_size
ebizzy.throughput.per_thread.stddev_percent
ebizzy.time.system_time
ebizzy.time.user
ebizzy.time.elapsed_time.max
ebizzy.time.sys
ebizzy.time.file_system_outputs
ebizzy.time.involuntary_context_switches
ebizzy.time.maximum_resident_set_size
ebizzy.time.elapsed_time
ebizzy.time.voluntary_context_switches
ebizzy.time.real
ebizzy.time.percent_of_cpu_this_job_got
ebizzy.throughput.per_thread.max
我的思路是首先分析这17个准KPI和KPI相关性的大小，按照他们被设定成准KPI的事实来看，相关性应该很大，可以作为是否相关的一个标准值
##5-23
几个准ebizzy中的kpi含有数字5238个，其17个准KPI的值中都是有约3900个的空值，尚且有1000个以上的可比较值，因此可以实现比较。

我计算的18个准KPI（其中包括KPI本身）与KPI的相关系数表格如下所示：
ebizzy.time.involuntary_context_switches
ebizzy.time.maximum_resident_set_size
ebizzy.throughput
ebizzy.time.elapsed_time
ebizzy.time.voluntary_context_switches
ebizzy.time.real
ebizzy.time.percent_of_cpu_this_job_got
ebizzy.throughput.per_thread.max
ebizzy.throughput.per_thread.min
ebizzy.time.minor_page_faults
ebizzy.time.user_time
ebizzy.time.page_size
ebizzy.throughput.per_thread.stddev_percent
ebizzy.time.system_time
ebizzy.time.user
ebizzy.time.elapsed_time.max
ebizzy.time.sys
ebizzy.time.file_system_outputs
[0.65636159150479501, 0.61894249478962238, 1.0007541478129702, -0.091181707089333111, 0.57911967189022107, 0.12726592357809047, 0.60550377165085978, 0.042290611160961951, -0.082054380510512046, 0.99200646319340435, 0.74195632268186562, 0.14034997994668358, -0.43902747989437596, 0.59495980389181624, 0.74694998790454392, -0.091181707089333111, 0.58691781161965473, 0.084365981758326866]
从数据中可以看出相当大的一部分准KPI与KPI的相关性都很大，很多都超过了0.5
接着我们计算所有的指标与KPI的相关性，形成的结果将使用一个csv表格来呈现
#5-24
从前面的结果看有一些指标与KPI的相关系数绝对值超过了1，且其一大部分都是正负2.0，这明显是错误的结果，现在我们要找出为什么会出现这种错误，
以其中相关系数为2.0的指标diskstats.sde2.time_in_queue为例，看看它与KPI之间的数据差别。

























