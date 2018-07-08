library(effsize)
library(xtable)

good_test <- read.csv("good_tests.csv")
bad_test <- read.csv("bad_tests.csv")
metrics <- colnames(good_test)[9:86]

p_values <- c()
for (metric in metrics) {
  p_values <- c(p_values, wilcox.test(good_test[,metric], bad_test[,metric], paired = F)$p.value)
}

cliff_delta <- c()
cliff_estimate <- c()
for (metric in metrics) {
  res_delta <- cliff.delta(good_test[,metric], bad_test[,metric], paired = F)
  cliff_delta <- c(cliff_delta, as.character(res_delta$magnitude))
  cliff_estimate <- c(cliff_estimate, res_delta$estimate)
}

df <- data.frame(metrics, p_values, cliff_delta, cliff_estimate)
write.csv(df, "rq1.csv", row.names = F)
print(xtable(df, digits=4))
