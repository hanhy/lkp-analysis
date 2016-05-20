##This functiong below can count pearson correlation between metrics
pearson <- function(v1, v2){
  
  
  
  row = nrow(target)
  col = ncol(target)
  for (c in 7:col){
    vector <- as.numeric(target[,c])
    target[,c] <- (vector - min(vector))/(max(vector) - min(vector))
  }	
  target
}


data = read.table("~/lkp-analysis/PCA_part1/test.csv",header=F, sep=",")  #读取csv文件  
data    #输出向量data4中的内容  
class(data)
