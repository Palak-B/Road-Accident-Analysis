#setwd("F://Academic//EvenSem2018//RExercises//")
sample <- read.table("acc.csv",header=TRUE,sep=",")
traindata <- as.data.frame(sample[1:1500,])
testdata <- as.data.frame(sample[1600,])
library(e1071)
model <- naiveBayes(Casualty.Severity ~ Road.Surface+Lighting.Conditions+Weather.Conditions,traindata)
#play is the class and rest of the attributes become features
model
results <- predict (model,testdata)
results
testdata
model1 = naiveBayes(Play ~., traindata, laplace=.01)
model1
results1 <- predict (model1,testdata)
# display results
results1


