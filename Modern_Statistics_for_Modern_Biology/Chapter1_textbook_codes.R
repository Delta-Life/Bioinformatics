# codes on textbook
# 1.2 A real example
dpois(x = 3, lambda = 5)
dpois(x = 0:12, lambda = 5)
barplot(dpois(0:12, 5), names.arg = 0:12, col = "red")

# 1.3 Using discrete probability models
genotype = c("AA","AO","BB","AO","OO","AO","AA","BO","BO",
             "AO","BB","AO","BO","AB","OO","AB","BB","AO","AO")
table(genotype)
genotypeF = factor(genotype)
levels(genotypeF)
table(genotypeF)

# 1.3.1 Bernoulli trials
rbinom(15, prob = 0.5, size = 1)

# 1.3.2 Binomial success counts
rbinom(1, prob = 2/3, size = 12)

probabilities = dbinom(0:15, prob = 0.3, size = 15)
round(probabilities, 2)
barplot(probabilities, names.arg = 0:15, col = "red")

# 1.3.3 Poisson distributions
5^3 * exp(-5) / factorial(3)

rbinom(1, prob = 5e-4, size = 10000)
simulations = rbinom(n = 300000, prob = 5e-4, size = 10000)
barplot(table(simulations), col = "lavender")

# 1.3.4 A generative model for epitope detection
