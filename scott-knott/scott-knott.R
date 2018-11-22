library(ScottKnottESD)
library(dplyr)

# read the frame
# - the first one is for the model with only static features
# - the second line (the one commented) is for the model with line covearage too
frame <- read.csv("features_importance_static_rfc.csv")
# frame <- read.csv("features_importance_dynamic_rfc.csv")

# transpose the matrix and put the features as column name
frame <- transpose(frame)
colnames(frame) <- as.character(frame[1,])
frame <- frame[-1,]
rownames(frame) <- NULL

# remove the columns that have all 0 as value
frame <- mutate_all(frame, function(x) as.numeric(as.character(x)))
frame = frame[, colSums(frame != 0) > 0]

# do the analysis and print the groups
# the ScottKnottESD has also other built-in methods to plot graphs and compute other statistics
sk <- sk_esd(frame)
print(sk_esd(frame))
