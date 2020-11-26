> #!/usr/bin/env Rscript

# I) Statistiques descriptive
## Exercice 0

```R
cats <- read.table(file="cats.txt", sep=" ", header=T)
names(cats)
nrow(cats)
```

## Exercice 1

### 1)
```R
names(cats)
```

### 2)
```R
length(cats)
```

### 3)
```R
cats[1:10,]
attach(cats)
```

## Exercice 2
### 1)
```R
mean(Bwt)
quantile(Bwt, 0.5)
quantile(Bwt, 0.25)
quantile(Bwt, 0.5)
quantile(Bwt, 0.75)
var(Bwt)
sd(Bwt)
diff(range(Bwt))
IQR(Bwt)
```

### 2)
```R
summary(cats)
```

## Exercice 3
### 1)
```R
boxplot(Hwt, Bwt)
boxplot(Bwt, Hwt)

hist(Bwt, breaks=10)
hist(Hwt, breaks=10, col="green")

par(mfrow=c(1,1))
boxplot(Bwt)
boxplot(Bwt, Hwt)
```


## Exercice 4
```R
histo = hist(Bwt)
histo$counts
```

# II) Variable Qualitative
```R
class(Sex)
levels(Sex)
```

## Exercice 5
```R
table(Sex)
prop <- table(Sex)/length(Sex)
barplot(prop)
plot(prop)
pie(prop)

boxplot(var.num ~ var.facteur)
```

## Exercice 6
```R
boxplot(Bwt ~ Sex)
boxplot(Hwt ~ Sex)
```

## Exercice 7
### 1)
```R
plot(Bwt, Hwt)
```

### 2)
```R
cov(Bwt, Hwt)
cor(Bwt, Hwt)
```

### 3)
```R
plot(Hwt, Bwt)
```