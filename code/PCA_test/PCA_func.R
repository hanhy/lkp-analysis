library(psych)
fa.parallel(USJudgeRatings[,-1],fa="PC",n.iter=100,show.legend=FALSE,main="Screen plot with parallel analysis")

library(psych)
pc<-principal(USJudgeRatings[,-1],nfactors=1)
pc

library(psych)
fa.parallel(Harman23.cor$cov,n.obs=302,fa="pc",n.iter=100,show.legend=FALSE,main="Scree plot with parallel analysis")

install.packages("GPArotation")
library(GPArotation)
rc<-principal(Harman23.cor$cov,nfactors=2,rotate="varimax")
rc

library(psych)
pc<-principal(USJudgeRatings[,-1],nfactors=1,score=TRUE)
head(pc$scores)

cor(USJudgeRatings$CONT,PC$scores)

library(psych)
rc<-principal(Harman23.cor$cov,nfactor=2,rotate="varimax")
round(unclass(rc$weights),2)

options(digits=2)
covariances<-ability.cov$cov
correlations<-cov2cor(covariances)
correlations

library(psych)
convariances<-ability.cov$cov
correlations<-cov2cor(covariances)
fa.parallel(correlations,n.obs=112,fa="both",n.iter=100,main="Scree plots with parallel analysis")

fa<-fa(correlations,nfactors=2,rotate="none",fm="pa")
fa

fa.varimax<-fa(correlations,nfactors=2,rotate="varimax",fm="pa")
fa.varimax

fa.promax<-fa(correlations,nfactors=2,rotate="promax",fm="pa")
fa.promax

fsm<-function(oblique){
  if(class(oblique)[2]=="fa"&is.null(oblique$Phi)){
    warning("Object doesn't look like oblique EFA")
  }else{
    P<-unclass(oblique$loading)
    F<-P%*%oblique$Phi
    colnames(F)<-c("PA1","PA2")
    return (F)
  }
}
fsm(fa.promax)

factor.plot(fa.promax,labels=rownames(fa.promax$loadings))

fa.diagram(fa.promax,simple=TRUE)

fa.promax$weights