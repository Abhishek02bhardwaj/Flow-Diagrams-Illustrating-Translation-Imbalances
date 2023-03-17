# load the required packages
library(networkD3)
library(tidyverse)

# read the data from the CSV file
sankey_data <- read.csv("C:/Users/abhis/PycharmProjects/outreachy/task 5/output.csv")

# create a data frame for the Sankey plot
sankey_plot_data <- sankey_data %>%
  select(from = translations_from, to = translations_to, value = article_count)

# create the nodes data frame
nodes <- data.frame(name = unique(c(sankey_plot_data$from, sankey_plot_data$to)))
nodes$ID <- seq_len(nrow(nodes))

# create the Sankey plot
sankeyPlot <- sankeyNetwork(Links = sankey_plot_data, 
                            Nodes = nodes,
                            Source = "from",
                            Target = "to", 
                            Value = "value",
                            NodeID = "name",
                            sinksRight = FALSE)

# display the Sankey plot
sankeyPlot

