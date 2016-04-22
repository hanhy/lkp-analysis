##This functiong below can normlize a matrix
Normalize <- function(target){
	row = nrow(target)
	col = ncol(target)
	for (c in 1:col){
		vector <- as.numeric(target[,c])
		target[,c] <- (vector - min(vector))/(max(vector) - min(vector))
	}	
	target
}

#1. computing principal components(PC) number

ori_data <- read.csv('washeddata.csv')#load data
norm_data <-Normalize(as.matrix(ori_data))#Normlize data
print type(norm_data)
#print(norm_data)#print to test

##We will use the normlized data to do PCA
library(psych)
fa.parallel(Harman23.cor$cov,n.obs=302,fa="pc",n.iter=100,show.legend=FALSE,main="Scree plot with parallel analysis")

#2. Extract principal components
library(psych)  
pc<-principal(norm_data, nfactors=10, scores = TRUE)
print (pc)

#3. Obtain principal components coefficient
round(unclass(pc$weights),2)