title: index0
speaker: 韩慧阳
url: https://github.com/ksky521/nodePPT
transition: cards
files: /css/theme.moon.css

[slide]

# Toddler: Detecting Performance Problems via Similar Memory-Access Patterns

[slide]
#ABSTRACT {:&.flexbox.vleft}
- Performance bugs usually require more human effort to detected
- TODDLER(presented in this paper) reports code loops whose computation has repetitive and partially similar memory-access patterns across loop iterations

[slide]
#INTRODUCTION {:&.flexbox.vleft}
- Why are performance bugs so difficult to detected?
- Why is TODDLER effective for performance bugs detecting?
- What did they study with TODDLER?

[slide]
# Why are performance bugs(PBs) so difficult to detected? {:&.flexbox.vleft}
- Programmer usually follow these three steps toe detect functional bugs
	- Write as many and as diverse tests as allowed by the testing budget
	- Run these tests and use automated oracles to find which tests fail
	- inspect _only_ the failing tests(most PBs won't result in fails)
- Programmers could find code which takes time, but not that takes unnecessary time(waste)

[slide]
#Why is TODDLER effective for performance bugs detecting {:&.flexbox.vleft}
- TODDLER reports tests that execute loops whose computation is repetitive and very similar across iterations
- TODDLER is designed based on two observations about PBs
	- Many severe PBs are contained by nested loops
	- Wasted computation is often reflected by repetitive and partially similar memory accesses across loop iterations

[slide]
#What did they study with TODDLER {:&.flexbox.vleft}
- Java、C++
- GCC、Mozilla、MySQL
- Google Core Libraries、JUnit、Apache Collections、JDK、JFreeChart

[slide]
#STUDY OF PERFORMANCE BUGS {:&.flexbox.vleft}
- 90% PBs involve loops and more than 50% of PBs involve at least two levels of loops
- PBs that involved nested loops can be categorized along two dimensions:
	- Is the PB in the inner or the outer loop
	- Is the PB caused by redundant computation or ineffcient computation?
- They categorized the real-world PBs into four types along the two dimensions

[slide]
#PBs category {:&.flexbox.vleft}
- **Redundancy in Outer Loops**
- **Redundancy in Inner Loops**
- **Inefficient Outer Loops**
- **Inefficient Inner Loops**

[slide]
#Implications {:&.flexbox.vleft}
- **Why do developers need automated support for performance testing?**
	- Many PBs are embeded in code written by different developers
	- It is unavoidable to developer who don't know the inner details

[slide]
#Implications {:&.flexbox.vleft}
- **Why do we focus on nested-loop performance bugs?**
	- Bugs that involve nested loops usually have severe performance
	- The outer loop will amplify the performance penalty of the inner loop

[slide]
#Implications {:&.flexbox.vleft}
- **How can we detect nested-loop performance bugs?**
	- Nested-loop PBs often involve repeated memory-access patterns
	- One of the feature is these iterations have the same input and the same result(or a similar dataset)

[slide]
#TODDLER DESIGN AND IMPLEMENTATIONS {:&.flexbox.vleft}
- Instrumentation
- Collecting IPCS-Sequences
- Data Structures
- Algorithm for Finding Performance Bugs
- Measureing Similarity
- Filtering Reads
- Implementations

[slide]
# INstrumentation
- Because
[slide]
# EXPERIMENTAL RESULTS




































[slide]
#Reasons {:&.flexbox.vleft}
- It covers representative application domains
- It covers representative workloads
- It covers diverse software stacks
- It considers data volume and veracity

[slide]
#Methodology {:&.flexbox.vleft}
- Methodologies used to analyze the software stack’s impact on big data workloads
	- Workload Selection
	- Microarchitectural Metric Selection
	- **Removing Correlated Data**(For metrics)
	- **Measuring Similarity**(For worloads)
	- **Removing Redundancy**

[slide]
#Experimental setup {:&.flexbox.vleft}
- Describe the exprimental environment and explain how to obtain the microarchitectural-level data
	- Hardware configurations
	- Software environments
	- Performance data collection

[slide]
#Software stacks impact {:&.flexbox.vleft}
- (Dis)similarity Analysis
- Principle Component Space Analysis
- Differentiating Hadoop and Spark

[slide]
#The result of the PCA and hierarchical clustering.
- (Dis)similarity Analysis
![PCA and hierarchical clustering result](../img/index0_fig1.png)

[slide]
#(Dis)similarity Analysis {:&.flexbox.vleft}
- **Observation 1**:The linkage distance between different software stacks is longer than them between different algorithms
- **Observation 2**:Algorithms on different software stacks do not get clustered together in the first clustering iteration
- **Observation 3**:After the first iteration, workloads based on the same software stack are easier to cluster together
- **Observation 4**:workloads using the same software stack to implement similar algorithms have similar behaviors
- **Observation 5**:Hadoop-based workloads have more similarities with each other than their Spark-

[slide]
#Principle Component Space Analysis {:&.flexbox.vleft}
- Scatter plot of workloads using the first and second principle components
![fig2](../img/index0_fig2.png)

[slide]
#Principle Component Space Analysis {:&.flexbox.vleft}
- Scatter plot of workloads using the third and fourth principle components
![fig3](../img/index0_fig3.png)

[slide]
#Principle Component Space Analysis {:&.flexbox.vleft}
- Factor loadings for all workloads
![fig4](../img/index0_fig4.png)

[slide]
#Principle Component Space Analysis {:&.flexbox.vleft}
- Spark-based workloads show more diversity than the Hadoop-based workloads

[slide]
# Differentiating Hadoop and Spark {:&.flexbox.vleft}
- PC2 could help to differentiate Hadoop and Spark
- Use metrics which dominate PC2’s values, we could plot a figure

[slide]
# Differentiating Hadoop and Spark {:&.flexbox.vleft}
- Metrics causing Hadoop and Spark to behave differently
![fig5](../img/index0_fig5.png)

[slide]
# Some observations {:&.flexbox.vleft}
- **Observation 6**: The S-workloads have a large amount of L3 cache misses per kilo instructions, about twice those of the H-workloads.
- **Observation 7**: The H-workloads have more data shared TLB hits and fewer DTLB misses than the S-workloads.
- **Observation 8**: The H-workloads have more instruction fetch stalls, whereas the S-workloads have more resource related stalls.
- **Observation 9**: The S-workloads have more SNOOP HIT and SNOOP HITE responses than H-workloads

[slide]
# Subsetting {:&.flexbox.vleft}
- How to facilitate workload subsetting
	- Clustering
	- Selecting Representative Workloads
	- BigDataBench Simulator Version

[slide]
# Clustering {:&.flexbox.vleft}
- We ultimately cluster the 32 workloads into seven groups which are listed in Table IV
![table4](../img/index0_table4.png)

[slide]
# Selecting Representative Workloads {:&.flexbox.vleft}
- There are two approaches(center and boundary), and the second is more diverse
![table5](../img/index0_table5.png)

[slide]
# Selecting Representative Workloads {:&.flexbox.vleft}
- The result of the second approache
![fig6](../img/index0_fig6.png)

[slide]
# BigDataBench Simulator Version {:&.lexbox.vleft}
- They deploy the representative applications on a full-system simulator and release the simulator images as the BigDataBench simulator version

[slide]
#The End













