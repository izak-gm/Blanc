x <-c(34,12,60,23,45,71)
  labels<-c("Wales","Canada","India","Pakistan","USA","Spain")
  piepercent<-round(100*x/sum(x),1)
  png(file=("contries.png"))
pie(x,labels=piepercent,main="countries",col = rainbow(length(x)))
legend("topright",c("Wales","Canada","India","Pakistan","USA","Spain"),cex=0.8,
fill=rainbow(length(x)))
dev.off()


