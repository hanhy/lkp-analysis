title: index0
speaker: 韩慧阳
url: https://github.com/ksky521/nodePPT
transition: cards
files: /css/theme.moon.css

[slide]

# Characterizing and Subsetting Big Data Workloads

[slide]
#Abstract {:&.flexbox.vleft}
- Big data benchmark suites must include a dicersity of data and workloads
- This diversity bring great chanllenges
- What did they do in this paper?

[slide]
#Chanllenges {:&.flexbox.vleft}
- Thorough understanding is needed
- Simulation-based reasearch methods become prohibitively expensive for big data
- More and more software stacks are proposed to facilitate the development of big data applications

[slide]
#What they did {:&.flexbox.vleft}
- Use PCA to identify the most important characteristics from 45 
- Apply a clustering technique to the PCs from PCA
	- To investigate the similarity among big data work loads
	- To verify the importance of including different software stacks
- Select seven workloads ny removing redundant ones and release the BigDataBench simulation version

[slide]
#Introduction {:&.flexbox.vleft}
- What did they specificly do in this paper?
- What did they get from the work?

[slide]
### What they specificly did {:&.flexbox.vleft}
- Propose a general approach to
	- Identify the most important metics for characterizing big data workloads
	- Cull redundant work loads

[slide]
#What they specificly did {:&.flexbox.vleft}
- How do they demonstrate the effectiveness of the approach?
	- Select 32 workloads from BigDataBench to run on **Hadoop** and **Spark**
	- Evaluate them via 45 typical microarchitechural metrics that represent basic characteristics of modern processors
	- PCA and hierarchical clustering

[slide]
#What did they get {:&.flexbox.vleft}
- Software stacks have significant impact on the microarchitectural behaviors of big data workloads(even more than algorithms)
- **We can identify the most important microarchitecturallevel metrics for studying the impact of different software stacks**
- We can successfully subset big data workloads

[slide]
#Background {:&.flexbox.vleft}
- Why choose BigDataBench for their workload characterization

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














