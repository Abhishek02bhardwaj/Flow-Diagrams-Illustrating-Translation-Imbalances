import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('wiki_article_counts.csv')

# Create a scatter plot
plt.scatter(df['wiki'], df['article_count'])

# Set the title and axis labels
plt.title('Wiki article count')
plt.xlabel('Wiki')
plt.ylabel('Article count')

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Display the plot
plt.show()
