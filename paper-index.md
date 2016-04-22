#论文列表
##初选
###列表
1. Zhen Jia1,, Jianfeng Zhan , Lei Wang，etc, ["Characterizing and Subsetting Big Data Workloads"](http://prof.ict.ac.cn/BigDataBench/wp-content/uploads/2014/04/IISWC_jz.pdf),2014

1. Adrian Nistor1, Linhai Song2, Darko Marinov1 and Shan Lu. _**[Toddler: Detecting Performance Problems via Similar Memory-Access Patterns.](http://people.cs.uchicago.edu/~shanlu/paper/icse13-preprint.pdf)**_ In ICSE, 2013.

2. Yepang Liu, Chang Xu and Shingchi Cheung. _**[Characterizing and Detecting Performance Bugs for Smartphone Applications.](http://tcloud.sjtu.edu.cn/wiki/images/e/e4/Characterizing_and_Detecting_Performance_Bugs.pdf)**_ In ICSE, 2014.

3. Michael.J.Fischer, Martin Pinzger, Harald Gall. _**[Populating a Release History Database from version control and bug tracking systems.](http://swerl.tudelft.nl/twiki/pub/Trash/MartinPinzgerPublications/Fischer2003-rhdb.pdf)**_ In ICSM, 2003.

4. Nachiappan Nagappan, Thomas Ball and Andreas Zeller. _**[Mining Metrics to Predict Component Failures.](http://research.microsoft.com/pubs/70232/tr-2005-149.pdf)**_ In ICSE, 2006.

5. T.Zimmermann, Rahul Premraj and Andreas Zeller. _**[Predicting Defects for Eclipse.](http://thomas-zimmermann.com/publications/files/zimmermann-promise-2007.pdf)**_ In MoDELS, 2007.

6. Sunghun Kim, Thomas Zimmermann, E.James Whitehead and Andreas Zeller. _**[Predicting Faults from Cached History.](http://thomas-zimmermann.com/publications/files/kim-icse-2007.pdf)**_ In ICSE, 2007.

7. Patrice Godefroid, Nils Klarlund and Koushik Sen. _**[DART: directed automated random testing.](http://research.microsoft.com/en-us/um/people/pg/public_psfiles/pldi2005.pdf)**_ In pldi, 2005.

8. Cristian Cadar, Daniel Dunbar and Dawson R Engler. _**[KLEE: unassisted and automatic generation of high-coverage tests for complex systems programs.](http://llvm.org/pubs/2008-12-OSDI-KLEE.pdf)**_ In OSDI, 2008.

9. Dawson R Engler, David Yu Chen, Seth Hallem, Andy Chou and Benjamin Chelf. _**[Bugs as deviant behavior: a general approach to inferring errors in systems code.](http://research.cs.queensu.ca/~ahmed/home/teaching/CISC880/F10/papers/BugsAsDeviantBehavior_SOSP2001.pdf)**_ In sosp, 2001.

10. Cristian Cadar and Koushik Sen. _**[Symbolic execution for software testing: three decades later.](http://www.eecs.berkeley.edu/~raluca/cs261-f15/readings/symb.pdf)**_ In Communications of the ACM, 2013.

11. Adrian Nistor, Tian Jiang and Lin Tan. _**[Discovering, reporting, and fixing performance bugs.](http://mir.cs.illinois.edu/~nistor1/pubs/msr13.pdf)**_ In MSR, 2013.

12. Christian Bird, Alex Gourley, Prem Devanbu, Michael Gertz and Anand Swaminathan. _**[Mining email social networks.](http://research.microsoft.com/pubs/138221/bird2006mes.pdf)**_ In MSR, 2006.

13. Luis Lopezfernandez, Gregorio Robles, Jesus M Gonzalezbarahona, U Rey and Juan Carlos. _**[Applying Social Network Analysis to the Information in CVS Repositories.](http://gsyc.es/~jgb/libresofteng/sna-repositories-2004/sna-repositories-2004.pdf)**_ In MSR, 2004.

14. Jaime Spacco, David Hovemeyer and William Pugh. _**[Tracking defect warnings across versions.](http://www.irisa.fr/lande/lande/icse-proceedings/msr/p133.pdf)**_ In MSR, 2006.

15. Abram Hindle, Daniel M German and Ric Holt. _**[What do large commits tell us?: a taxonomical study of large commits.](http://turingmachine.org/~dmg/papers//dmg2008_msr_largeCommits.pdf)**_ In MSR, 2008.

16. Daniel M German. _**[Mining CVS repositories, the softChange experience.](http://2004.msrconf.org/papers/German.pdf)**_ In MSR, 2004.

17. Sunghun Kim, E J Whitehead and Yi Zhang. _**[Classifying Software Changes: Clean or Buggy?.](https://users.soe.ucsc.edu/~ejw/papers/cc.pdf)**_ In IEEE, 2008.

18. S.M.A. Zaman, Bram Adams and Ahmed E.Hassan. _**[A qualitative study on performance bugs.](http://sail.cs.queensu.ca/Downloads/MSR2012_AQualitativeStudyOnPerformanceBugs.pdf)**_ IN MSR, 2012.

19. Godfrey and Qiang Tu. _**[Evolution in open source software: a case study.](http://plg.uwaterloo.ca/~migod/papers/2000/icsm00.pdf)**_ In ICSM, 2000.

20. Kunrong Chen and Vaclav Rajlich. _**[Case study of feature location using dependence graph.](http://www.cs.wayne.edu/~vip/publications/Chen.IWPC.2000.FeatureLocation.pdf)**_ In ICPC, 2000.

21. Thomas Eiter and Heikki Mannila. _**[Computing Discrete Fr´echet Distance](http://www.kr.tuwien.ac.at/staff/eiter/et-archive/cdtr9464.pdf)**_ In CD-TR, 1994.

22. to be continued...

###简介
1. 	介绍了一种叫做TODDLER的性能缺陷预测和检测的方法。

2.  介绍了安卓智能手机中的性能缺陷的种类和特点、检测方法等。

3.  基于大量有效信息被版本控制系统忽略的事实，引入了一种将bug-tracking（作为补充）和version-control结合的方式，然后我们可以对结构化的数据进行简单查询，获得其发展进程，这对于软件迭代过程的**推理和预测**很有帮助（文章使用了Mozilla作为研究对象）。

4.  文章研究发现软件的易出错性与其代码的复杂度量度有关系，但是没有一个通用的量化指标，文章建立了一个**回归模型**来**预测软件发布之后会出现错误的可能性**，且可移植性很大。

5.  建立了从eclipse的bug数据库中的数据到源码的映射关系，得到的数据集最终列出了三个版本的所有包和文件的缺陷数据，另外还做了统一的**复杂性度量**的基准（值得参考）。

6.  本文发现软件错误往往不是单独发生，而是相关几个问题一起发生，因此引入了一种缓存法：从已知的故障位置出发，记录下相关的位置、出错的位置、最近添加的和改变的位置，当已知错误修正之后观察其变化，从而检测出易出错区。

7. 提出了一种软件自动测试工具，结合了三种技术：
	1、使用静态源码分析自动提取软件与外部环境的程序接口
    2、为以上接口生成测试驱动，该接口可以对程序能够运行的最一般环境（模拟的）做随机测试
    3、动态分析程序在随机测试的表现，针对沿着替代程序路径的直接系统级执行，自动生成新的测试输入
    该三项技术构成了*直接自动随机测试*（Directed Automated Random Testing）,简称DART。
	DART最大的好处就在于测试可以在任何编译的程序上完全自动地执行，不需要编写任何测试驱动或工具代码
    测试中，DART会检测出诸如程序崩溃、违规断言和非终止错误等标准的error，目前对C程序的初步单元测试结果很令人鼓舞。

8. 提出了一种新的符号执行工具——KLEE，它能够在在多样化的复杂度和环境密集型程序中实现高覆盖率的自动测试用例的生成。文章中使用了KLEE彻底检查了安装在数以百万计的Unix系统的用户级环境中的GNU的coreutils工具套件中的所有89个独立程序。KLEE生成的测试实现了高线路覆盖率，每个工具的平均覆盖率超过90%（中位数是94%），远远高于开发者自己编写的测试用例。当作者对在BUSYBOX嵌入式系统套件中的75个等价工具做同样的测试时，覆盖率更大，其中的31个甚至达到了100%。KLEE还可以用作为错误检测的工具，作者将它用于452个应用（共包含了430K以上的代码量），KLEE从中发现了56个严重的bug，包括15年来COREUTILS中一直被忽略的3个错误。

9. 在真实系统中查找程序中的错误的一个主要障碍是知道什么是必须服从的正确规则。这些规则往往是没有明确记录的或以特别的方式指定。本文展示了一种自动从源代码本身而非程序提取检查信息的技术，从而避免了系统的规则的先验知识的需要。之所以不需要先验知识，是因为文章中的方法是根据程序员的代码分析他们的“belief”，当出现不同的belief时候，说明有矛盾的存在，这里就指出了一个error。

10. 因为符号执行软件测试能够产生高覆盖率的测试套件并且能找到复杂软件的深层错误，有关研究激增，文章中给出了现在符号执行技术的概述，讨论了路径探索，约束求解，记忆造型方面的关键挑战，并讨论了几个基于作者自己工作的解决方法。

11. 文章介绍了性能缺陷是如何被发现、报告给开发者并且被开发者修复，以及与非性能缺陷相比有什么区别。本文研究了三个软件区分性能缺陷与其他的bug，分别是：Eclipse JDT, Eclipse SWT 和 Mozilla。

12. 本文以基础设施的讨论为基础，然后讨论作者挖掘邮件档案的方法，最后从分析的数据中提出一些初步结果。

13. 开源软件的存储库中大量的数据和数据之间的相互关系提供了从中提取很多关于其结构、演化和内部流程的有价值的信息。然而，这些信息在没有能够突出该项目特定方面的资料的方法之前能够提供的有效信息很少，文章建议使用**社交网络分析**方法来表现软件随时间的演化和它们的内部结构。并且文章给出了使用该方法的一个真实案例，并且从经验中获取了一些初步的结论。

14. 本文主要研究在开源软件的版本演化过程中的潜在问题，文章中讨论了其在FindBugs中实现的两种不同的技术，用于跨版本跟踪缺陷，讨论它们的相对优点和如何将它们纳入到软件开发过程，并讨论结果追踪整个Sun的Java运行时库缺陷警告。

15. 从开源软件的代码库中挖掘数据通常会忽略包含有大量文件的提交（称之为大提交），本文的主要目标是理解大提交背后的原因，以及我们可以从中学习到什么。作者在文中做的研究对象包含了来源于九个开源软件的大提交，而且进行了手动分类。大提交更具有生产力，而小提交更倾向于纠正错误。

16. CVS日志文件是丰富的软件开发轨迹的研究来源，本文介绍了怎样提取这些轨迹并且增强他们，同时本文还解决了CVS事实提取给研究者带来的一些挑战。

17. 本文介绍了一种叫做“更改分类（Change Classification）”的发现潜在软件bug的方法。该方法使用一种机器学习的分类器来判断一个新的更改是更倾向于包含bug还是完全没有bug。该方法使用的feature是从历史版本代码库中分离出来的。该分类器的分类精度能够达到78%的准确率和65%的召回率。该方法有几个理想的特质：
	（1）预测的粒度小（改变到单个文件）
	（2）预测不要求有关源代码语义信息
	（3）该技术适用于项目类型和编程语言浩如烟海
	（4）改变完成后可以立即进行预测
	本文的贡献包括：对于改变分类方法的描述，从源码和变更历史中提取feature的技术，改变分类法在12个开源软件项目中的表现，以及不同群体特征的预测能力评估。

18. 本文定性地随机研究了400个来自Mozilla Firefox和GoogleChrome的性能bug和非性能bug，我们发现开发者和用户往往会在性能bug上面花费更多的时间，有的时候作为这种方案，一定的性能允许出现来改善其他方面的问题。

19. 对比Linux内核的发展历程与商业开发系统的不同之处

20. 软件变更请求通常配制为请求修改或添加特定功能或概念。为了实现这些改变，这些特征或概念必须定位到代码上。在本文中，我们描述的特征和概念位置的场景。该方案是利用电脑辅助搜索软件依赖图的。方案由NCSA的马赛克源代码的案例研究证明。

##终选
3、4、5、7、10（了解符号研究的背景）、11、12、13、15、16、17
