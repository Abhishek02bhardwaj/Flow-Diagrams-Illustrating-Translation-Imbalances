library(circlize)

# Read in the CSV file
mydata <- read.csv("C:/Users/abhis/PycharmProjects/outreachy/task 5/output.csv")

# Manipulate the data to prepare it for the chord diagram
mydata <- mydata[,c("translations_from", "translations_to", "article_count")] # select the columns you need
colnames(mydata) <- c("From", "To", "Value") # rename the columns
mydata <- aggregate(Value ~ From + To, mydata, sum) # group by From and To, summing the values

# Create the chord diagram
chordDiagram(mydata, directional = 1, direction.type = c("diffHeight", "arrows"), link.arr.type = "big.arrow")