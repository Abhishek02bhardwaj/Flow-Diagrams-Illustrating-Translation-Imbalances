library(circlize)

# Read in the CSV file
mydata <- read.csv("C:/Users/abhis/PycharmProjects/outreachy/task 5/output.csv")

# Manipulate the data to prepare it for the chord diagram
mydata <- mydata[!(mydata$translations_from %in% c("en", "es", "ru", "fr")) & !(mydata$translations_to %in% c("en", "es", "ru", "fr")), c("translations_from", "translations_to", "article_count")] # select the columns you need and exclude specified languages
colnames(mydata) <- c("From", "To", "Value") # rename the columns
mydata <- aggregate(Value ~ From + To, mydata, sum) # group by From and To, summing the values

# Create the chord diagram
chordDiagram(mydata, directional = 1, direction.type = c("diffHeight", "arrows"), link.arr.type = "big.arrow")
