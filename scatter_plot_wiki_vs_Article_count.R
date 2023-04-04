# Load the ggplot2 library
library(ggplot2)

# Read the CSV file into a data frame
data <- read.csv("filename.csv")

# Create a scatter plot using ggplot2
ggplot(data, aes(x = wiki, y = article_count)) + 
  geom_point() +
  labs(x = "Wiki", y = "Article Count") +
  ggtitle("Wiki vs Article Count")

