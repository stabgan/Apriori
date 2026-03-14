# Apriori — Association Rule Learning in R
# Discovers frequent itemsets in transaction data using the arules package.

# install.packages('arules')
library(arules)

# Data Preprocessing — read directly as transactions
dataset <- read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

# Training Apriori on the dataset
rules <- apriori(data = dataset, parameter = list(support = 0.004, confidence = 0.2))

# Visualising the results — top 10 rules by lift
inspect(sort(rules, by = 'lift')[1:10])
