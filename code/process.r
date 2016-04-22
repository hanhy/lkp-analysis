
first <- function(x){sort(x)[1];}; 
spread <- function(x){ length(table(as.character(x))); };

x <- read.table("bsd.l2", sep=";",comment.char="", quote="",col.names=c("v","an","cn","ae","ce","line","at","ct","f","cmt"));

x <- read.table("linux.l2", sep=";",comment.char="", quote="",col.names=c("v","an","cn","ae","ce","line","at","ct","f","cmt"));

#x$t <- as.integer(x$t);
x$y <- floor(x$at/3600/24/365.25)+1970;
x$q <- floor(x$at/3600/24/365.25*4)/4+1970;
x$m <- floor(x$at/3600/24/365.25*12)/12+1970;
x$ty<-x$at/3600/24/365.25+1970;

tmin <- tapply(x$ty, x$l, min, na.rm=T);
x$fr <- tmin[match(x$l,names(tmin))];
tmax <- tapply(x$ty, x$l, max, na.rm=T);
x$to <- tmax[match(x$l,names(tmax))];
x$tenure <- x$ty-x$fr;
x$tt <- ceiling((x$tenure+.000001)*12); # tenure months, .000001 is used to spare, e.g., one delta people

abym <- tapply(x$ae,x$m,spread);
vbym <- tapply(x$v,x$m,length);

png("chgovertime.png", width=800,height=600);
plot(vbym/10,main = "# of changes/authors over time",type="l",xlab="Tenure (months)",ylab="# LTCs each month");
lines(abym,col=2);
legend(80, max(vbym/10),legend=c("# changes/10","# authors"),cex=1,lwd=2,col=rep(1:2),bg="white"); 
dev.off();

x$ff<-sub(".*/","",x$f,perl=T,useBytes=T);
x$ext<-tolower(sub(".*\\.","",x$ff,perl=T,useBytes = T)); 
x$mmod<-sub("^([^/]*/[^/]*)/.*","\\1", x$f, perl=T,useBytes=T);

tot <- tapply(x$tt, x$ae,length);
ten <- tapply(x$tt, x$ae,max);
x$tot <- tot[match(x$ae,names(tot))]; # number of commits overall
x$prod <- (tot/ten)[match(x$ae,names(tot/ten))];

x$isclean <- grepl("clean|maintenanc|reorganiz|refactor", x$cmt, ignore.case=TRUE); #cleanup, clean up, cleaning up, clean out
x$isl10n <- grepl("translat|l10n|localization|i18n|internationalization|documentation|locale", x$cmt, ignore.case=TRUE);
x$istest <- grepl("test|build", x$cmt, ignore.case=TRUE);
x$isobsolete <- grepl("obsolete&remov", x$cmt, ignore.case=TRUE);
x$isclean[x$isobsolete==1] <- 1;
x$isobsolete <- NULL;
x$modl10n <- grepl("translat|l10n|localization|i18n|internationalization|documentation|locale|user", x$mmod, ignore.case=TRUE);
x$modtest <- grepl("test|build", x$mmod, ignore.case=TRUE);


