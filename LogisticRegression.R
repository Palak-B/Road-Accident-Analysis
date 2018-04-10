setwd("C:\\Users\\Palak\\Desktop\\R\\Assignment 2")
mydata <- read.csv("acc.csv","r")
mydata
head(mydata)
summary(mydata)
sapply(mydata, sd)
index <- 1:nrow(mydata)
index
trainindex <- sample(index, trunc(length(index)/2))
trainindex
trainset <- mydata[trainindex, ]
trainset
testset <- mydata[-trainindex, ]
mylogit <- glm(Casualty_Severity ~ Road_Surface+Lighting_Conditions+Weather_Conditions, data = trainset, family = "binomial")
predict <- predict(mylogit, testset,type = 'response')
table(testset$admit, predict > 0.5)
