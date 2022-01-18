# Questions
# Q 1.3
cases = c(rbinom(10, prob = 0.3, size = 15))
y = table(cases)
names(y)[which(y==max(y))]

# Q 1.4
dbinom(3, prob = 2/3, size = 4)
choose(4, 3) * (2/3) ** 3 * (1/3)

# Q 1.5
barplot(dpois(0:12, 5), names.arg = 0:12, col = "red")
